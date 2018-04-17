## arcpy and os workspace parameters
## Comment-out/Delete unused method if not using both

import arcpy
import os

## Scratch folder for analysis processing
arcpy.env.workspace = r"C:\Users\mnaro\Documents\ArcGIS\Scratch"
arcpy.env.overwriteOutput = True

## os workspace, join paths for assignment
data_folder = r"C:\Users\mnaro\Documents\ArcGIS"
data_workspace = os.path.join(data_folder, "Arc Scratch")
jeffco_hydro = os.path.join(data_workspace, "clip_hydro.prj")

# Assign appropriate fc or shapefile, return filename w/o extension
fc = "test_fc.shp"
path = os.path.splitext(fc)
basename = path[0]
extension = path[-1]
print basename
