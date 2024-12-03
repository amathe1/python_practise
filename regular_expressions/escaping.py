import re

# Put 'r' to stop python string engine from interpreting this as a new line
#
text = r"-\n-"

print(text)
# Even if we put 'r' here and mention regex as r"-\n-" , it won't work 
# because we have stopped string engine to interprit this as new line
# but this string then passed to regular expression engine
# and the regex engine can also interprit this as a new line
# to stop it, we need to add a escape '\' 
# we can also put escape '\' to both '-' as well
print(re.match(r"-\\n-", text))