import requests
from bs4 import BeautifulSoup as bs

def get_github_profile_details(username):
    github_profile_url = f"https://github.com/{username}"
    req = requests.get(github_profile_url)
    scraper = bs(req.content, "html.parser")

    # Fetching details
    username_element = scraper.find("span", {"class": "p-nickname"})
    name_element = scraper.find("span", {"class": "p-name"})
    bio_element = scraper.find("div", {"class": "p-note"})
    location_element = scraper.find("span", {"class": "p-label"})

    # Extracting content
    username = username_element.text.strip() if username_element else "Not available"
    name = name_element.text.strip() if name_element else "Not available"
    bio = bio_element.text.strip() if bio_element else "Not available"
    location = location_element.text.strip() if location_element else "Not available"

    return {
        "Username": username,
        "Name": name,
        "About": bio,
        "Location": location
    }

# 'sadashiv0001' with the desired GitHub username
profile_details = get_github_profile_details("sadashiv0001")

# Displaying the fetched details
for key, value in profile_details.items():
    print(f"{key}: {value}")
