import os.path
import glob
import openMINDS.version_manager
import json


class AtlasVersion:

    # class variables used for json Instances

    # intialize openMinds instance creator
    openMINDS.version_manager.init()
    openMINDS.version_manager.version_selection('v3')
    helper = openMINDS.Helper()
    basic = helper.create_collection()

    def __init__(self, version_dir, versions, areas_hierarchy):
        self.path = version_dir
        self.versions = versions
        self.areas = areas_hierarchy

    # THE LOOP NEEDS TO BE DONE OUTSIDE THE CLASS!!!!
    @classmethod
