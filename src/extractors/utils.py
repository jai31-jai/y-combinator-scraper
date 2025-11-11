thonimport json

def load_config(file_path):
    """Load configuration from a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def save_data(data, file_path):
    """Save data to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)