import os.path
import glob
import openMINDS.version_manager
import json


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
            if any(area in tuple for tuple in areas_version):
                if parent_versions:
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


    def entity_instance_generation(cls, instance):
        for area in areas_unique
            versions = cls.version_extraction_PE(area, instance.hierarchy)
            parents = cls.parent_extraction_PE(area, instance)

            # create entity isntance
            entity = cls.basic.add_SANDS_parcellationEntity(name=area)
            cls.basic.get(entity).lookupLabel = f"{instance.abb}_{area}"


        # add entity version creation


        basic.get(entity).hasVersion = has_version_listOfdic

        # add parent structures

        basic.get(entity).hasParent = has_parent_listOfdic
        basic.save(p)




