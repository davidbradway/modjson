import json
from typing import Dict, Any

def write_file(filepath: str, data: Dict) -> None:
    # Write data to a json file
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile, indent=4)

def read_file(filepath: str) -> Dict:
    with open(filepath, 'r') as json_file:
        data = json.load(json_file)
        return data

def modify_file_dict(filepath: str, d: Dict) -> Dict:
    # Read data in
    data = read_file(filepath)
    # change some field values
    for key, value in d.items():
        data[key] = value
    write_file(filepath, data)
    return data

def print_pretty(data: Dict) -> None:
    print(json.dumps(data, indent=4))
    
def main() -> None:
    # You can use an abosolute path (yours may vary)
    #filepath = r'C:\Users\dpb6\Downloads\repos\modjson\data.json'
    filepath = r'data.json'
    data = {'firstname': 'Scott', 'from': 'Nebraska'}
    write_file(filepath, data)
    print_pretty(data)
    # Create dictionary of name-value pairs to modify
    d = {'firstname': 'David', 'from': 'Ohio'}
    data = modify_file_dict(filepath, d)
    print_pretty(data)

if __name__ == '__main__':
    main()
