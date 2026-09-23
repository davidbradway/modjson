# modjson

A Python tool and script to modify json file data fields.

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
