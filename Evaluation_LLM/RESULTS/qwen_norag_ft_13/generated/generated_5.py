
import geopandas as gpd
import pandas as pd

# Load data
geo_df = gpd.read_file("geo_df.gpkg")
countries = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp")
europe = gpd.read_file("europe.gpkg")

# Filter for southern Europe
southern_europe = countries[(countries["CENT_LAT"] > 35) & (countries["Continent"] == "Europe")]

# Merge with geo_df to get pH_CaCl2 values
merged_df = pd.merge(geo_df, southern_europe, left_on="NUTS_0", right_on="ISO_A2")

# Calculate average pH_CaCl2
average_ph = merged_df["pH_CaCl2"].mean()

print(f"Average pH in calcium chloride for southern European countries: {average_ph:.2f}")
