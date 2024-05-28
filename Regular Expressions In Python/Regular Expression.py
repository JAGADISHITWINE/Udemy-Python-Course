import re

## Match
string = 'bca'
pattern = 'a'
if re.match(pattern,string):
    print("Pattern matched")
else:
    print('No match found')

## search
string = 'bca'
pattern = 'a'
if re.search(pattern,string):
    print("Pattern matched")
else:
    print('No match found')

string = 'abc'
pattern = r'ab{2,}c'
if re.search(pattern,string):
    print("Pattern matched")
else:
    print('No match found')
    
## Wildcard Example
string = 'aaaccb'
pattern = r'a.b'
if re.search(pattern,string):
    print("Pattern matched")
else:
    print('No match found')

## Optional Metacharacter Example
string = 'bccbb'
pattern = r'a?bc'
if re.search(pattern,string):
    print("Pattern matched")
else:
    print('No match found')
    
## Character Class
string = 'Cython'
pattern = r'[CPp]ython'
if re.search(pattern,string):
    print("Pattern matched")
else:
    print('No match found')
    
## Find All
text = 'the sun is shining, the birds are singing'
pattern = r'the'
matches=re.findall(pattern,text)
print(matches)

## Character Class & Find All
text = 'The sun is shining, the birds are singing'
pattern = r'[Tt]he'
matches=re.findall(pattern,text)
print(matches)

## Finding Vowels
text = 'The quick brown fox jumps over the lazy dog'
pattern = r'[aeiou]'
matches=re.findall(pattern,text)
print(matches)

## Shorthand For Numeric Characters
text = 'The meeting is scheduled at 9 AM'
pattern = r'[0-9]'
matches=re.findall(pattern,text)
print(matches)

## W Shorthand
text = 'The variable name is my_var123!???#$#'
pattern = r'\W'
matches=re.findall(pattern,text)
print(matches)

## S Shorthand
text = 'The variable name is my_var123!???#$#'
pattern = r'\S+'
matches=re.findall(pattern,text)
print(matches)