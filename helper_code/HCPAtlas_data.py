
def data_structures():
    # Brain Area Info for each version (can be the same) THIS NEEDS TO BE SAME LENGTH FOR ALL AREAS
    areas_children = ['caudalAnteriorCingulate', 'caudalMiddleFrontal', 'cuneus', 'entorhinal', 'fusiform',
                      'inferiorParietal', 'inferiorTemporal', 'isthmusCingulate', 'lateralOccipital',
                      'lateralOrbitofrontal', 'lingual', 'medialOrbitofrontal', 'middleTemporal', 'parahippocampal',
                      'paracentral', 'parsOpercularis', 'parsOrbitalis', 'parsTriangularis', 'pericalcarine',
                      'postcentral', 'posteriorCingulate', 'precentral', 'precuneus', 'rostralAnteriorCingulate',
                      'rostralMiddleFrontal', 'superiorFrontal', 'superiorParietal', 'superiorTemporal',
                      'supramarginal', 'transverseTemporal', 'insula']
    areas_1st_parent = ['cingulateCortex', 'frontalLobe', 'occipitalLobe', 'medialTemporalLobe', 'medialTemporalLobe',
                        'parietalLobe', 'lateralTemporalLobe', 'cingulateCortex', 'occipitalLobe', 'frontalLobe',
                        'occipitalLobe', 'frontalLobe', 'lateralTemporalLobe', 'medialTemporalLobe', 'frontalLobe',
                        "frontalLobe", 'frontalLobe', 'frontalLobe', 'occipitalLobe', 'parietalLobe', 'cingulateCortex',
                        "frontalLobe", 'parietalLobe', 'cingulateCortex', 'frontalLobe', 'frontalLobe', 'parietalLobe',
                        'lateralTemporalLobe', 'parietalLobe', 'lateralTemporalLobe', None]
    # areas = {outer_key: {outer_value: areas_2ndParent[0]} for outer_key, outer_value in areas_parent_matched.items()}
    areas_2nd_parent = ['brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain',
                        'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain',
                        "brain", 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', 'brain', None]

    # zip list to store as tuples
    areas = list(zip(areas_children, areas_1st_parent, areas_2nd_parent))

    # atlas info
    DKT_authors = [{"glasserMatthew" : {"familyName" : "Glasser", "givenName" : "Matthew", "ORCID" : None}},
                   {"coalsonTimothy" : {"familyName" : "Coalson", "givenName" : "Timothy", "ORCID" : "https://orcid.org/0000-0002-2105-7896"}},
                   {"robinsonEmma" : {"familyName" : "Robinson", "givenName" : "Emma", "ORCID" : "https://orcid.org/0000-0002-7886-3426"}},
                   {"hackerCarl" : {"familyName" : "Hacker", "givenName" : "Carl", "ORCID" : None}},
                   {"harwellJohn" : {"familyName" : "Harwell", "givenName" : "John", "ORCID" : None}},
                   {"yacoubEssa" : {"familyName" : "Essa", "givenName" : "Yacoub", "ORCID" : None}},
                   {"ugurbilKamil" : {"familyName" : "Kamil", "givenName" : "Ugurbil", "ORCID" : None}},
                   {"anderssonJesper" : {"familyName" : "Andersson", "givenName" : "Jesper", "ORCID" : None}},
                   {"beckmannChristian" : {"familyName" : "Beckmann", "givenName" : "Christian", "ORCID" : "https://orcid.org/0000-0002-3373-3193"}},
                   {"jenkinsonMark" : {"familyName" : "Jenkinson", "givenName" : "Mark", "ORCID" : "https://orcid.org/0000-0001-6043-0166"}},
                   {"smithStephen" : {"familyName" : "Smith", "givenName" : "Stephen", "ORCID" : "https://orcid.org/0000-0001-8166-069X"}},
                   {"vanEssenDavid" : {"familyName" : "van Essen", "givenName" : "David", "ORCID" : "https://orcid.org/0000-0001-7044-4721"}}]
    authors_simple = [key for dic in DKT_authors for key in dic.keys()]

    full_documentation =  [{"DKT": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4990127/"}]
    main_documentation = "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4990127/"
    description = "Glasser's  multi-modal parcellation of the human cerebral cortex"
    abbreviation = "HCP-MMP1"
    fullName = "Human Connectome Project Multi-modal Cortical Parcellation "
    shortName = "HCP-MMP1"
    homepage = "https://balsa.wustl.edu/study/RVVG"

    # Data Structures for all VERSIONS (BAVs, PEVs)
    # version info
    versions = [{"HCP-MMP1-MNI152": {"reference_space": "MNI_ICBM_152_2009c_nonlin_asym",
                                      "accessibility": "freeAccess", "atlasType": "parcellationScheme", "version_identifier": "180 areas, MNI",
                                      "version_innovation": "Volume atlas version of the Glasser atlas",
                                      "release_date": "2016-07-21", "short_name": "HCP-MMP1", "homepage": "https://neurovault.org/collections/1549/",
                                      "license": "ccBy4.0", "digitalIdentifier": "https://doi.org/10.1038/nature18933",
                                      "full_doc_name": "HCP-MMP1-MNI152", "authors": authors_simple, "altVersion": ["HCP-MMP1-fsaverage"],
                                      "criteriaQualityType": ["processive"], "annotationCriteriaType": ["deterministicAnnotation"],
                                      "laterality": ["left", "right"], "annotationType": "annotationMask"}},
                {"HCP-MMP1-fsaverage": {"reference_space" : "fsaverage-5",
                                             "accessibility": "freeAccess", "atlasType": "parcellationScheme", "version_identifier": "180 areas, fsaverage",
                                             "version_innovation": "Cortical surface atlas version of the Glasser atlas",
                                             "release_date": "2016-07-25", "short_name": "HCP-MMP1", "homepage": "https://figshare.com/articles/dataset/HCP-MMP1_0_projected_on_fsaverage/3498446",
                                             "license":"ccBy4.0", "digitalIdentifier": "https://doi.org/10.1038/nature18933",
                                             "full_doc_name": "HCP-MMP1-fsaverage", "authors": authors_simple, "altVersion": ["HCP-MMP1-MNI152"],
                                             "criteriaQualityType": ["processive"], "annotationCriteriaType": ["deterministicAnnotation"],
                                             "laterality": ["left", "right"], "annotationType": "annotationSurface"}}
                ]

    # area for each version for BAVs and PE
    areas_versions_hierachry = {"HCP-MMP1-MNI152": areas, "HCP-MMP1-fsaverage": areas}

    # unique areas for BA
    areas_unique = set()
    for value_list in areas_versions_hierachry.values():
        for tuple_value in value_list:
            first_entry = tuple_value[0]
            areas_unique.add(first_entry)

    # unique parents
    parents_unique = set()
    for value_list in areas_versions_hierachry.values():
        for tuple_value in value_list:
            parents_unique.update(tuple_value[1:])

    return (DKT_authors, full_documentation, main_documentation, description, abbreviation, fullName, shortName, homepage, versions, areas_versions_hierachry, areas_unique, parents_unique)


if __name__ == '__main__':
    DKT_authors, full_documentation, main_documentation, description, abbreviation, fullName, shortName, homepage, versions, areas_versions_hierachry, areas_unique, parents_unique = data_structures()