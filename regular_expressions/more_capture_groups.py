import re

email = "one.two.three.four@example.com"

result = re.match("((?:\w+\.)*)\w+@\w+\.\w+", email)

print(result.group())
print(result.groups())