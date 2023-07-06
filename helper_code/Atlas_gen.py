import Mars_data_structures
from Atlas import AtlasGen
from AtlasVersion import AtlasVersionGen

# get the Mars Atlas data
authors, documentation, description, abbreviation, fullname, shortname, \
    homepage, versions, areas_versions_hierachry, areas_unique, parents_unique = Mars_data_structures.data_structures()


# create the atlas dir
# atlas dir
j = ".jsonld"
atlas_dir = f"/home/kiwitz1/PycharmProjects/openMINDS_SANDS/instances/atlas/brainAtlas/{fullname}{j}"
version_dir = "/home/kiwitz1/PycharmProjects/openMINDS_SANDS/instances/atlas/brainAtlasVersion/"
entity_dir = f"/home/kiwitz1/PycharmProjects/openMINDS_SANDS/instances/atlas/parcellationEntity/{abbreviation}/"
os.mkdir(entity_dir)

# create the Atlas Instance and call all Atlas methods
Mars = AtlasGen(atlas_dir, authors, versions, description, shortname, fullname, homepage, documentation, abbreviation,
             areas_unique, parents_unique)
AtlasGen.generate_instances(Mars)
AtlasGen.generate_openminds_instances(Mars)

# create atlas versions and call altlas versions methods
for dic in versions:
    for version in dic.keys():
        MarsVersion = AtlasVersionGen(version_dir, version, dic, areas_versions_hierachry)
        AtlasVersionGen.generate_instances(MarsVersion)
        AtlasVersionGen.generate_openminds_instances(MarsVersion)

# entitties





