import os.path
from Atlas_data import MarsAtlas, DKTAtlas
from class_utils import AutoInitializeAndCall
from Atlas import AtlasGen
from AtlasVersion import AtlasVersionGen
from ParcellationEntity import ParcellationEntityGen
from ParcellationEntityVersion import ParcellationEntityVersionGen


def main(BA_path, BAV_path, PE_path, PEV_path):
    atlases = [MarsAtlas, DKTAtlas]
    for atlas in atlases:
        # get Mars Atlas data
        data_atlas = atlas()
        authors, documentation, description, abbreviation, fullname, shortname, \
            homepage, versions, areas_versions_hierachry, areas_unique, parents_unique = data_atlas.get_data()
        instantiation_BA(BA_path, authors, versions, description, shortname, fullname, homepage, documentation,
                         abbreviation, areas_unique, parents_unique)
        instantiation_PE(PE_path, abbreviation, areas_versions_hierachry, areas_unique, parents_unique)
        instantiation_BAV(BAV_path, versions, areas_versions_hierachry)
        instantiation_PEV(PEV_path, abbreviation, versions, areas_versions_hierachry)


def instantiation_BA(path, authors, versions, description, shortname, fullname, homepage, documentation,
                     abbreviation, areas, parents):
    # global Atlas
    print(f"Creating openMINDS-SANDS compatible Atlas Instance for {abbreviation}...")
    path = f"{path}{fullname}.jsonld"
    Atlas = AtlasGen(path, authors, versions, description, shortname, fullname, homepage, documentation,
                     abbreviation, areas, parents)
    Atlas_handler = AutoInitializeAndCall(Atlas)
    Atlas_handler.call_methods((Atlas.generate_instances, Atlas))
    print(f"...Atlas Instance for {abbreviation} created")


def instantiation_PE(path, abbreviation, areas_hierachry, areas, parents):
    # global Parcellations
    path = f"{path}{abbreviation}/"
    os.mkdir(path)
    print(f"Creating openMINDS-SANDS compatible Parcellation Entitiy Instances for {abbreviation}...")
    Parcellations = ParcellationEntityGen(path, abbreviation, areas_hierachry, areas, parents)
    Parcellations_handler = AutoInitializeAndCall(Parcellations)
    Parcellations_handler.call_methods((Parcellations.generate_instances, Parcellations))
    print(f"...Parcellation Entities for {abbreviation} created")

def instantiation_BAV(path, versions, areas_hierachry):
    # global version, AtlasVersion
    # global AtlasVersion
    for dic in versions:
        for version in dic.keys():
            print(f"Creating openMINDS-SANDS compatible Brain Atlas Version Instance for {version}...")
            AtlasVersion = AtlasVersionGen(path, version, dic, areas_hierachry)
            AtlasVersion_handler = AutoInitializeAndCall(AtlasVersion)
            AtlasVersion_handler.call_methods((AtlasVersion.generate_instances, AtlasVersion))
            print(f"...Brain Atlas Versions for {version} created")


def instantiation_PEV(path, abbreviation, versions, areas_hierachry):
    # global version, ParcellationEntityVersion
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

    # atlas paths
    atlas_path = "/home/kiwitz1/PycharmProjects/openMINDS_SANDS/instances/atlas/brainAtlas/"
    version_path = "/home/kiwitz1/PycharmProjects/openMINDS_SANDS/instances/atlas/brainAtlasVersion/"
    entity_path = "/home/kiwitz1/PycharmProjects/openMINDS_SANDS/instances/atlas/parcellationEntity/"
    entity_ver_path = "/home/kiwitz1/PycharmProjects/openMINDS_SANDS/instances/atlas/parcellationEntityVersion/"
    # function call
    main(atlas_path, version_path, entity_path, entity_ver_path)
