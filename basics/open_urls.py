import webbrowser
import time

# List of URLs to open
# Please put wf's in between double quotes with comma seperated as below
urls = ["https://workflows-prod.us.g.apple.com/pbo/prod/config/workflows/aa4cc8d0-a352-11f0-9c02-2301f24b6b50?serviceType=core",
"https://workflows-prod.us.g.apple.com/pbo/prod/config/workflows/b7aa1c30-a352-11f0-9c02-2301f24b6b50?serviceType=core",
"https://workflows-prod.us.g.apple.com/pbo/prod/config/workflows/c4a9bf30-a352-11f0-975c-6380861d4814?serviceType=core",
"https://workflows-prod.us.g.apple.com/pbo/prod/config/workflows/d1e6b950-a352-11f0-975c-6380861d4814?serviceType=core",
"https://workflows-prod.us.g.apple.com/pbo/prod/config/workflows/df18de00-a352-11f0-9906-650272a32f71?serviceType=core",
"https://workflows-prod.us.g.apple.com/pbo/prod/config/workflows/ec5514d0-a352-11f0-975c-6380861d4814?serviceType=core",
"https://workflows-prod.us.g.apple.com/pbo/prod/config/workflows/f9a2fee0-a352-11f0-9c02-2301f24b6b50?serviceType=core",
"https://workflows-prod.us.g.apple.com/pbo/prod/config/workflows/06e1f4d0-a353-11f0-975c-6380861d4814?serviceType=core",
"https://workflows-prod.us.g.apple.com/pbo/prod/config/workflows/13f1eb80-a353-11f0-975c-6380861d4814?serviceType=core",
"https://workflows-prod.us.g.apple.com/pbo/prod/config/workflows/21019410-a353-11f0-9c02-2301f24b6b50?serviceType=core",
"https://workflows-prod.us.g.apple.com/pbo/prod/config/workflows/2e305d60-a353-11f0-9906-650272a32f71?serviceType=core",
"https://workflows-prod.us.g.apple.com/pbo/prod/config/workflows/3b405410-a353-11f0-9c02-2301f24b6b50?serviceType=core",
"https://workflows-prod.us.g.apple.com/pbo/prod/config/workflows/4861fe00-a353-11f0-975c-6380861d4814?serviceType=core",
"https://workflows-prod.us.g.apple.com/pbo/prod/config/workflows/557ddb90-a353-11f0-9c02-2301f24b6b50?serviceType=core",
"https://workflows-prod.us.g.apple.com/pbo/prod/config/workflows/62c1b380-a353-11f0-975c-6380861d4814?serviceType=core",
"https://workflows-prod.us.g.apple.com/pbo/prod/config/workflows/6fe1d6d0-a353-11f0-975c-6380861d4814?serviceType=core",
"https://workflows-prod.us.g.apple.com/pbo/prod/config/workflows/7cfca2f0-a353-11f0-975c-6380861d4814?serviceType=core",
"https://workflows-prod.us.g.apple.com/pbo/prod/config/workflows/8a02ae90-a353-11f0-975c-6380861d4814?serviceType=core",
"https://workflows-prod.us.g.apple.com/pbo/prod/config/workflows/9710d080-a353-11f0-9906-650272a32f71?serviceType=core",
"https://workflows-prod.us.g.apple.com/pbo/prod/config/workflows/a47aa700-a353-11f0-975c-6380861d4814?serviceType=core",

]
# Open each URL in Safari
for url in urls:
    # Open URL in Safari
    webbrowser.get('safari').open(url)
    time.sleep(2)  # Wait for 2 seconds before opening the next URL