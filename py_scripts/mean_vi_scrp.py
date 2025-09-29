import arcpy
... from arcpy.sa import *
... import os
... import pandas as pd
... 
... # Enable Spatial Analyst
... arcpy.CheckOutExtension("Spatial")
... 
... # ---------------- USER SETTINGS ----------------
... workspace = r"C:\Users\Andy\Desktop\musu"
... arcpy.env.workspace = workspace
... arcpy.env.overwriteOutput = True
... 
... # Input AOI shapefile
... AOI = os.path.join(workspace, "musubi.shp")
... zone_field = "name"
... output_excel = os.path.join(workspace, "MeanIndexResults.xlsx")
... 
... # List of pre-calculated index raster file paths
... index_rasters = {
...     "NDVI": os.path.join(workspace, "NDVI.tif"),
...     "NDRE": os.path.join(workspace, "NDRE.tif"),
...     "NDMI": os.path.join(workspace, "NDMI.tif"),
...     "LAI": os.path.join(workspace, "LAI.tif")
... }
... 
... # ---------------- STEP 1: Zonal Statistics & Export ----------------
... print("Calculating mean index values for each polygon...")
... index_values_df = None
... 
... # Loop through each pre-calculated index raster
... for name, raster_path in index_rasters.items():
...     out_table_name = "{}_stats.dbf".format(name)
...     out_table_path = os.path.join(workspace, out_table_name)
...     
...     # Perform Zonal Statistics to get the MEAN value
...     arcpy.sa.ZonalStatisticsAsTable(AOI, zone_field, raster_path, out_table_path, "DATA", "MEAN")
...     print("✅ Stats table created for {}: {}".format(name, out_table_name))
...     
...     # Convert .dbf to pandas DataFrame and merge
...     arr = arcpy.da.TableToNumPyArray(out_table_path, [zone_field, "MEAN"])
...     df = pd.DataFrame(arr).rename(columns={zone_field: "name", "MEAN": name})
...     
...     if index_values_df is None:
...         index_values_df = df
...     else:
...         index_values_df = index_values_df.merge(df, on="name")
... 
... # ---------------- STEP 2: Export to Excel ----------------
... print("Exporting results to Excel...")
... 
... with pd.ExcelWriter(output_excel) as writer:
...     index_values_df.to_excel(writer, sheet_name="Mean_Index_Values", index=False)
... 
... print("🎯 Done! Results exported to:", output_excel