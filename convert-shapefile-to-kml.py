import geopandas as gpd
import fiona
import glob
import os.path

# list files in the directory that have an extension of .kml
filenames: list = glob.glob(r"./KML/*.kml")

fiona.drvsupport.supported_drivers['KML'] = 'rw'

# loop through the files and convert them to shapefiles
for file in filenames:
    # Read the KML file into a GeoDataFrame
    gdf = gpd.read_file(file, driver='KML')

    # Write the GeoDataFrame to a shapefile
    basename: str = os.path.basename(file)
    shp_file: str = f"./Shapefiles/{basename.replace('.kml', '.shp')}"
    gdf.to_file(shp_file, driver='ESRI Shapefile')

    print(f"Converted {file} to {shp_file}")
