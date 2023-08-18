import os.path
import Mars_data_structures
from class_utils import AutoInitializeAndCall
from Atlas import AtlasGen
from AtlasVersion import AtlasVersionGen
from ParcellationEntity import ParcellationEntityGen
from ParcellationEntityVersion import ParcellationEntityVersionGen

# get Mars Atlas data
authors, documentation, description, abbreviation, fullname, shortname, \
    homepage, versions, areas_versions_hierachry, areas_unique, parents_unique = Mars_data_structures.data_structures()

# atlas dirs
j = ".jsonld"
atlas_dir = f"/home/kiwitz1/PycharmProjects/openMINDS_SANDS/instances/atlas/brainAtlas/{fullname}{j}"
version_dir = "/home/kiwitz1/PycharmProjects/openMINDS_SANDS/instances/atlas/brainAtlasVersion/"
entity_dir = f"/home/kiwitz1/PycharmProjects/openMINDS_SANDS/instances/atlas/parcellationEntity/{abbreviation}/"
os.mkdir(entity_dir)
entity_ver_dir = "/home/kiwitz1/PycharmProjects/openMINDS_SANDS/instances/atlas/parcellationEntityVersion/"


def instantiation_BA():
    global Atlas
    Atlas = AtlasGen(atlas_dir, authors, versions, description, shortname, fullname, homepage, documentation,
                     abbreviation, areas_unique, parents_unique)
    Atlas_handler = AutoInitializeAndCall(Atlas)
    Atlas_handler.call_methods((Atlas.generate_instances, Atlas), (Atlas.generate_openminds_instances, Atlas))


def instantiation_PE():
    global Parcellations
    Parcellations = ParcellationEntityGen(entity_dir, abbreviation, areas_versions_hierachry, areas_unique,
                                          parents_unique)
    Parcellations_handler = AutoInitializeAndCall(Parcellations)
    Parcellations_handler.call_methods((Parcellations.generate_instances, Parcellations))


def instantiation_BAV():
    global version, AtlasVersion
    for dic in versions:
        for version in dic.keys():
            AtlasVersion = AtlasVersionGen(version_dir, version, dic, areas_versions_hierachry)

            AtlasVersion_handler = AutoInitializeAndCall(AtlasVersion)
            AtlasVersion_handler.call_methods((AtlasVersion.generate_instances, AtlasVersion),
                                              (AtlasVersion.generate_openminds_instances, AtlasVersion))


def instantiation_PEV():
    global version, ParcellationEntityVersion
    for dic in versions:
        for version in dic.keys():
            ver_dir = f"{entity_ver_dir}{version}/"
            os.mkdir(ver_dir)
            ParcellationEntityVersion = ParcellationEntityVersionGen(ver_dir, version, dic, areas_versions_hierachry,
                                                                     abbreviation, versions)
            ParcellationEntityVersion_handler = AutoInitializeAndCall(ParcellationEntityVersion)
            ParcellationEntityVersion_handler.call_methods(
                (ParcellationEntityVersion.generate_instances, ParcellationEntityVersion))


if __name__ == "__main__":
    # instantiate Atlas instances
    instantiation_BA()
    instantiation_PE()
    instantiation_BAV()
    instantiation_PEV()
