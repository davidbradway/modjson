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

def display_data(data: Dict) -> None:
    print(data)

def modify(data: Dict, name: str, value: Any) -> Dict:
    data[name] = value
    return data

def modify_file_dict(filepath: str, d: Dict) -> None:
    # Read data in
    data = read_file(filepath)
    display_data(data)
    # change some field values
    for key, value in d.items():
        data = modify(data, key, value)
        data = modify(data, 'from', 'Ohio')
    display_data(data)
    write_file(filepath, data)

def main() -> None:
    filepath = r'C:\Users\dpb6\Downloads\repos\modjson\data.txt'
    data = {'firstname': 'Scott', 'from': 'Nebraska'}
    write_file(filepath, data)
    # Create dictionary of name-value pairs to modify
    data = {'firstname': 'David', 'from': 'Ohio'}
    modify_file_dict(filepath, data)

if __name__ == '__main__':
    main()
