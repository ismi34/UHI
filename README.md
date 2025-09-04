Urban Heat Island Analysis in Saidpur, Bangladesh

🌍 Introduction

The Urban Heat Island (UHI) effect occurs when urban areas record higher surface temperatures than their surrounding rural or less-urbanized regions. This temperature difference is primarily driven by:

Low surface albedo (darker built surfaces absorb more heat)

Reduced evapotranspiration (less vegetation and open soil)

Anthropogenic heat generation (traffic, industry, energy use)

Understanding and identifying UHI hotspots is essential for:

Urban heat management

Sustainable city planning

Public health and well-being

📍 Study Area

This project explores UHI in Saidpur, a sub-district of Bangladesh. The goal was to examine whether Saidpur experiences measurable UHI effects using Landsat Surface Temperature (ST) imagery.

⚙️ Methodology

I developed a Python-based processing pipeline to analyze Landsat ST data:

Vector preparation → creating urban and rural masks.

Raster masking → clipping Landsat imagery to the defined regions.

Cloud masking → using the QA_PIXEL band to filter out cloud-contaminated pixels.

DN conversion → transforming digital numbers into surface temperature (°C).

Visualization → generating maps, histograms, and bar charts to compare urban vs rural temperature.

All scripts were run in a Jupyter Notebook, which also served for visualization and documentation.

📊 Results

On average, urban Saidpur recorded surface temperatures about +5 °C higher than its rural surroundings.

Temperature distribution:

Urban center: most areas between 34–38 °C

Rural ring: most areas between 28–32 °C

The results clearly highlight a distinct UHI effect in Saidpur.


The "scripts" folder contains:
1. mask_raster.py which is a custom function that mask a raster tile to the extend of a given area of interest
2. rural_ring.py which is a custom function that trim the city center from the study area to create a rural ring vector
3. mak_clod.py which is a custom function that filter out the cell from calculation that are overshadowed by cloud and shadow. It uses Landsat QA_PIXEL band as cell quality reference
4. dn_to_unit.py which is a custom function that converts the Landsat ST B10 raster's digital number to a readable physical unit value, in this case-degree celcius.
5. main.ipynb is the main notebook where all the above mentioned functions were executed
uhi.qgz is the QGIS project where the results were turned into maps
The "result" folder holds the visual results of the analysis 
