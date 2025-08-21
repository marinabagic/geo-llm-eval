
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

df = pd.read_csv("LUCAS_with_country_info.csv")
df["K"] = pd.to_numeric(df["K"], errors="coerce")
df = df.dropna(subset=["K", "TH_LONG", "TH_LAT"])

k_85 = df["K"].quantile(0.85)
df = df[(df["Country"] == "Slovakia") & (df["K"] > k_85)]

if df.empty:
    print("No matching points to plot.")
else:
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["TH_LONG"], df["TH_LAT"]), crs="EPSG:4326")

    europe = gpd.read_file("europe.gpkg").to_crs("EPSG:4326")
    slovakia = europe[europe["NAME"] == "Slovakia"].explode(index_parts=True)

    fig, ax = plt.subplots(figsize=(10, 10))
    slovakia.plot(ax=ax, color="lightgrey", edgecolor="black")
    gdf.plot(ax=ax, color="red", marker=".", markersize=10)

    ax.set_title("Slovakia: K above 85th percentile")
    ax.set_xlim(gdf.total_bounds[0] - 0.1, gdf.total_bounds[2] + 0.1)
    ax.set_ylim(gdf.total_bounds[1] - 0.1, gdf.total_bounds[3] + 0.1)

    plt.tight_layout()
    plt.savefig('plots/plot34.png', dpi=300)
