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

import urllib.request, urllib.parse, urllib.error
import requests
from bs4 import BeautifulSoup

base_url = "https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions"
html2 = urllib.request.urlopen(base_url).read()
soup = BeautifulSoup(html2, "html.parser")
html = soup.prettify("utf-8")
with open("BSIpage.html", "wb") as file:
	file.write(html)

for stuff in soup.find(class_="body"):
	for line in stuff: 
		print(line)







