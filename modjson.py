import json

def create_file(filename):
    data = {'firstname': 'Scott', 'from': 'Nebraska'}
    write_file(data, filename)

def write_file(data, filename):
    # Write data to a json file
    with open(filename, 'w') as outfile:  
        json.dump(data, outfile, indent=4)

def read_file(filename):
    with open(filename, 'r') as json_file:  
        data = json.load(json_file)
        return data

def display_data(data):
    print(data)

def modify(data, name, value):
    data[name] = value
    return data

def modify_file_dict(filename, d):
    # Read data in
    data = read_file(filename)
    display_data(data)
    # change some field values
    for key, value in d.items():
        data = modify(data, key, value)
        data = modify(data, 'from', 'Ohio')
    display_data(data)
    write_file(data, filename)

def main():
    abolute_path = r'C:\Users\dpb6\Downloads\repos\modjson\data.txt'
    create_file(abolute_path)
    # Create dictionary of name-value pairs to modify
    d = {'firstname': 'David', 'from': 'Ohio'}
    modify_file_dict(abolute_path, d)

if __name__ == '__main__':
    main()
