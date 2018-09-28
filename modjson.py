import json

def create_file(filename):
    data = {'firstname': 'Scott', 'from': 'Nebraska'}
    write_file(data, filename)

def write_file(data, filename):
    # Write data to a json file
    with open(filename, 'w') as outfile:  
        json.dump(data, outfile)

def read_file(filename):
    with open(filename) as json_file:  
        data = json.load(json_file)
        return data

def display_data(data):
    print(data)

def modify(data, name, value):
    data[name] = value
    return data

def main():
    filename = 'data.txt'
    create_file(filename)
    # Read data in
    data = read_file(filename)
    display_data(data)
    # change some field values
    data = modify(data, 'firstname', 'David')
    data = modify(data, 'from', 'Ohio')
    display_data(data)
    write_file(data, filename)

if __name__ == '__main__':
    main()
