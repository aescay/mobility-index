def convex_hull_shape(gf):
    point_collection = shapely.geometry.MultiPoint(gf.geometry.tolist())
    polygon = point_collection.convex_hull
    gfShape = gpd.GeoDataFrame(geometry=[polygon], crs = {'init': 'epsg:4326'})
    return(gfShape)