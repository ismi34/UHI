import rasterio
import numpy as np 

def celcius(input_raster, outpath, scale_factor, add_offset):
    with rasterio.open(input_raster) as src:
        array = src.read(1)
        meta = src.meta.copy()
        nodata = src.nodata
        
        if nodata is not None:
            n_array = np.where(array==nodata, np.nan, array)
        else:
            n_array = array
        
            
        n_array = np.round(((n_array * scale_factor + add_offset) - 273.15), 2)  # Apply scaling and offset
        
        meta.update({
            'dtype': 'float32',   
        })
        
        name_str = input("Give a file name: > ")
        out_file = outpath / f"{name_str}.tif"
        
        with rasterio.open(out_file, "w", **meta) as dest:
            dest.write(n_array, 1)
    print(f"Saved the converted raster to: {out_file}")
    
    
def kalvin(input_raster, outpath, scale_factor, add_offset):
    with rasterio.open(input_raster) as src:
        array = src.read()
        meta = src.meta.copy()
        nodata = src.nodata
        
        if nodata is not None:
            n_array = np.where(array==nodata, np.nan, array)
        else:
            n_array = array
        
            
        n_array = np.round((n_array * scale_factor + add_offset), 2)  # Apply scaling and offset
        
        meta.update({
            'dtype': 'float32',   
        })
        
        name_str = input("Give a file name: > ")
        out_file = outpath / f"{name_str}.tif"
        
        with rasterio.open(out_file, "w", **meta) as dest:
            dest.write(n_array, 1)
    print(f"Saved the converted raster to: {out_file}")