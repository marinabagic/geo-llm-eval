
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

df = pd.read_csv("LUCAS_with_country_info.csv")
df["pH_CaCl2"] = pd.to_numeric(df["pH_CaCl2"], errors="coerce")
df = df[(df["Country"] == "Austria") & (df["pH_CaCl2"] > 5) & (df["LC0_Desc"] == "Woodland")]
df = df.dropna(subset=["TH_LONG", "TH_LAT"])

gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["TH_LONG"], df["TH_LAT"]), crs="EPSG:4326")

europe = gpd.read_file("europe.gpkg").to_crs("EPSG:4326")
country = gpd.read_file("../natural_earth_data/ne_10m_admin_0_countries.shp").to_crs("EPSG:4326")
austria = country[country["NAME"] == "Austria"]

fig, ax = plt.subplots(figsize=(10, 10))
europe.plot(ax=ax, color="lightgrey")
austria.plot(ax=ax, color="white", edgecolor="black")
if not gdf.empty:
    gdf.plot(ax=ax, color="blue", marker=".", markersize=5)
    bounds = gdf.total_bounds
    ax.set_xlim(bounds[0] - 0.5, bounds[2] + 0.5)
    ax.set_ylim(bounds[1] - 0.5, bounds[3] + 0.5)
    ax.set_title("Austria: Woodland with pH_CaCl2 > 5")
else:
    ax.set_xlim(austria.total_bounds[0] - 0.5, austria.total_bounds[2] + 0.5)
    ax.set_ylim(austria.total_bounds[1] - 0.5, austria.total_bounds[3] + 0.5)
    ax.set_title("No matching points in Austria (Woodland & pH_CaCl2 > 5)")

plt.tight_layout()
plt.savefig('plots/plot32.png', dpi=300)
