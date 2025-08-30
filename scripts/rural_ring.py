import geopandas as gpd

def rural_ring(whole_area_shp, urban_area_shp, outpath):
    """
    Create a rural ring shapefile by subtracting the urban area from the whole area.

    Parameters:
    whole_area_shp (str): Path to the shapefile of the whole area.
    urban_area_shp (str): Path to the shapefile of the urban area.
    outpath (str): Directory where the output shapefile will be saved.

    Returns:
    None
    """
    #load two shapefiles
    w_area = gpd.read_file(whole_area_shp) #whole large area
    u_area = gpd.read_file(urban_area_shp) #_urban area

    #make sure same crs
    if u_area.crs != w_area.crs:
        u_area = u_area.to_crs(w_area.crs)
        
    rr_poly = w_area['geometry'].iloc[0].difference(u_area.unary_union) #rural ring polygon

    rr_df = gpd.GeoDataFrame(geometry=[rr_poly], crs=w_area.crs) #make gdf

    #save the shapefile
    rr_df.to_file(outpath / 'rural_ring.shp')
    print('Rural ring shapefile created and saved.')
    


