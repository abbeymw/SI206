# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

import requests
from bs4 import BeautifulSoup
import re

base_url = "http://collemc.people.si.umich.edu/data/bshw3StarterFile.html"
r =requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

for stuff in soup.find_all(text=re.compile("student")):
	st = str(stuff)
	st = st.replace("student","AMAZING student")
	stuff.replaceWith(st)

for img in soup.find_all("img", src="logo2.png"):
	img['src'] = 'media/logo.png'

for img in soup.find_all("img", src="https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg"):
	img['src'] = 'media/headshot.jpg'

with open("hw3_BSIpage.html", "wb") as file:
	file.write(str(soup).encode())

