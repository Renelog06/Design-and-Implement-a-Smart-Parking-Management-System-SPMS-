import json
import os

def load_json(path):
    if not os.path.exists(path):
        return {}
    with open(path, 'r') as f:
        try:
            return json.load(f)
        except:
            return {}
        
def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

