import geopandas as gpd

gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'

# Read in the list of shapefiles in the directory


# Read the KML file into a GeoDataFrame
kml_file = "example.kml"
gdf = gpd.read_file(kml_file, driver='KML')

# Write the GeoDataFrame to a shapefile
shp_file = "examplee.shp"
gdf.to_file(shp_file, driver='ESRI Shapefile')