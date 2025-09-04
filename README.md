The "scripts" folder contains:
1. mask_raster.py which is a custom function that mask a raster tile to the extend of a given area of interest
2. rural_ring.py which is a custom function that trim the city center from the study area to create a rural ring vector
3. mak_clod.py which is a custom function that filter out the cell from calculation that are overshadowed by cloud and shadow. It uses Landsat QA_PIXEL band as cell quality reference
4. dn_to_unit.py which is a custom function that converts the Landsat ST B10 raster's digital number to a readable physical unit value, in this case-degree celcius.
5. main.ipynb is the main notebook where all the above mentioned functions were executed
uhi.qgz is the QGIS project where the results were turned into maps
The "result" folder holds the visual results of the analysis 
