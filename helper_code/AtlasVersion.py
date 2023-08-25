import glob
import openMINDS.version_manager
import json
from class_utils import replace_empty_lists


class AtlasVersionGen:

    # class variables used for json Instances
    coordinate_space_https = "https://openminds.ebrains.eu/instances/commonCoordinateSpace/"
    accessibility_https = "https://openminds.ebrains.eu/instances/productAccessibility/"
    author_https = "https://openminds.ebrains.eu/instances/person/"
    parcellation_entity_version_https = "https://openminds.ebrains.eu/instances/parcellationEntityVersion/"
    license_https = "https://openminds.ebrains.eu/instances/licenses/"
    version_https = "https://openminds.ebrains.eu/instances/brainAtlasVersion/"

    # intialize openMinds instance creator
    openMINDS.version_manager.init()
    openMINDS.version_manager.version_selection('v3')
    helper = openMINDS.Helper()
    basic = helper.create_collection()

    def __init__(self, version_dir, version, version_info, areas_hierarchy):
        self.path = version_dir
        self.version = version
        self.version_info = version_info
        self.areas = areas_hierarchy
        self.license = version_info.get(version).get("license")
        self.coordinateSpace = version_info.get(version).get("reference_space")
        self.version_innovation = version_info.get(version).get("version_innovation")
        self.version_identifier = version_info.get(version).get("version_identifier")
        self.release_date = version_info.get(version).get("release_date")
        self.short_name = version_info.get(version).get("short_name")
        self.DOI = version_info.get(version).get("digitalIdentifier")
        self.accessibility = version_info.get(version).get("accessibility")
        self.authors = version_info.get(version).get("authors")
        self.altVersions = version_info.get(version).get("altVersion")
        self.newVersions = version_info.get(version).get("newVersion")
        self.homepage = version_info.get(version).get("homepage")
        self.type = version_info.get(version).get('atlasType')
        self.authors_list_of_dic = []
        self.has_entity_listofdic = []
        self.altVersion_list_of_dic = []
        self.newVersion_list_of_dic = []
        self.docu_list_of_dic = []

    @classmethod
    def getLicense(cls, instance):
        license_dic = {"@id": f"{cls.license_https}{instance.license}"}
        return license_dic

    @classmethod
    def getCoordinateSpace(cls, instance):
        coordinate_space_dic = {"@id": f"{cls.coordinate_space_https}{instance.coordinateSpace}"}
        return coordinate_space_dic

    @classmethod
    def getAccessibility(cls, instance):
        accessibility_dic = {"@id": f"{cls.accessibility_https}{instance.accessibility}"}
        return accessibility_dic

    @classmethod
    def authors_version(cls, instance):
        for author in instance.authors:
            author_dic = {"@id": f"{cls.author_https}{author}"}
            instance.authors_list_of_dic.append(author_dic)

    @classmethod
    def terminology_versions(cls, instance):
        # the following variable defines that we just want the "child" structure, we may improve this in
        # the future for cases where
        # we have version specific parent structures
        version_entities = (t[0] for t in instance.areas[instance.version])
        for area in version_entities:
            entity_version_dic = {"@id": f"{cls.parcellation_entity_version_https}{instance.version}_{area}"}
            instance.has_entity_listofdic.append(entity_version_dic)
        terminology_dic = {"@type": "https://openminds.ebrains.eu/sands/ParcellationTerminologyVersion",
                           "definedIn": None, "hasEntity": instance.has_entity_listofdic}
        return terminology_dic

    @classmethod
    def alternativeVersions(cls, instance):
        if instance.altVersions is not None:
            for altVersion in instance.altVersions:
                altVersion_dic = {"@id": f"{cls.version_https}{altVersion}"}
                instance.altVersion_list_of_dic.append(altVersion_dic)

    @classmethod
    def newerVersion(cls, instance):
        if instance.newVersions is not None:
            for newVersion in instance.newVersions:
                newVersion_dic = {"@id": f"{cls.version_https}{newVersion}"}
                instance.newVersion_list_of_dic.append(newVersion_dic)

    @classmethod
    def docugen(cls, instance):
        docu = {"@id": f"{instance.DOI}"}
        instance.docu_list_of_dic.append(docu)

    @classmethod
    def generate_instances(cls, instance):
        cls.authors_version(instance)
        cls.docugen(instance)
        cls.alternativeVersions(instance)
        cls.newerVersion(instance)
        atlas_version = cls.basic.add_SANDS_brainAtlasVersion(license=cls.getLicense(instance),
                                                              coordinateSpace=cls.getCoordinateSpace(instance),
                                                              accessibility=cls.getAccessibility(instance),
                                                              hasTerminology=cls.terminology_versions(instance),
                                                              fullDocumentation=instance.docu_list_of_dic,
                                                              versionInnovation=instance.version_innovation,
                                                              versionIdentifier=instance.version_identifier,
                                                              releaseDate=instance.release_date,
                                                              shortName=instance.short_name)

        cls.basic.get(atlas_version).isAlternativeVersionOf = instance.altVersion_list_of_dic
        cls.basic.get(atlas_version).isNewVersionOf = instance.newVersion_list_of_dic
        cls.basic.get(atlas_version).author = instance.authors_list_of_dic
        cls.basic.get(atlas_version).homepage = instance.homepage
        cls.basic.get(atlas_version).type = {"@id": f"https://openminds.ebrains.eu/instances/atlasType/"
                                                    f"{instance.type}"}
        cls.basic.save("./instances/PythonLibrary/")
        cls.generate_openminds_instances(instance)

    def generate_openminds_instances(self):
        # copy contents of created file
        latest = max(glob.glob("./instances/PythonLibrary/brainAtlasVersion/*jsonld"))
        with open(latest, 'r') as f:
            data = json.load(f)
            data = replace_empty_lists(data)
            data["@id"] = f"https://openminds.ebrains.eu/instances/brainAtlasVersion/{self.version}"
        # write content to new file
        json_target = open(f"{self.path}{self.version}.jsonld", "w")
        json.dump(data, json_target, indent=2, sort_keys=True)
        json_target.write("\n")
        json_target.close()
