## Serialization
import json

data_1 = {
    'Name':'Jaga',
    'Email':'jaga@gmail.com',
    'Contact':'123456789'
}

json_data = json.dumps(data_1)
print(json_data)

## Deserialization
data_2 = json.loads(json_data)
print(data_2)
