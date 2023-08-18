import os.path
import glob
import openMINDS.version_manager
import json
from MarsAtlas_generation import replace_empty_lists


class ParcellationEntityVersionGen:

    # class variables used for json Instances
    has_parent_listOfdic = []
    has_annotation_listOfdic = []
    parent_https = "https://openminds.ebrains.eu/instances/parcellationEntity/"
    entity_version_https = "https://openminds.ebrains.eu/instances/parcellationEntityVersion/"

    # intialize openMinds instance creator
    openMINDS.version_manager.init()
    openMINDS.version_manager.version_selection('v3')
    helper = openMINDS.Helper()
    basic = helper.create_collection()
    addon = helper.create_collection()

    def __init__(self, entity_ver_path, version, version_info, areas_hierachry, abbreviation, versions):
        self.path = entity_ver_path
        self.hierarchy = areas_hierachry
        self.version = version
        self.versions = versions
        self.abb = abbreviation
        self.version_identifier = version_info.get(version).get("version_identifier")
        self.criteriaQualityType = version_info.get(version).get("criteriaQualityType")
        self.annotationCriteriaType = version_info.get(version).get("annotationCriteriaType")
        self.laterality = version_info.get(version).get("laterality")
        self.type = version_info.get(version).get("annotationType")

    @classmethod
    def reset(cls, *args):
        for var_name in args:
            setattr(cls, var_name, [])

    @classmethod
    def parent_dic(cls, abbreviation, parent):
        cls.reset("has_parent_listOfdic")
        if parent is not None:
            has_parent_dic = {"@id": f"{cls.parent_https}{abbreviation}_{parent}"}
            cls.has_parent_listOfdic.append(has_parent_dic)

    @classmethod
    def get_annotation(cls, annotationCriteriaType, criteriaQualityType, laterality, type):
        cls.reset("has_annotation_listOfdic")
        for quality in criteriaQualityType:
            for criteria in annotationCriteriaType:
                for lat in laterality:
                    annotation = cls.addon.add_SANDS_atlasAnnotation(criteriaQualityType=quality, criteriaType=criteria,
                                                                     type=type)
                    cls.addon.get(annotation).laterality = lat
                    cls.addon.save("./instances/PythonLibrary/")
                    latest = max(glob.glob("./instances/PythonLibrary/atlasAnnotation/*jsonld"))
                    with open(latest, 'r') as f:
                        data = json.load(f)
                        data = replace_empty_lists(data)
                        del data["@id"]
                        del data["@context"]
                        data["laterality"] = {"@id": f"https://openminds.ebrains.eu/instances/laterality/{lat}"}
                        data["criteriaType"] = {
                            "@id": f"https://openminds.ebrains.eu/instances/annotationCriteriaType/{criteria}"}
                        data["criteriaQualityType"] = {
                            "@id": f"https://openminds.ebrains.eu/instances/criteriaQualityType/{quality}"}
                        data["type"] = {"@id": f"https://openminds.ebrains.eu/controlledTerms/AnnotationType/{type}"}
                        cls.has_annotation_listOfdic.append(data)
                    f.close()
                    
    @classmethod
    def generate_instances(cls, instance):
        """create person directories, files and instances ind a semi-automatic manner"""
        # if not os.path.isfile(path):
        for area_tuple in instance.hierarchy[instance.version]:
            # get are and parent info
            area = area_tuple[0]
            parent = area_tuple[1]
            # intiliaize instance
            entity_version = cls.basic.add_SANDS_parcellationEntityVersion(name=area, versionIdentifier=instance.version_identifier)
            cls.basic.get(entity_version).lookupLabel = f"{instance.version}_{area}"
            # add info
            cls.parent_dic(instance.abb, parent)
            cls.get_annotation(instance.annotationCriteriaType, instance.criteriaQualityType, instance.laterality, instance.type)
            cls.basic.get(entity_version).hasParent = cls.has_parent_listOfdic
            cls.basic.get(entity_version).hasAnnotation = cls.has_annotation_listOfdic
            # save instance
            cls.basic.save("./instances/PythonLibrary/")
            cls.generate_openminds_instances(instance, area)

    @staticmethod
    def generate_openminds_instances(instance, area):
        # copy contents of saved instance
        latest = max(glob.glob("./instances/PythonLibrary/parcellationEntityVersion/*jsonld"))
        with open(latest, 'r') as f:
            data = json.load(f)
            data = replace_empty_lists(data)
            data["@id"] = f"https://openminds.ebrains.eu/instances/parcellationEntityVersion/{area}"
        # write content to new file
        json_target = open(f"{instance.path}{instance.version}_{area}.jsonld", "w")
        json.dump(data, json_target, indent=2, sort_keys=True)
        json_target.write("\n")
        json_target.close()
