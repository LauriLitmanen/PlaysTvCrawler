import webbrowser
import requests
import time
import urllib
import re

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Open browser and got to playstv login page
login_url = 'https://plays.tv/login'
driver = webdriver.Chrome()

def login():
	""" Login  """
	driver.find_element_by_id('login_urlname').send_keys('username')
	driver.find_element_by_id('login_pwd').send_keys('password' + '\n')

def scroll_down():
	"""Scroll at the end of the page """
	elem = driver.find_element_by_tag_name("body")
	no_of_pagedowns = 60
	while no_of_pagedowns:
	    elem.send_keys(Keys.PAGE_DOWN)
	    time.sleep(1)
	    no_of_pagedowns-=1

def open_video(url):
	""" opens the video url  """
	driver.get(url)

def download_video(url, name):
	""" downloads the video """
	print(f"Downloading {name}")
	r = requests.get(url,stream=True)
	#download started
	with open(name, 'wb') as f:
		for chunk in r.iter_content(chunk_size = 1024*1024):
			if chunk:
				f.write(chunk)
	print(f"{name} downloaded!")

def check_name(name):
	"""Get rid of all the special characters in the name and return new name """
	new_name = ''
	new_name = new_name.join(e for e in name if e.isalnum())
	new_name += ".mp3"
	return new_name


driver.get(login_url)
time.sleep(1)
login()
time.sleep(3)
driver.get('https://www.plays.tv/u/USERNAME')
scroll_down()

# Create a list containing all the video URLs
list_of_videos = driver.find_elements_by_css_selector(".thumb-link")
list_of_video_urls = []
for video in list_of_videos:
	list_of_video_urls.append(video.get_attribute("href"))
print(len(list_of_video_urls))

#Get rid of Duplicates in the list
list_of_video_urls = list( dict.fromkeys(list_of_video_urls))
print(f"List length: {len(list_of_video_urls)}")

#Loop through each video and download
while list_of_video_urls:
	#get last video url on list of urls
	last_video_on_the_list = list_of_video_urls.pop(0)

	#open the last video url on list
	open_video(last_video_on_the_list)

	#get the name of the video
	title = driver.find_element_by_class_name("description-text").text
	# Making a name for the video
	name = check_name(title)
	print(f"Preparing to download {name}")
	
	# Download the video
	driver.find_element_by_class_name("dotdotdot").click()
	driver.find_element_by_class_name("download-video").click()
	time.sleep(2) # Wait for the modal to open
	download_url = driver.find_element_by_class_name("download-video-btn").get_attribute("href")
	download_video(download_url, name)
	print(f"List length: {len(list_of_video_urls)}")

print("Downloaded all the videos!")
print(f"List length: {len(list_of_video_urls)}")