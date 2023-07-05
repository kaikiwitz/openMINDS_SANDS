import os.path
import glob
import openMINDS.version_manager
import json


class AtlasVersionGen:

    # class variables used for json Instances
    coordinate_space_https = "https://openminds.ebrains.eu/instances/commonCoordinateSpace/"
    accessibility_https = "https://openminds.ebrains.eu/instances/productAccessibility/"
    author_https = "https://openminds.ebrains.eu/instances/person/"
    parcellation_entity_version_https = "https://openminds.ebrains.eu/instances/parcellationEntityVersion/"

    version_https = "https://openminds.ebrains.eu/instances/brainAtlasVersion/"
    authors_list_of_dic = []
    has_entity_listofdic = []
    altVersion_list_of_dic = []
    newVersion_list_of_dic = []
    docu_list_of_dic = []
    # intialize openMinds instance creator
    openMINDS.version_manager.init()
    openMINDS.version_manager.version_selection('v3')
    helper = openMINDS.Helper()
    basic = helper.create_collection()

    def __init__(self, version_dir, version, version_info, areas_hierarchy):
        self.path = version_dir
        self.version = version
        self.version_info = version_info
        self.areas = areas_hierarchy
        self.coordinateSpace = version_info.get(version).get("reference_space")
        self.version_innovation = version_info.get(version).get("version_innovation")
        self.version_identifier = version_info.get(version).get("version_identifier")
        self.release_date = version_info.get(version).get("release_date")
        self.short_name = version_info.get(version).get("short_name")
        self.DOI = version_info.get(version).get("digitalIdentifier")
        self.accessibility = version_info.get(version).get("accessibility")
        self.authors = version_info.get(version).get("authors")
        self.altVersions = version_info.get(version).get("altVersion")
        self.newVersions = version_info.get(version).get("newVersion")

    # THE LOOP NEEDS TO BE DONE OUTSIDE THE CLASS!!!!
    @classmethod
    def getCoordinateSpace(cls, instance):
        coordinate_space_dic = {"@id": f"{cls.coordinate_space_https}{instance.coordinateSpace}"}
        return coordinate_space_dic


    @classmethod
    def accessibility_extract(cls, instance):
        accessibility_dic = {"@id": f"{cls.accessibility_https}{instance.accessibility}"}
        return accessibility_dic

    @classmethod
    def authors_version(cls, instance):
        for author in instance.authors:
            author_dic = {"@id": f"{cls.author_https}{author}"}
            cls.authors_list_of_dic.append(author_dic)

    @classmethod
    def terminology_versions(cls, instance):
        # the following variable defines that we just want the "child" structure, we may improve this in the future for cases where
        # we have version specific parent structures
        version_entities = (t[0] for t in instance.areas[instance.version])
        for area in version_entities:
            entity_version_dic = {"@id": f"{cls.parcellation_entity_version_https}{instance.version}_{area}"}
            cls.has_entity_listofdic.append(entity_version_dic)
        terminology_dic = {"@type": "https://openminds.ebrains.eu/sands/ParcellationTerminologyVersion",
                           "definedIn": None, "hasEntity": cls.has_entity_listofdic}
        return terminology_dic

    @classmethod
    def alternativeVersions(cls, instance):
        if instance.altVersions is not None:
            for altVersion in instance.altVersions:
                altVersion_dic = {"@id": f"{cls.version_https}{altVersion}"}
                cls.altVersion_list_of_dic.append(altVersion_dic)

    @classmethod
    def newerVersion(cls, instance):
        if instance.newVersions is not None:
            for newVersion in instance.newVersions:
                newVersion_dic = {"@id": f"{cls.version_https}{newVersion}"}
                cls.newVersion_list_of_dic.append(newVersion_dic)

    @classmethod
    def docugen(cls, instance):
        docu = {"@id": f"{instance.DOI}"}
        cls.docu_list.append(docu)






