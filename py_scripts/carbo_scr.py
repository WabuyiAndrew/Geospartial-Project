import arcpy
... from arcpy.sa import *
... import os
... import pandas as pd
... import math
... 
... # Enable Spatial Analyst
... arcpy.CheckOutExtension("Spatial")
... 
... # Workspace
... workspace = r"C:\Users\Andy\Desktop\musu"
... arcpy.env.workspace = workspace
... arcpy.env.overwriteOutput = True
... 
... # Input bands (Sentinel-2 assumed)
... B2 = os.path.join(workspace, "B2.tif")   # Blue
... B4 = os.path.join(workspace, "B4.tif")   # Red
... B5 = os.path.join(workspace, "B5.tif")   # Red Edge
... B8 = os.path.join(workspace, "B8.tif")   # NIR
... B11 = os.path.join(workspace, "B11.tif") # SWIR1
... AOI = os.path.join(workspace, "musubi.shp")  # Shapefile for zonal stats
... 
... # Step 1 – Scale reflectance (Sentinel-2 is 0–10000)
... B2f = Raster(B2) / 10000.0
... B4f = Raster(B4) / 10000.0
... B5f = Raster(B5) / 10000.0
... B8f = Raster(B8) / 10000.0
... B11f = Raster(B11) / 10000.0
... 
... # Step 2 – Vegetation Indices
... NDVI = (B8f - B4f) / (B8f + B4f)
... NDVI_path = os.path.join(workspace, "NDVI.tif")
... NDVI.save(NDVI_path)
... 
... NDRE = (B8f - B5f) / (B8f + B5f)
... NDRE_path = os.path.join(workspace, "NDRE.tif")
... NDRE.save(NDRE_path)
... 
... NDMI = (B8f - B11f) / (B8f + B11f)
... NDMI_path = os.path.join(workspace, "NDMI.tif")
... NDMI.save(NDMI_path)
... 
... # LAI estimation from NDVI (empirical formula from literature)
... LAI = (3.618 * NDVI) - 0.118
... LAI_path = os.path.join(workspace, "LAI.tif")
... LAI.save(LAI_path)
... 
... # Step 3 – Carbon Stock Models (literature-inspired, placeholder coefficients)
... # ⚠️ Replace coefficients with calibrated values if you have field data
... 
... # NDMI – exponential model
... C_NDMI = 15.7 * Exp(0.85 * NDMI)   # Inspired by stand volume studies
... C_NDMI_path = os.path.join(workspace, "C_NDMI.tif")
... C_NDMI.save(C_NDMI_path)
... 
... # NDRE – polynomial model (example form)
... C_NDRE = 5.7 * (NDRE ** 2) + 2.3 * NDRE + 8.1
... C_NDRE_path = os.path.join(workspace, "C_NDRE.tif")
... C_NDRE.save(C_NDRE_path)
... 
... # LAI – linear model
... C_LAI = 0.45 * LAI + 12.3
... C_LAI_path = os.path.join(workspace, "C_LAI.tif")
... C_LAI.save(C_LAI_path)
... 
... # Step 4 – Zonal Statistics for AOI
... results = {}
... 
... for raster in [C_NDMI_path, C_NDRE_path, C_LAI_path]:
...     out_table_name = os.path.basename(raster).replace(".tif", "_stats.dbf")
...     out_table_path = os.path.join(workspace, out_table_name)
... 
...     arcpy.sa.ZonalStatisticsAsTable(AOI, "FID", raster, out_table_path, "DATA", "ALL")
...     print("✅ Stats table created:", out_table_name)
... 
...     # Convert .dbf to pandas DataFrame
...     df = pd.DataFrame(arcpy.da.TableToNumPyArray(out_table_path, "*"))
...     results[os.path.basename(raster).replace(".tif", "")] = df
... 
... # Step 5 – Export all results to Excel
... excel_path = os.path.join(workspace, "CarbonResults_AGC.xlsx")
... with pd.ExcelWriter(excel_path) as writer:
...     for name, df in results.items():
...         df.to_excel(writer, sheet_name=name, index=False)
... 
... print("🎯 Done! Results exported to:", excel_path)
