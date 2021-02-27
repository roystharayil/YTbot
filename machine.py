from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from typing import Dict
import time

def browser(proxy):
    PATH = "C:\\Users\\DELL\\Documents\\Quant\\Libraries\\chromedriver\\chromedriver.exe"
    USER = "user-data-dir=C:\\Users\\DELL\\AppData\\Local\\Google\\Chrome\\User Data"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(USER)
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--incognito")
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(PATH, options=chrome_options)

    return driver

def signInGoogle(driver,username,password):
    
    driver.get("https://www.google.com/") 

    time.sleep(5)

    signin = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div[2]/a')
    signin.click()
    time.sleep(5)

    email = driver.find_element_by_id('identifierId')
    email.send_keys(username)
    email.send_keys(Keys.ENTER)
    time.sleep(5)

    pwd = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
    pwd.send_keys(password)
    pwd.send_keys(Keys.ENTER)
    time.sleep(5)

def getUsers(file) -> dict:
    creds = {}
    with open(file, 'r') as f:
        users = f.readlines()    
        for user in users:
            creds.update({user.split(",")[0]:user.split(",")[1]})
    return creds

def search(driver,keyword,engine):
    '''
        Searching for keyword
        -------------------------------------
        Parameters:
        driver : selenium webdriver
        keyword (str) : to search for keyword
        -------------------------------------
    '''
    driver.get(searchEngine(engine,keyword))

def searchEngine(engine,keyword):
    switcher = {
        "google" : f"https://www.google.com/search?q={keyword}",
        "bing" : "https://www.bing.com/",
        "youtube" : "https://www.youtube.com/",
    }
    return switcher.get(engine)

def getVideoLink(driver,keyword):
    """To get the youtube link for the video

    Args:
        driver ([type]): selenium webdriver
        keyword (string): partial search keyword

    Returns:
        [type]: [description]
    """    
    v1 = driver.find_element_by_partial_link_text(keyword) 
    return v1.get_attribute('href')


def likes(driver):
    xpath = '//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]'
    like = driver.find_element_by_xpath(xpath)
    like.click()
    return

def dislikes(driver):
    xpath = '//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[2]'
    like = driver.find_element_by_xpath(xpath)
    like.click()
    return

def subscribe(driver):
    subscribe = driver.find_element_by_id('subscribe-button')
    subscribe.click()
    return

def getChannelInfo(driver) -> Dict:
    """ To get channel information


    Args:
        driver ([type]): selenium webdriver

    Returns:
        Dict: channel name, link, number of subscribers
    """    
    channel_info = {}
    xpath = '//*[@id="text"]/a'
    channel = driver.find_element_by_xpath(xpath)
    link = channel.get_attribute('href')
    name = channel.text()
    subscribers = driver.find_element_by_xpath('//*[@id="owner-sub-count"]')
    channel_info['name'] = name
    channel_info['link'] = link
    channel_info['subscribers'] = subscribers
    return channel_info

def nextVideo(driver):
    next_video = driver.find_element_by_xpath('//*[@id="contents"]/ytd-compact-video-renderer[1]')
    next_video.click()
    return

def faker(driver):
    