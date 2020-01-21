# PlaysTvCrawler
A webcrawler script that downloads videos from PlaysTv
## Motivation
PlaysTv is a tool made to record gameplay. You can also upload your videos to their website. On November 2019 PlaysTv announced that they will discontinue their service on December 15th, 2019. All videos will no longer exist after that date. So I went to look at my PlaysTv account and realized I had almost 290 videos on the platform, and each video had golden gameplay content on it. It was clear that I would download all of them but I immediately thought about writing a script that would do it for me. So I got to work and wrote this PlaysTvCrawler.

## What it does
1. PlaysTvCrawler goes to PlaysTv and logs in.
2. Then it goes to the users homepage and creates a list of all the video links
3. After that it starts to iterate each video and finds the download link and loads the video and deletes that link from the list
4. Each video is given a name in the loop to match that videos title (without special characters and spaces)
5. The program will stop when the video link list is empty

It took 30 minutes for this script to load 290 videos so it saved me from some manual work. 

![](https://media.giphy.com/media/SUoWJNcDP64rf4vP72/giphy.gif)

## How to use
* run with Python 3.8.0
* On line 16, replace USERNAME with your username
* On line 17, replace PASSWORD with your password
* On line 55, replace USERNAME with your username
* Install dependencies (see requirements.txt and imports on top of the code) and run on terminal with: python PlaysTvCrawler.py


## Libraries
* [Selenium](https://selenium-python.readthedocs.io/)
