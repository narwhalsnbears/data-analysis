## arcpy - Geodatabase environment

import arcpy

arcpy.env.workspace = r'C:\Users\mnaro\Documents\Work\ArcGIS\Workspace'
arcpy.CreatePersonalGDB_management(arcpy.env.workspace, "Test")

my_geodatabase = arcpy.ListWorkspaces("Test*")[0]
my_geodatabase

## Create random points
arcpy.CreateRandomPoints_management(my_geodatabase, "RanPoints")
arcpy.CreateFeatureclass_management(my_geodatabase, "SqBuffs")
