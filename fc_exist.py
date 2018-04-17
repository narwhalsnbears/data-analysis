## arcpy - This tests if a Feature Class (fc) exists in a given path and returns shapeType

import arcpy

fc = r"C:\Users\mnaro\Documents\ArcGIS\Scratch\clip_hydro.shp" ## Shapefile or FC
## Add new fc with fc_'filename'

## Test if fc exists or not
if arcpy.Exists(fc):
	print("It's there!")
else:
	print("Not there. :( ")

## If FC exists, print FC's shape type.
fc_desc = arcpy.Describe(fc)
print fc_desc.shapeType

if fc.shapeType in ["Polygon", "Polyline", "Point"]:
	print "This feature is a " + fc.shapeType
else:
	print("Does not exist or is not a Feature Class.")
