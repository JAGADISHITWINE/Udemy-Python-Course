import re

text = 'Please contact me at +91 (123) 456-7890 or via email at john@example.com'

# +1 (123) 456-7890

pattern = r'\+?\d{1,3}[-.\s]\(?\d{1,3}\)?[-.\s]?\d{1,3}[-.\s]?\d{1,4}'

matches = re.findall(pattern,text)
print(matches)