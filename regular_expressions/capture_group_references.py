import re

tag = '<span id="123">Hello</span>'

result = re.match(
    r"""
        <(\w+)\s+        # Match opening tag
        id="(\w+)"       # Match id attribute
        >                # End of opening tag
        ([^<>]+)         # Match content of tag
        </\1>            # Closing div tag
    
    
    """
    , tag, re.VERBOSE) # if we use "VERBOSE" option then we can write multi line regex with clear comments on each line

if result is None:
    print("No match")
else:       
    tag, id, content = result.groups()
    print(tag, id, content)