import os.path
import glob
import openMINDS.version_manager
import json


class AtlasGen:

    # class variables used for json Instances
    has_entity_listofdic = []
    has_terminology_listofdic = []
    author_listofdic = []
    has_version_listofdic = []
    version_https = "https://openminds.ebrains.eu/instances/brainAtlasVersion/"
    entity_https = "https://openminds.ebrains.eu/instances/parcellationEntity/"
    person_https = "https://openminds.ebrains.eu/instances/person/"

    # intialize openMinds instance creator
    openMINDS.version_manager.init()
    openMINDS.version_manager.version_selection('v3')
    helper = openMINDS.Helper()
    basic = helper.create_collection()

    def __init__(self, atlas_dir, authors, versions, description, shortname, fullname, homepage,
                 documentation, abbreviation, *areas):
        self.path = atlas_dir
        self.authors = authors
        self.versions = versions
        self.description = description
        self.shortname = shortname
        self.fullname = fullname
        self.homepage = homepage
        self.documentation = documentation
        self.abbreviation = abbreviation
        self.areas = areas

    @classmethod
    def author_gen(cls, instance):
        for item in instance.authors:
            for name in item.keys():
                if name is None:
                    continue
                else:
                    author_dic = {"@id": f"{cls.person_https}{name}"}
                    cls.author_listofdic.append(author_dic)

    @classmethod
    def entity_gen(cls, instance):
        for set in instance.areas:
            for area in set:
                if area is not None:
                    entity_dic = {"@id": f"{cls.entity_https}{instance.abbreviation}_{area}"}
                    cls.has_entity_listofdic.append(entity_dic)
        return cls.has_entity_listofdic

    @classmethod
    def terminology_gen(cls, instance):

        has_terminology_dic = {"@type": "https://openminds.ebrains.eu/sands/ParcellationTerminology", "definedIn": None,
                               "hasEntity": cls.entity_gen(instance)}
        cls.has_terminology_listofdic = has_terminology_dic

    @classmethod
    def version_gen(cls, instance):
        for dic in instance.versions:
            for version in dic.keys():
                has_version_dic = {"@id": f"{cls.version_https}{version}"}
                cls.has_version_listofdic.append(has_version_dic)

    @classmethod
    def generate_instances(cls, instance):
        # generate atlas with necessary information
        cls.author_gen(instance)
        cls.terminology_gen(instance)
        cls.version_gen(instance)

        atlas = cls.basic.add_SANDS_brainAtlas(description=instance.description, shortName=instance.shortname,
                                               fullName=instance.fullname,
                                               author=cls.author_listofdic,
                                               hasTerminology=cls.has_terminology_listofdic,
                                               hasVersion=cls.has_version_listofdic)
        # adding additional info
        cls.basic.get(atlas).digitalIdentifier = [{"@id": f"{instance.documentation}"}]
        cls.basic.get(atlas).homepage = instance.homepage
        # custodian
        cls.basic.get(atlas).custodian = [{"@id": "https://openminds.ebrains.eu/instances/person/kleinArno"}]
        # saving in class-specific path
        cls.basic.save("./instances/PythonLibrary/")

    @staticmethod
    def generate_openminds_instances(instance):
        # copy contents
        latest = max(glob.glob("./instances/PythonLibrary/brainAtlas/*jsonld"))
        with open(latest, 'r') as f:
            data = json.load(f)
            atlas_name = os.path.basename(instance.path).replace(".jsonld", "")
            data["@id"] = f"https://openminds.ebrains.eu/instances/brainAtlas/{atlas_name}"
            f.close()
        # write content to new file
        json_target = open(instance.path, "w")
        json.dump(data, json_target, indent=2, sort_keys=True)
        json_target.write("\n")
        json_target.close()
