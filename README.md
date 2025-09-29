# Geospatial Project: Sentinel-2 Satellite Imagery Analysis for Vegetation & Soil Health Mapping 🛰️

This project implements a complete workflow for **Geographic Information Systems (GIS) mapping** and **satellite remote sensing analysis**. Using **Sentinel-2** data, the objective was to assess vegetation health, soil moisture, and crop stress within a defined Area of Interest (AOI).

The repository documents the data acquisition, processing, and visualization methodology, including the Python scripts used for automation and analysis.

---

## 💻 Technical Stack & Key Technologies

| Category | Tools & Technologies Used |
| :--- | :--- |
| **GIS Software** | ArcMap (Primary Processing), ArcGIS Pro (Alternative), QGIS (FOSS) |
| **Satellite Data** | Sentinel-2 (ESA Copernicus L2A), Landsat, GeoJSON, Shapefile |
| **Data Acquisition** | Copernicus Open Access Hub (SciHub) |
| **Scripting & Automation** | Python (for post-processing, statistics, and automation of repetitive tasks) |
| **File Formats** | .SAFE (Sentinel-2), .shp (Shapefile), .geojson, .dbf (dBASE) |

---

## ✨ Project Highlights & Key Deliverables

* **Geospatial Data Handling:** Demonstrated proficiency in converting vector data ($\text{GeoJSON} \rightarrow \text{Shapefile}$), handling large **.SAFE** raster files, and managing projections.
* **Spectral Index Derivation:** Successfully calculated and mapped multiple critical indices using **Raster Calculator**. The key formulas used are:
    * **Normalized Difference Vegetation Index ($\text{NDVI}$):** $(\text{B8} - \text{B4}) / (\text{B8} + \text{B4})$
    * **Normalized Difference Moisture Index ($\text{NDMI}$):** $(\text{B8} - \text{B11}) / (\text{B8} + \text{B11})$
    * **Normalized Difference Red Edge ($\text{NDRE}$):** $(\text{B8A} - \text{B4}) / (\text{B8A} + \text{B4})$
* **Thematic Mapping & Analysis:** Performed **raster reclassification** and **raster-to-polygon conversion** for thematic visualization and statistical area ($\text{ha}$) calculation using Excel ($\text{Pivot Tables}$).
* **Python Integration:** Included a Python script to **[DESCRIBE WHAT THE SCRIPT DOES: e.g., automate batch processing of shapefiles or calculate final statistics]**.

---

## 📈 Detailed Workflow: Data Processing Steps

This section outlines the primary steps executed during the internship using **ArcMap** and external tools, with images illustrating the process.

### 1. Data Acquisition & Preparation

1.  **AOI Definition:** Obtained $\text{GeoJSON}$ boundary and converted it to $\text{Shapefile}$ ($\text{.shp}$) format.
    `![Figure 3: GeoJSON Data on geojson.io](images/figure_3_geojson_aoi.png)`
    `![Figure 4: Conversion of GeoJSON into Shapefile](images/figure_4_geojson_to_shp.png)`
2.  **Imagery Search:** Used the **Copernicus Open Access Hub** to filter and download **Sentinel-2 L2A** products, ensuring low cloud cover and a specific time range.
    `![Figure 5: Uploading AOI to Copernicus](images/figure_5_uploading_aoi.png)`
    `![Figure 7: Selecting the appropriate range of time](images/figure_7_time_range.png)`
3.  **Band Selection:** Selected and harmonized 10m resolution bands ($\text{B2, B3, B4, B8}$) and resampled 20m bands ($\text{B8A, B11}$) to a consistent 10m resolution.

### 2. GIS Processing & Analysis (ArcMap)

1.  **Data Clipping:** Applied the $\text{AOI Shapefile}$ to clip the raw Sentinel-2 imagery.
    `![Figure 8: Shapefile added as a layer in ArcMap](images/figure_8_shapefile_in_arcmap.png)`
2.  **Index Calculation:** Ran the **Raster Calculator** to generate the $\text{NDVI}$, $\text{NDMI}$, and $\text{NDRE}$ raster layers.
3.  **Classification & Visualization:** **Reclassified** the index layers into meaningful classes and applied relevant **color ramps** for intuitive display.
    `![Figure 9: NDVI raster layer](images/NDVI.png)` **<-- Using your specified file name**
4.  **Statistical Analysis:** Converted the final classified raster maps to $\text{Polygon Shapefiles}$ to enable area calculation (in hectares) using $\text{Geometry Calculation}$ and exporting statistics to Excel.
    `![Figure 10: Area of Classes statistical summary in Excel](images/figure_10_area_in_excel.png)`

### 3. Final Output & Documentation

1.  **Map Layout:** Designed **map layouts** (including title, legend, scale, north arrow) and exported high-quality $\text{PNG/JPEG}$ maps for reporting.
    `![Figure 11: Final NDVI map in Layout View](images/figure_11_ndvi_map_layout.png)`
    `![Figure 12: Final Exported NDVI Map](images/NDVI.jpg)`

---

## 📚 Learning & Conclusion

As a Computer Engineer, this project was a valuable introduction to the complexities of **geospatial data** and remote sensing principles. The primary challenges involved managing large data volumes, overcoming **cloud cover challenges**, and mastering the specialized $\text{GIS}$ environment.