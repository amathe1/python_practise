import webbrowser
import time

# List of URLs to open
# Please put wf's in between double quotes with comma seperated as below
urls = [ ]

# Open each URL in Safari
for url in urls:
    # Open URL in Safari
    webbrowser.get('safari').open(url)
    time.sleep(2)  # Wait for 2 seconds before opening the next URL