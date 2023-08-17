import os.path
import Mars_data_structures
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
for dic in versions:
    for version in dic.keys():
        os.mkdir(f"{entity_ver_dir}{version}/")


# create the Atlas
Mars = AtlasGen(atlas_dir, authors, versions, description, shortname, fullname, homepage, documentation, abbreviation,
             areas_unique, parents_unique)
AtlasGen.generate_instances(Mars)
AtlasGen.generate_openminds_instances(Mars)

# create Atlas Versions
for dic in versions:
    for version in dic.keys():
        MarsVersion = AtlasVersionGen(version_dir, version, dic, areas_versions_hierachry)
        AtlasVersionGen.generate_instances(MarsVersion)
        AtlasVersionGen.generate_openminds_instances(MarsVersion)

# create Atlas Parcellations
Parcellation_Entitites = ParcellationEntityGen(entity_dir, abbreviation, areas_versions_hierachry,areas_unique, parents_unique)
ParcellationEntityGen.generate_instances(Parcellation_Entitites)

# create Atlas Parcellation Versions
# WE SHOULD LOOP OVER THE PARCELLATION VERSION INFO JUST LIKE WE DID FOR THE ATLAS VERSIONS, DEFINE INSTANCE VARIABLES ACCORDINGLY, WAY EASIER
ParcellationEntityVersions = ParcellationEntityVersionGen(entity_ver_dir, areas_versions_hierachry, versions)
generate_entity_versions(entity_ver_dir, areas_versions_hierachry, versions)

