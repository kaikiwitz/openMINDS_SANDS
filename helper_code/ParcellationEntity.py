import glob
import openMINDS.version_manager
import json
from class_utils import replace_empty_lists


class ParcellationEntityGen:

    # class variables used for json Instances
    parent_https = "https://openminds.ebrains.eu/instances/parcellationEntity/"
    entity_version_https = "https://openminds.ebrains.eu/instances/parcellationEntityVersion/"
    # intialize openMinds instance creator
    openMINDS.version_manager.init()
    openMINDS.version_manager.version_selection('v3')
    helper = openMINDS.Helper()
    basic = helper.create_collection()

    def __init__(self, entity_path, abbreviation, areas_hierachry, areas_unique, parents_unique):
        self.path = entity_path
        self.abb = abbreviation
        self.hierarchy = areas_hierachry
        self.areas = areas_unique
        self.parents = parents_unique

    @classmethod
    def version_extraction_PE(cls, area, hierarchy, parent_versions=True):
        entity_version_list = []
        has_version_listOfdic = []
        # check whether they are part of a specific version, add version
        for version, areas_version in hierarchy.items():
            if any(area in tuple for tuple in areas_version) & parent_versions:
                # if parent_versions:
                entity_version_list.append(version)
        if entity_version_list:
            for version in entity_version_list:
                has_version_dic = {"@id": f"{cls.entity_version_https}{version}_{area}"}
                has_version_listOfdic.append(has_version_dic)
        return has_version_listOfdic

    @classmethod
    def parent_extraction_PE(cls, area, instance):
        parent_structure_list = []
        has_parent_listOfdic = []
        # check whether they are part of a specific version, add version
        for version, areas_version in instance.hierarchy.items():
            if any(area in tuple for tuple in areas_version):
                # loop over the areas of the version to extract the parent structures
                for i, tuple in enumerate(areas_version):
                    if area in tuple and area is not None:
                        parent_structure_list.extend(areas_version[i][tuple.index(area) + 1:])
                        parent_structure_list = [x for x in parent_structure_list if x is not None]
                        continue
        if parent_structure_list:
            has_parent_dic = {"@id": f"{cls.parent_https}{instance.abb}_{parent_structure_list[0]}"}
            has_parent_listOfdic.append(has_parent_dic)
        return has_parent_listOfdic

    @classmethod
    def generate_instances(cls, instance):
        for area in instance.areas:
            versions = cls.version_extraction_PE(area, instance.hierarchy)
            parents = cls.parent_extraction_PE(area, instance)

            # create entity isntance
            entity = cls.basic.add_SANDS_parcellationEntity(name=area)
            cls.basic.get(entity).lookupLabel = f"{instance.abb}_{area}"
            # add entity version creation
            cls.basic.get(entity).hasVersion = versions
            # add parent structures
            cls.basic.get(entity).hasParent = parents
            cls.basic.save("./instances/PythonLibrary/")
            # create openMINDS instances
            cls.generate_openminds_instances(instance, area)

        for area in instance.parents:
            versions = cls.version_extraction_PE(area, instance.hierarchy, parent_versions=False)
            parents = cls.parent_extraction_PE(area, instance)

            # create entity isntance
            entity = cls.basic.add_SANDS_parcellationEntity(name=area)
            cls.basic.get(entity).lookupLabel = f"{instance.abb}_{area}"
            # add entity version creation
            cls.basic.get(entity).hasVersion = versions
            # add parent structures
            cls.basic.get(entity).hasParent = parents
            cls.basic.save("./instances/PythonLibrary/")
            # create openMINDS instances
            cls.generate_openminds_instances(instance, area)

    def generate_openminds_instances(self, area):
        latest = max(glob.glob("./instances/PythonLibrary/parcellationEntity/*jsonld"))
        with open(latest, 'r') as f:
            data = json.load(f)
            data = replace_empty_lists(data)
            data["@id"] = f"https://openminds.ebrains.eu/instances/parcellationEntity/{self.abb}_{area}"
        # write content to new file
        json_target = open(f"{self.path}{self.abb}_{area}.jsonld", "w")
        json.dump(data, json_target, indent=2, sort_keys=True)
        json_target.write("\n")
        json_target.close()
