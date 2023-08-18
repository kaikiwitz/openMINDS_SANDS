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


def instantiation_BA_PE():
    global Atlas
    Atlas = AtlasGen(atlas_dir, authors, versions, description, shortname, fullname, homepage, documentation,
                     abbreviation, areas_unique, parents_unique)
    Parcellations = ParcellationEntityGen(entity_dir, abbreviation, areas_versions_hierachry, areas_unique,
                                          parents_unique)
    Atlas_handler = AutoInitializeAndCall(Atlas)
    Parcellations_handler = AutoInitializeAndCall(Parcellations)
    Atlas_handler.call_methods((Atlas.generate_instances, Atlas), (Atlas.generate_openminds_instances, Atlas))
    Parcellations_handler.call_methods((Parcellations.generate_instances, Parcellations))


def instantiation_BAV_PEV():
    global version, AtlasVersion, ParcellationEntityVersion
    for dic in versions:
        for version in dic.keys():
            ver_dir = f"{entity_ver_dir}{version}/"
            os.mkdir(ver_dir)
            AtlasVersion = AtlasVersionGen(version_dir, version, dic, areas_versions_hierachry)
            ParcellationEntityVersion = ParcellationEntityVersionGen(ver_dir, version, dic, areas_versions_hierachry,
                                                                     abbreviation, versions)
            AtlasVersion_handler = AutoInitializeAndCall(AtlasVersion)
            ParcellationEntityVersion_handler = AutoInitializeAndCall(ParcellationEntityVersion)
            AtlasVersion_handler.call_methods((AtlasVersion.generate_instances, AtlasVersion),
                                              (AtlasVersion.generate_openminds_instances, AtlasVersion))
            ParcellationEntityVersion_handler.call_methods(
                (ParcellationEntityVersion.generate_instances, ParcellationEntityVersion))


if __name__ == "__main__":

    # instantiate Atlas and PE instances incl methods
    instantiation_BA_PE()

    # instantiate AtlasVersion and PEV instances incl methods
    instantiation_BAV_PEV()
