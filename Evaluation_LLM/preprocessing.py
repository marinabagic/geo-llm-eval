import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# === 1. Load LUCAS dataset ===
df = pd.read_csv("LUCAS-SOIL-2018.csv")

# Ensure latitude and longitude columns exist
if "TH_LAT" not in df.columns or "TH_LONG" not in df.columns:
    raise ValueError("Missing TH_LAT or TH_LONG columns in the dataset.")

# === 2. Convert to GeoDataFrame using TH_LAT and TH_LONG ===
geometry = [Point(xy) for xy in zip(df["TH_LONG"], df["TH_LAT"])]
gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")

# === 3. Load country polygons ===
world = gpd.read_file("natural_earth_data/ne_110m_admin_0_countries.shp")

# === 4. Spatial join: match points to countries ===
gdf_with_country = gpd.sjoin(
    gdf,
    world[["geometry", "NAME", "CONTINENT"]],  # Use uppercase NAME and CONTINENT
    how="left",
    predicate="within"
)

# === 5. Rename and enrich ===
gdf_with_country.rename(columns={"NAME": "Country", "CONTINENT": "Continent"}, inplace=True)
gdf_with_country["IsInEurope"] = gdf_with_country["Continent"] == "Europe"

# === 6. Save to enriched CSV ===
gdf_with_country.drop(columns=["geometry", "index_right"]).to_csv("LUCAS_with_country_info.csv", index=False)

print("Saved enriched dataset to 'LUCAS_with_country_info.csv'")




""" import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# === 1. Load your original LUCAS dataset ===
df = pd.read_csv("LUCAS-SOIL-2018.csv")  # Ensure this file is in the same directory

# === 2. Convert to GeoDataFrame ===
geometry = [Point(xy) for xy in zip(df["TH_LONG"], df["TH_LAT"])]
gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")

# === 3. Load country polygons (from built-in Natural Earth data) ===
world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

# === 4. Spatial join: map each point to a country and continent ===
gdf_with_country = gpd.sjoin(gdf, world[["geometry", "name", "continent"]], how="left", predicate="within")

# === 5. Clean up column names and enrich with IsInEurope ===
gdf_with_country.rename(columns={"name": "Country", "continent": "Continent"}, inplace=True)
gdf_with_country["IsInEurope"] = gdf_with_country["Continent"] == "Europe"

# === 6. Save to new CSV without geometry columns ===
gdf_with_country.drop(columns=["geometry", "index_right"]).to_csv("LUCAS_with_country_info.csv", index=False)

print("Enriched dataset saved as 'LUCAS_with_country_info.csv'") """

""" import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import requests
import zipfile
import io
import os

# === 1. Load your original LUCAS dataset ===
df = pd.read_csv("LUCAS-SOIL-2018.csv")  # Ensure this file is in the same directory

# === 2. Convert to GeoDataFrame ===
geometry = [Point(xy) for xy in zip(df["TH_LONG"], df["TH_LAT"])]
gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")

# === 3. Download and load country polygons from Natural Earth ===
natural_earth_url = "https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/110m/cultural/ne_110m_admin_0_countries.zip"
data_dir = "natural_earth_data"
os.makedirs(data_dir, exist_ok=True)
zip_path = os.path.join(data_dir, "ne_110m_admin_0_countries.zip")
shp_path = os.path.join(data_dir, "ne_110m_admin_0_countries.shp")

# Download and extract if not already present
if not os.path.exists(shp_path):
    print("Downloading Natural Earth dataset...")
    response = requests.get(natural_earth_url)
    z = zipfile.ZipFile(io.BytesIO(response.content))
    z.extractall(data_dir)
    print("Dataset downloaded and extracted.")

# Load the shapefile
world = gpd.read_file(shp_path)

# === 4. Spatial join: map each point to a country and continent ===
gdf_with_country = gpd.sjoin(gdf, world[["geometry", "NAME", "CONTINENT"]], how="left", predicate="within")

# === 5. Clean up column names and enrich with IsInEurope ===
gdf_with_country.rename(columns={"NAME": "Country", "CONTINENT": "Continent"}, inplace=True)
gdf_with_country["IsInEurope"] = gdf_with_country["Continent"] == "Europe"

# === 6. Save to new CSV without geometry columns ===
gdf_with_country.drop(columns=["geometry", "index_right"]).to_csv("LUCAS_with_country_info.csv", index=False)

print("Enriched dataset saved as 'LUCAS_with_country_info.csv'") """
