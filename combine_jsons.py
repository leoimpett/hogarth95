import os
import json

# Directory containing JSON files
JSON_DIR = "json_outputs"
# Output JSON file
OUTPUT_FILE = "combined_folders.json"

# Delay (in milliseconds) between consecutive windows
DELAY_BETWEEN_WINDOWS = 20000

# List of JSON files to be processed

# Let's do the followning. 
# Start with Battle of the Pictures - this is the theme. But maybe delay that start a bit. 
# Then a text box
# Then...


# Reserve list
    # "John Wilkes.json",

json_files = [
    "Battle of Pictures.json",
    "Stages of Cruelty.json",
    "Gate of Calais.json",
    "Rake's Progress plate 3.json",
    "Self-Portrait Pug.json",
    "Self_Portrait_Trump_RTI_Export_LWL.json",
    "Self-Portrait Bear.json",
    "Self-Portrait with Comic Muse.json",
    "Self_Portrait_Muse_RTI_LWL_Export.json",
    "Harlot's Progress Plate 2.json",
    "Gin Lane.json",
]

# List to hold all windows from all JSON files
all_windows = []

# Read the specified JSON files and append windows to the list
# DEFINE START TIME BY SETTING THIS
total_time = 0

for json_file in json_files:
    with open(os.path.join(JSON_DIR, json_file), 'r') as f:
        data = json.load(f)
        windows = data.get("windows", [])
        
        # Update the timings for each window
        for window in windows:
            window["createTime"] += total_time
            for keyframe in window["keyframes"]:
                keyframe["time"] += total_time
            all_windows.append(window)
        
        # Update total_time to include the delay after the last window of this file
        if windows:
            last_window = windows[-1]
            last_keyframe_time = max(keyframe["time"] for keyframe in last_window["keyframes"])
            total_time = last_keyframe_time + DELAY_BETWEEN_WINDOWS

# Create the final JSON structure
final_data = {
    "windows": all_windows
}

# Write the patched JSON to the output file
with open(OUTPUT_FILE, 'w') as f:
    json.dump(final_data, f, indent=2)

print(f"Patched JSON saved to '{OUTPUT_FILE}'")
