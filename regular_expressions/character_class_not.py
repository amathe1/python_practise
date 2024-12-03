import re


tag = '<div id="123">Hello</div>'

# Creating a regular expression using NOT '^'
result = re.match("<[^>]+>([^<>]+)</[^>]+>", tag)

print(result.group(1))