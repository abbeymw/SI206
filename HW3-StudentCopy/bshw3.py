# collarborated with: Nicole Ackerman-Greenberg and Allan Chen

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

# help from this website: http://stackoverflow.com/questions/15056633/python-find-text-using-beautifulsoup-then-replace-in-original-soup-variable

for content in soup.find_all(text=re.compile("student")):	#compiles a list of all the instances of student
	st = str(content)		#turns each instance into a string
	st = st.replace("student","AMAZING student")	#replaces with the new phrase
	content.replaceWith(st)	#replaces the original instance with the new

for img in soup.find_all("img", src="logo2.png"):	#finds the instance of img tag with src tag of the logo
	img['src'] = 'media/logo.png'	#goes to the media file and replaces the src tag with new logo

for img in soup.find_all("img", src="https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg"): #finds the instance of the main image
	img['src'] = 'media/headshot.jpg'	#goes to the media file and replaces the src tag with my personal headshot image

with open("hw3_BSIpage.html", "wb") as file:	
	file.write(str(soup).encode())		#writes all of this code into an html file names hw3_BSIpage.html

