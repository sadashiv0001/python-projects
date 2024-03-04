from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# Creating an instance
driver = webdriver.Chrome("Enter-Location-Of-Your-Web-Driver")

# Logging into LinkedIn
driver.get("https://linkedin.com/uas/login")
time.sleep(5)

username = driver.find_element(By.ID, "username")
username.send_keys("") # Enter Your Email Address

pword = driver.find_element(By.ID, "password")
pword.send_keys("")	 # Enter Your Password

driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Opening Sadashiv's Profile
# paste the URL of Sadashiv's profile here
profile_url = "https://www.linkedin.com/in/sadashiv-mitra"

driver.get(profile_url)	 # this will open the link
