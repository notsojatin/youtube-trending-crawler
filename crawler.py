import smtplib
import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import xml.dom.minidom



def initialize_driver():
  '''
  function to initialize headless chrome driver
  :return : headless chrome driver isinstance
  '''
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver


def get_videos(driver,url,tag_name):
  '''
  function to return all the video tags from the youtube trending page
  :param driver: driver instance which will be used to access the youtube trending page
  :param url: url of the page that you want to access
  :param tag_name: tag of the video div
  :return list of video div tags
  '''
  driver.get(url)
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  videos=driver.find_elements(By.TAG_NAME,tag_name)
  return videos

def parse_videos(video):
  '''
  function to return all the details about the video in the dictionary format
  :param video: selenium element that contains all the data of the video
  :returns details of video as a dictionary
  '''
  pass

if __name__=='__main__':

  YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending'
  YOUTUBE_VIDEO_TAG_NAME='ytd-video-renderer'
  
  #get driver
  driver =initialize_driver()

  #get list of videos
  videos=get_videos(driver,YOUTUBE_TRENDING_URL,YOUTUBE_VIDEO_TAG_NAME)

  print(len(videos),' have been found on the page')


  #parse videos
  # html_string=videos[0].get_attribute('innerHTML')
  # dom = xml.dom.minidom.parseString(html_string)

  # print(dom.toprettyxml())
  with open('test.xml','w') as f:
    f.write(videos[-1].get_attribute('innerHTML'))