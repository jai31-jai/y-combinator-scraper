thonimport csv
import json

def export_to_json(data, file_path):
    """Export data to a JSON file."""
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def export_to_csv(data, file_path):
    """Export data to a CSV file."""
    if data:
        keys = data[0].keys()
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)