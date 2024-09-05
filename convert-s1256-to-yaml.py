import json
import yaml

# Paths to the files
json_file_path = 'nibe/data/s1256.json'
yaml_file_path = 'nibe/data/s1256-config-coils.yaml'

# Function to extract values from the "name" tags
def extract_name_values(json_data):
    values = [entry["name"] for entry in json_data.values() if "name" in entry]
    return values

# Read JSON file
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

# Extract values
values = extract_name_values(json_data)

# Write YAML file
with open(yaml_file_path, 'w', encoding='utf-8') as yaml_file:
    yaml.dump(values, yaml_file, default_flow_style=False, sort_keys=False)

print(f'Values have been written to the file {yaml_file_path}.')
