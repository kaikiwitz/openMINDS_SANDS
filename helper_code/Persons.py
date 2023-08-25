import glob
import openMINDS.version_manager
import json


class PersonGen:

    # initialize instance creator
    openMINDS.version_manager.init()
    openMINDS.version_manager.version_selection('v3')
    helper = openMINDS.Helper()
    basic = helper.create_collection()

    def __init__(self, person_dir, authors):
        self.path = person_dir
        self.authors = authors

    @classmethod
    def generate_instances(cls, instance):
        for item in instance.authors:
            for name in item.keys():
                if name is None:
                    continue
                else:
                    author = cls.basic.add_core_person(givenName=item[name].get("givenName"))
                    cls.basic.get(author).familyName = item[name].get("familyName")
                    cls.basic.get(author).digitalIdentifier = {"@id": item[name].get("ORCID")}
                    cls.basic.save("./instances/PythonLibrary/")
                    cls.generate_openminds_instances(instance, name)

    def generate_openminds_instances(self, name):
        # copy contents of created file
        latest = max(glob.glob("./instances/PythonLibrary/person/*jsonld"))
        with open(latest, 'r') as f:
            data = json.load(f)
            # person = os.path.basename(person_path).replace(j, "")_name
            data["@id"] = f"https://openminds.ebrains.eu/instances/person/{name}"
        # write content to new file
        person_path = f"{self.path}{name}.jsonld"
        json_target = open(person_path, "w")
        json.dump(data, json_target, indent=2, sort_keys=True)
        json_target.write("\n")
        json_target.close()
