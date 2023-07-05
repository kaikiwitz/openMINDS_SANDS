import Mars_data_structures
from Atlas import AtlasGen

# get the Mars Atlas data
authors, documentation, description, abbreviation, fullname, shortname, \
    homepage, versions, areas_versions_hierachry, areas_unique, parents_unique = Mars_data_structures.data_structures()


# create the atlas dir
# atlas dir
j = ".jsonld"
atlas_dir = f"/home/kiwitz1/PycharmProjects/openMINDS_SANDS/instances/atlas/brainAtlas/{fullname}{j}"

# create the Atlas Instance and call all Atlas methods

Mars = AtlasGen(atlas_dir, authors, versions, description, shortname, fullname, homepage, documentation, abbreviation,
             areas_unique, parents_unique)
AtlasGen.author_gen(Mars)
AtlasGen.terminology_gen(Mars)
AtlasGen.version_gen(Mars)
AtlasGen.generate_instances(Mars)
AtlasGen.generate_openminds_instances(Mars)


