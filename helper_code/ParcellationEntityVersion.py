
import glob
import openMINDS.version_manager
import json
from MarsAtlas_generation import replace_empty_lists


class ParcellationEntityVersionGen:

    # class variables used for json Instances

    parent_https = "https://openminds.ebrains.eu/instances/parcellationEntity/"
    entity_version_https = "https://openminds.ebrains.eu/instances/parcellationEntityVersion/"

    # intialize openMinds instance creator
    openMINDS.version_manager.init()
    openMINDS.version_manager.version_selection('v3')
    helper = openMINDS.Helper()
    basic = helper.create_collection()

    def __init__(self, entity_ver_path, areas_hierachry, versions):
        self.path = entity_ver_path
        self.hierarchy = areas_hierachry
        self.versions = versions

    @classmethod
    def generate_entity_versions(cls, instance):
        """create person directories, files and instances ind a semi-automatic manner"""
        # if not os.path.isfile(path):
        for version, areas_version in instance.hierarchy.items():
            for area_tuple in areas_version:
                area = area_tuple[0]
                parent = area_tuple[1]
                entity_ver_file_path = f"{instance.entity_ver_path}{version}_{area}.jsonld"
                cls.entity_version_instance_generation(entity_ver_file_path, area, parent, version, instance.versions)