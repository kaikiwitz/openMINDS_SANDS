import os.path
import glob
import openMINDS.version_manager
import json


class ORCIDGen:
    # initialize instance creator
    openMINDS.version_manager.init()
    openMINDS.version_manager.version_selection('v3')
    helper = openMINDS.Helper()
    basic = helper.create_collection()

    def __init__(self, orcid_path, authors, abbreviation):
        self.path = orcid_path
        self.authors = authors
        self.abb = abbreviation

    @classmethod
    def generate_instances(cls, instance):
        for item in instance.authors:
            for name in item.keys():
                orcid = item.get(name).get("ORCID")
                if orcid is None:
                    continue
                else:
                    cls.basic.add_core_ORCID(identifier=orcid)
                    cls.basic.save("./instances/PythonLibrary/")
                    cls.generate_openminds_instances(instance, name, orcid)

    def generate_openminds_instances(self, name, orcid):
        # copy contents of created file
        latest = max(glob.glob("./instances/PythonLibrary/ORCID/*jsonld"))
        orcid_path = f"{self.path}ORCID_{name}_{os.path.basename(orcid)}.jsonld"
        with open(latest, 'r') as f:
            data = json.load(f)
            orcid_name = os.path.basename(orcid_path).replace(".jsonld", "")
            data["@id"] = f"https://openminds.ebrains.eu/instances/ORCID/{orcid_name}"
            # write content to new file
        json_target = open(orcid_path, "w")
        json.dump(data, json_target, indent=2, sort_keys=True)
        json_target.write("\n")
        json_target.close()
