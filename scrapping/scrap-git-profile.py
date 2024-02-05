# pip install requests
# pip install beautifulsoup
import requests
from bs4 import BeautifulSoup as bs

github_profile = "https://github.com/sadashiv0001"
req = requests.get(github_profile)
scraper = bs(req.content, "html.parser")

# Check if the image element is found
profile_picture_element = scraper.find("img", {"alt": lambda x: x and x.strip() != ""})
if profile_picture_element:
    profile_picture = profile_picture_element["src"]
    print(profile_picture)
else:
    print("Profile picture not found on the page.")
