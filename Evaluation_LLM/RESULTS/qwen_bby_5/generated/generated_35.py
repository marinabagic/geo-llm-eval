
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

df = pd.read_csv("LUCAS_with_country_info.csv")
df["pH_H2O"] = pd.to_numeric(df["pH_H2O"], errors="coerce")
df = df.dropna(subset=["pH_H2O", "TH_LONG", "TH_LAT"])

pH_10 = df["pH_H2O"].quantile(0.1)

df = df[(df["Country"] == "Belgium") & (df["pH_H2O"] <= pH_10)]

if df.empty:
    print("No matching points to plot.")
else:
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["TH_LONG"], df["TH_LAT"]), crs="EPSG:4326")

    europe = gpd.read_file("europe.gpkg").to_crs("EPSG:4326")
    belgium = europe[europe["NAME"] == "Belgium"].explode(index_parts=True)
    belgium["area"] = belgium.geometry.area
    belgium_main = belgium[belgium["area"] > 0.5]

    gdf = gdf.to_crs("EPSG:4326")

    fig, ax = plt.subplots(figsize=(10, 10))
    belgium_main.plot(ax=ax, color="lightgrey", edgecolor="black")
    gdf.plot(ax=ax, color="red", marker=".", markersize=10)

    ax.set_title("Belgium: pH_H2O in Bottom 10 Percentile")
    ax.set_xlim(belgium_main.total_bounds[0] - 0.2, belgium_main.total_bounds[2] + 0.2)
    ax.set_ylim(belgium_main.total_bounds[1] - 0.2, belgium_main.total_bounds[3] + 0.2)

    plt.tight_layout()
    plt.savefig('plots/plot35.png', dpi=300)
