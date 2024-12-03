import re

text = "Hello Arun. How are you doing Arun"

result = re.sub("Arun", "Wine", text)

print(result)