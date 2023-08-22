import os.path
import glob
import openMINDS.version_manager
import json


class DOIGen:

    # initialize instance creator
    openMINDS.version_manager.init()
    openMINDS.version_manager.version_selection('v3')
    helper = openMINDS.Helper()
    basic = helper.create_collection()

    def __init__(self, doi_dir, documentation, abbreviation):
        self.path = doi_dir
        self.docu = documentation
        self.abb = abbreviation

    @classmethod
    def generate_instances(cls, instance):
        """create DOI directories, files and instances ind a semi-automatic manner"""
        doi_str = "https://doi.org/"
        doi = instance.docu
        doi_stripped = doi.replace(doi_str, "").replace("/", ".")
        if doi is not None:
            cls.basic.add_core_DOI(identifier=doi)
            cls.basic.save("./instances/PythonLibrary/")
            cls.generate_openminds_instances(instance, doi_stripped)

    def generate_openminds_instances(self, doi_stripped):
        # copy contents of created file
        latest = max(glob.glob("./instances/PythonLibrary/DOI/*jsonld"))
        doi_path = f"{self.path}DOI_{self.abb}_{doi_stripped}.jsonld"
        with open(latest, 'r') as f:
            data = json.load(f)
            doi_name = os.path.basename(doi_path).replace(".jsonld", "")
            data["@id"] = f"https://openminds.ebrains.eu/instances/DOI/{doi_name}"
            # write content to new file
        json_target = open(doi_path, "w")
        json.dump(data, json_target, indent=2, sort_keys=True)
        json_target.write("\n")
        json_target.close()
