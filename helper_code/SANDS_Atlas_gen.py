import os.path
from Atlas_data import MarsAtlas, DKTAtlas
from class_utils import AutoInitializeAndCall
from Persons import PersonGen
from DOIs import DOIGen
from ORCIDs import ORCIDGen
from Atlas import AtlasGen
from AtlasVersion import AtlasVersionGen
from ParcellationEntity import ParcellationEntityGen
from ParcellationEntityVersion import ParcellationEntityVersionGen


def main(BA_path, PERSON_path, DOI_path, ORCID_path, BAV_path, PE_path, PEV_path):
    atlases = [MarsAtlas, DKTAtlas]
    for atlas in atlases:
        # get Mars Atlas data
        data_atlas = atlas()
        authors, documentation, description, abbreviation, fullname, shortname, \
            homepage, versions, areas_versions_hierachry, areas_unique, parents_unique = data_atlas.get_data()
        instantiation_persons(PERSON_path, authors, abbreviation)
        instantiation_dois(DOI_path, documentation, abbreviation)
        instantiation_orcids(ORCID_path, authors, abbreviation)
        instantiation_BA(BA_path, authors, versions, description, shortname, fullname, homepage, documentation,
                         abbreviation, areas_unique, parents_unique)
        instantiation_PE(PE_path, abbreviation, areas_versions_hierachry, areas_unique, parents_unique)
        instantiation_BAV(BAV_path, versions, areas_versions_hierachry)
        instantiation_PEV(PEV_path, abbreviation, versions, areas_versions_hierachry)


def instantiation_persons(path, authors, abbreviation):
    print(f"Creating openMINDS-SANDS compatible Atlas Instance for {abbreviation}...")
    os.makedirs(path, exist_ok=True)
    Persons = PersonGen(path, authors)
    Person_handler = AutoInitializeAndCall(Persons)
    Person_handler.call_methods((Persons.generate_instances, Persons))
    print(f"...Persons Instances for {abbreviation} created")


def instantiation_dois(path, documentation, abbreviation):
    print(f"Creating openMINDS-SANDS compatible DOIs for {abbreviation}...")
    os.makedirs(path, exist_ok=True)
    DOIs = DOIGen(path, documentation, abbreviation)
    DOI_handler = AutoInitializeAndCall(DOIs)
    DOI_handler.call_methods((DOIs.generate_instances, DOIs))
    print(f"...DOI Instances for {abbreviation} created")


def instantiation_orcids(path, authors, abbreviation):
    print(f"Creating openMINDS-SANDS compatible ORCIDs for {abbreviation}...")
    os.makedirs(path, exist_ok=True)
    ORCIDs = ORCIDGen(path, authors, abbreviation)
    ORCID_handler = AutoInitializeAndCall(ORCIDs)
    ORCID_handler.call_methods((ORCIDs.generate_instances, ORCIDs))
    print(f"...ORCID Instances for {abbreviation} created")


def instantiation_BA(path, authors, versions, description, shortname, fullname, homepage, documentation,
                     abbreviation, areas, parents):
    print(f"Creating openMINDS-SANDS compatible Atlas Instance for {abbreviation}...")
    path = f"{path}{fullname}.jsonld"
    Atlas = AtlasGen(path, authors, versions, description, shortname, fullname, homepage, documentation,
                     abbreviation, areas, parents)
    Atlas_handler = AutoInitializeAndCall(Atlas)
    Atlas_handler.call_methods((Atlas.generate_instances, Atlas))
    print(f"...Atlas Instance for {abbreviation} created")


def instantiation_PE(path, abbreviation, areas_hierachry, areas, parents):
    path = f"{path}{abbreviation}/"
    os.mkdir(path)
    print(f"Creating openMINDS-SANDS compatible Parcellation Entitiy Instances for {abbreviation}...")
    Parcellations = ParcellationEntityGen(path, abbreviation, areas_hierachry, areas, parents)
    Parcellations_handler = AutoInitializeAndCall(Parcellations)
    Parcellations_handler.call_methods((Parcellations.generate_instances, Parcellations))
    print(f"...Parcellation Entities for {abbreviation} created")


def instantiation_BAV(path, versions, areas_hierachry):
    for dic in versions:
        for version in dic.keys():
            print(f"Creating openMINDS-SANDS compatible Brain Atlas Version Instance for {version}...")
            AtlasVersion = AtlasVersionGen(path, version, dic, areas_hierachry)
            AtlasVersion_handler = AutoInitializeAndCall(AtlasVersion)
            AtlasVersion_handler.call_methods((AtlasVersion.generate_instances, AtlasVersion))
            print(f"...Brain Atlas Versions for {version} created")


def instantiation_PEV(path, abbreviation, versions, areas_hierachry):
    for dic in versions:
        for version in dic.keys():
            pev_path = f"{path}{version}/"
            os.mkdir(pev_path)
            print(f"Creating openMINDS-SANDS compatible Parcellation Entity Version Instances for {version}...")
            ParcellationEntityVersion = ParcellationEntityVersionGen(pev_path, version, dic, areas_hierachry,
                                                                     abbreviation, versions)
            ParcellationEntityVersion_handler = AutoInitializeAndCall(ParcellationEntityVersion)
            ParcellationEntityVersion_handler.call_methods(
                (ParcellationEntityVersion.generate_instances, ParcellationEntityVersion))
            print(f"...Parcellation Entity Versions for {version} created")


if __name__ == "__main__":
    # paths
    atlas_path = "/home/kiwitz1/PycharmProjects/openMINDS_SANDS/instances/atlas/brainAtlas/"
    person_dir = "/home/kiwitz1/PycharmProjects/openMINDS_SANDS/instances/person/"
    doi_dir = "/home/kiwitz1/PycharmProjects/openMINDS_SANDS/instances/digitalIdentifier/DOI/"
    orcid_dir = "/home/kiwitz1/PycharmProjects/openMINDS_SANDS/instances/digitalIdentifier/ORCID/"
    version_path = "/home/kiwitz1/PycharmProjects/openMINDS_SANDS/instances/atlas/brainAtlasVersion/"
    entity_path = "/home/kiwitz1/PycharmProjects/openMINDS_SANDS/instances/atlas/parcellationEntity/"
    entity_ver_path = "/home/kiwitz1/PycharmProjects/openMINDS_SANDS/instances/atlas/parcellationEntityVersion/"
    # function call
    main(atlas_path, person_dir, doi_dir, orcid_dir, version_path, entity_path, entity_ver_path)
