import re

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}$'
text =  input('Enter email address: ' )

matches = re.match(pattern,text)
if matches:
    print('Valid email')
else:
    print('Invalid email')