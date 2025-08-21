from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import torch

# === Load Fine-Tuned Model v9 ===
model_path = "./ft_lora_v11_2_500"
print("Loading fine-tuned model (v11 500)...")
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
base_model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen2.5-Coder-14B-Instruct",
    device_map="auto",
    load_in_4bit=True,
    trust_remote_code=True,
    torch_dtype=torch.float16
)
model = PeftModel.from_pretrained(base_model, model_path)

# === Generation function ===
def generate(instruction):
    input_text = "Assume the file 'LUCAS_with_country_info.csv' is available and can be used in your code. You are familiar with its structure and contents."
    prompt = f"Instruction:\n{instruction}\n\nInput:\n{input_text}\n\nResponse:"
    inputs = tokenizer(prompt, return_tensors="pt").input_ids.to(model.device)
    with torch.no_grad():
        output = model.generate(inputs, max_new_tokens=512, do_sample=False, temperature=0.7)
    decoded = tokenizer.decode(output[0], skip_special_tokens=True)
    return decoded.split("Response:")[-1].strip()

# === Evaluation Test Cases (cleaned & improved) ===
queries = [
    #rag
    "Show which general land cover class has the highest average soil pH in water.",
    "Plot the average organic carbon content (0–20 cm) by general land cover type.",
    "Compare nitrogen content between Austria and France using a t-test.",
    "Display a histogram of phosphorus content with a KDE overlay.",
    "Print the average pH in calcium chloride for southern European countries.",
    "Create a heatmap showing the correlation matrix of all numeric columns.",
    "Print the top 3 regions (NUTS_2) with the highest average potassium content.",
    "Plot a boxplot of electrical conductivity (EC) grouped by land use class.",
    "Use ANOVA to test if organic carbon content differs across land cover types.",
    "Plot a regression of pH in water vs. potassium.",
    "Identify and print Z-score outliers for electrical conductivity (EC).",
    "Calculate the 95% confidence interval for the mean organic carbon content.",
    "Display a histogram of carbonate content (0–20 cm).",
    "Print average nitrogen content for each general land cover class.",
    "Plot the sampling distribution of mean pH in water from 1000 samples of size 30.",
    "Map all soil sample points across Europe.",
    "Show all points with pH_CaCl2 greater than 6 on a Europe map.",
    "Plot all woodland areas across Europe.",
    "Highlight woodland areas with pH_H2O below 6 on a Europe map.",
    "Map points in Grassland or Woodland where organic carbon content is greater than 20.",
    "Plot the top 10 percent of potassium values across Europe.",
    "Display all points with electrical conductivity greater than 50 on a Europe map.",
    "Map all sampling points colored by detailed land use category (LU1_Desc).",
    "Create a heatmap of pH_CaCl2 values across Europe.",
    "Highlight nitrogen outliers where N > 4 on a Europe map.",
    "Show all locations where organic carbon (20–30 cm) values are available.",
    "Map and compare grassland and cropland locations across Europe.",
    "Display spruce- and pine-dominated forest locations on a Europe map.",
    "Highlight points where the carbon to nitrogen ratio is greater than 10.",
    "Perform KMeans clustering to create 3 spatial clusters and map them across Europe.",

    #FILIPOVI
    "Plot all the points that have pH_CaCl2 > 6.",
    "Plot all the points with LC0_Desc = 'Woodland' in Europe.",
    "Plot all the points with LC0_Desc = 'Woodland' and pH < 6 in Europe.",
    "Perform KMeans clustering on the TH_LAT and TH_LONG data to identify 3 clusters and plot them on a map.",
    "Create a map with markers for all locations where 'K' is above its median value, in Europe.",
    "Generate a heatmap where each point is weighted by 'pH_CaCl2', in Europe.",
    "Create a map with markers for points where 'K' is in the top 10 percentile, in Europe.",
    "Plot the points with 'pH_H2O' > 5 in blue and 'pH_H2O' < 5 in red in Europe.",
    "Create a map displaying the distribution of soil types ('LC0_Desc') across Europe.",
    "Plot all the LC0_Desc = 'Grassland' and LC0_Desc = 'Woodland' points where 'OC' > 20.",
    
    


    # Basic spatial filters
    "Plot all points in Croatia where 'OC' is below 20.",
    "Plot all points in Austria where 'pH_CaCl2' > 5 and LC0_Desc is 'Woodland'.",

    # Europe-wide categorical filter
    "Plot all the points with LC0_Desc = Grassland in Europe.",

    # Statistical filters
    "Plot all points in Slovakia where 'K' is above its 85th percentile.",
    "Create a map of Belgium highlighting points where 'pH_H2O' is in the bottom 10 percentile.",

    # Category coloring
    "Plot all points in Poland where 'OC' > median and color them by LU_DESC.",
    "Show how land cover categories vary across France on a map.",

    # Clustering tasks (cleaned)
    "Perform KMeans clustering on TH_LAT and TH_LONG to identify 4 clusters in Europe and plot them.",
    "Perform KMeans clustering on OC and K values and plot the clusters in Spain.",

    # Custom styling and color logic
    "Plot the points in Europe with 'pH_H2O' > 4 in blue and others in red.",
    "Create a map of Italy where each point is colored by its LC0_Desc category.",

    # Europe-wide threshold plot
    "Plot all points in Europe where 'K' is below its median value."

    


]

# === Run test
# Output file
output_path = "v11_2_500_output.txt"

with open(output_path, "w", encoding="utf-8") as f:
    for i, instruction in enumerate(queries):
        print(f"\n=== Test Case {i + 1}: {instruction} ===")
        f.write(f"\n=== Test Case {i + 1}: {instruction} ===\n")
        
        result = generate(instruction)
        
        print(result)
        f.write(result + "\n")



"""     
    #MOJI STARI SA POCETKA
    "Show all forest areas (LC0_Desc = 'Woodland') where potassium (K) is in the top 10 percent and elevation is above 500 meters.",
    "Plot all locations where soil has more than 20 percent organic carbon (OC) and the pH_H2O value is greater than 6.",
    "Create a heatmap showing electrical conductivity (EC) values across Europe.",
    "Display all points where the amount of Ox_Al is greater than Ox_Fe.",
    "Show all grassland locations (LC0_Desc = 'Grassland') where nitrogen (N) is above 2 and phosphorus (P) is not below detection limit.",
    "Visualize all locations where CaCO3 is less than 1 and pH_CaCl2 is under 5.5  (possible acidified soils).",
    "Compare woodland and cropland areas by showing their average pH_H2O values on a map.",
    "Plot all grassland locations where phosphorus (P) is missing (marked as '< LOD').",
    "Highlight all locations sampled in July 2018, using different colors based on LC0_Desc.",
    "Create a clustered map of soil types based on organic carbon (OC) and CaCO3 values.",
    
# NEW additions tailored to recent improvements
    "Plot all points in Spain where 'OC' is above median and LU_DESC is 'Woodland'.",
    "Map woodland locations in Finland where pH_CaCl2 < 5.",
    "Visualize all locations in Norway where both 'K' and 'pH_H2O' are above their 70th percentile.",
    "Highlight areas in Portugal where 'pH_H2O' is greater than 7 and the LU_DESC is 'Artificial land'.",
    "Show all woodland areas in Finland with OC below its national median.",
    "Map the points in Belgium where K is below the 25th percentile, colored by LU_DESC.",
    "Visualize all locations in Ireland where 'pH_CaCl2' is greater than 6 and LC1_Desc is 'Cropland'.",
    "Display a map of European points with OC above 40 and K above 250.",
    "Plot all samples in the Netherlands where both pH_H2O and OC are above their medians.",
    "Create a map showing TH_LAT vs. TH_LONG in Slovakia, colored by K value using a 'plasma' colormap.",
    "Plot LUCAS points in Europe where LU_DESC is 'Woodland' and pH_H2O is less than 5.5.",
    "Show pH_CaCl2 values across Norway, using a color gradient from blue to red.",
    "Visualize all points in Romania with LC0_Desc = 'Shrubland' and OC below 25.",
    "Map all European points where LC1_Desc is not 'Bare land' and K is in the top 20 percentile.",
    "Display Polish points where LC1_Desc is 'Artificial land' and pH_H2O is above 6.5.",
    "Show all land cover types in Estonia and color points by LC0_Desc.",
    "Perform KMeans clustering using pH_H2O and OC on samples from Croatia and plot the result.",
    "Plot all locations in Greece where LU_DESC is 'Permanent crops' and OC is above the European median.",

    

    "Show all points in Hungary where 'CaCO3' is greater than 10 and 'LC0_Desc' is 'Cropland'.",
    "Map the locations in Denmark where 'Ox_Fe' is above its median and 'LU1_Desc' contains 'Forest'.",
    "Plot the distribution of 'Elev' across Austria, using a color gradient from light blue to dark red.",
    "Display German samples where 'N' is above 0.3 and 'LC1_Desc' is not 'Artificial land'.",
    "Visualize European points where 'CaCO3' is less than 5 and 'LU' is equal to 211.",
    "Show all samples in Lithuania where 'TH_LAT' is greater than 55.5 and 'K' is below the 25th percentile.",
    "Plot a map of Slovenia with points colored by 'pH_CaCl2', but only for 'Shrubland' in LC1_Desc.",
    "Display points in Czech Republic where 'NUTS_2' starts with 'CZ' and 'OC' is greater than 30.",
    "Map the samples in Belgium where 'Ox_Al' is above its 90th percentile, colored by 'LC0_Desc'.",
    "Highlight all samples in Bulgaria with 'EC' greater than 0.6 and 'LU1_Desc' containing 'Crop'.",
     "Plot all samples from France where 'LC0_Desc' is 'Cropland'.",
    "Show the distribution of 'pH_H2O' in Germany using a color scale.",
    "Display all points in Italy where 'OC' is greater than 20.",
    "Plot LUCAS samples in Sweden with 'pH_CaCl2' less than 5.5.",
    "Map all locations in Finland colored by 'LU1_Desc'." """