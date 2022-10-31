import selenium as sl
from selenium import webdriver
import pandas as pd
import time
from bs4 import BeautifulSoup 
import requests
PATH = "C:\\Users\\HP\\PycharmProject\\opencv\\chromedriver_win32\\chromedriver.exe"
webdriver = webdriver.Chrome(PATH)
webdriver.get('https://soundcloud.com/discover/sets/charts-top:all-music:in')
a = webdriver.find_element_by_xpath('//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div[1]/a').click()

def pause():
    webdriver.find_element_by_xpath('//*[@id="app"]/div[4]/section/div/div[3]/button[2]').click()
def play():
    webdriver.find_element_by_xpath('//*[@id="app"]/div[4]/section/div/div[3]/button[2]').click()
def next():
    webdriver.find_element_by_xpath('//*[@id="app"]/div[4]/section/div/div[3]/button[3]').click()
def previous():
    webdriver.find_element_by_xpath('//*[@id="app"]/div[4]/section/div/div[3]/button[1]').click()
def search():
    query = input('Input For Search')
    webdriver.find_element_by_xpath('//*[@id="app"]/header/div/div[2]/div/form/input').send_keys(query)
    webdriver.find_element_by_xpath('//*[@id="app"]/header/div/div[2]/div/form/button').click()
    url = webdriver.current_url
    print(url)
    res = requests.get(url)
    page = res.text
    soup = BeautifulSoup(page,'html.parser')
    songs = soup.findAll("a", attrs = {'class':'soundTitle__title'}) 

    songslist = []

    for s in songs:
        songslist = s.find('span', attrs={'class':" "})
    print(songslist)    
     

if __name__ == '__main__':
    while True: 
        wish  = input("choise") 
        if wish == 'pause':
            pause()
        elif wish == 'play':
            play()
        elif wish == 'next':
            next()
        elif  wish == 'previous':
            previous()
        elif  wish == 'search':
            search()
        else:
            webdriver.close()    
    else:
        webdriver.close()