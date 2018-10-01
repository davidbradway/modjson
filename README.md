# modjson

A Python tool and script to modify json file data fields. This project is intended to help manage POPS files on the Sequoia scanner and modify them while imaging.

## Installation

just download or clone and add to your path.

## Usage example

`python`  

```python
from modjson import write_file, modify_file_dict
filepath = r'data.json'
data = {'firstname': 'Scott', 'from': 'Nebraska'}
write_file(filepath, data)
# Create dictionary of name-value pairs to modify
data = {'firstname': 'David', 'from': 'Ohio'}
modify_file_dict(filepath, data)
```
