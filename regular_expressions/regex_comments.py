import re

tag = '<div id="123">Hello</div>'

result = re.match(
    r"""
        <div\s+          # Match opening tag
        id="(\w+)"       # Match id attribute
        >                # End of opening tag
        ([^<>]+)         # Match content of tag
        </div>           # Closing div tag
    
    
    """
    , tag, re.VERBOSE) # if we use "VERBOSE" option then we can write multi line regex with clear comments on each line

print(result)