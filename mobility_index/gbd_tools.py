def pandas2geopandas(df):
    # a function to convert a pandas data frame to geopandas data frame
    geometries = [shapely.geometry.Point(xy) for xy in zip(df.lng, df.lat)]
    crs = {'init': 'epsg:4326'}
    gf = gpd.GeoDataFrame(df, crs=crs, geometry=geometries)
    return(gf)