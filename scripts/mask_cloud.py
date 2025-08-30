import rasterio 
import numpy as np 
from pathlib import Path


def mask_cloud(raster, qa_raster, outpath):
    """_summary_

    Args:
        raster (_path object_): _to the raster to be masked_
        qa_raster (_path object_): _the QA_PIX raster that gives quality value_
        outpath (_path object_): _where to save the new masked raster _
    """
    #bit flags for cloud and cloud shadow
    cloud = 1 << 3
    shadow = 1 << 4
    
    #read qa_raster as create mask
    with rasterio.open(qa_raster) as qa_src:
        qa_arr = qa_src.read(1)
    bad = qa_arr & (cloud | shadow) != 0
    
    #read the input raster and apply the mask
    with rasterio.open(raster) as src:
        arr = src.read(1)
        meta = src.meta.copy()
        nodata = src.nodata if src.nodata is not None else 0
        meta.update(nodata=nodata)
    out_arr = arr.copy()
    out_arr[bad] = nodata
    
    #save the masked raster
    name_str = input("Give a file name: > ")
    out_file = outpath / f"{name_str}.tif"
    with rasterio.open(out_file, "w", **meta) as dest:
        dest.write(out_arr, 1)
    print(f"Saved the masked raster to: {out_file}")
        
        