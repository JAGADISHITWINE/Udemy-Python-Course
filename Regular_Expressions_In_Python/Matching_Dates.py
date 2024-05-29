import re

pattern = r'^\d{4}-\d{2}-\d{2}'
text =  '2023-05-01'

matches = re.match(pattern,text)
if matches:
    print('Valid date format')
else:
    print('Invalid date format')