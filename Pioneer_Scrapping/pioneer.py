# using selenium to open chrome
from selenium import webdriver
from selenium.webdriver.common.by import By

# using BeautifulSoap for Scrapping
from bs4 import BeautifulSoup

# using pandas to create CSV
import pandas as pd

# importing time to control the flow
import time

# importing requests
# import requests


# need to install chrome driver, you need to change this when clone this repo
chomedriver = 'F:/Python Projects/Pioneer_Scrapping/chromedriver'

# opening the website
browser = webdriver.Chrome(chomedriver)
browser.get('https://account.pioneer.app/login')

# using css selector to click on buttons
login = '/html/body/div[4]/div/div[2]/div[1]/div[1]/div/a'
browser.find_element(By.XPATH, login).click()

# Google authenticating
browser.implicitly_wait(4)
email_field = '//*[@id="identifierId"]'
browser.find_element(By.XPATH, email_field).send_keys('azm2006@gmail.com')
next_button = '//*[@id="identifierNext"]/div/span/span'
browser.find_element_by_xpath(next_button).click()
browser.implicitly_wait(4)
password_field = '//*[@id="password"]/div[1]/div/div[1]/input'
browser.find_element(By.XPATH, password_field).send_keys('Karachi5169141')
browser.find_element_by_xpath('//*[@id="passwordNext"]/div/span').click()
input('Press any key to continue after authenticating')

# The next piece will execute after you complete authenticating
navbarDropdown_button = '//*[@id="navbarDropdown"]'
browser.find_element_by_xpath(navbarDropdown_button).click()
browser.implicitly_wait(4)
Submissions_button = '//*[@id="navbarToggle"]/ul[2]/li[7]/div/a[4]'
browser.find_element_by_xpath(Submissions_button).click()

# Opening first week feedback
browser.implicitly_wait(4)
Week_button = '/html/body/div[4]/div/div/div/div[1]/div/div/div/div/div[35]/a'
browser.find_element_by_xpath(Week_button).click()

# View Feedback
browser.implicitly_wait(4)
viewFeedback_button = '/html/body/div[4]/div/div/div/div[2]/div[3]/div[1]/a'
browser.find_element_by_xpath(viewFeedback_button).click()

# storing content of the current_url
time.sleep(3)

# getting current_url
# current_url = browser.current_url
# content = browser.current_url.page_source
browser.get(browser.current_url)
content = browser.page_source
# Creating BeautifulSoap
soup = BeautifulSoup(content)
text = soup.find_all(text=True)

# Creating lists to store pageContent
Week = []
playerFeedback = []
Player = []

# sifting through content
pageContent = 'page-content'
for a in soup.findAll('a', href=True, attrs={'class': pageContent}):
    Week = text.find('text', attrs={'class': 'mb-3 title'})

# storing feedbackText class
    feedbackText = 'serif feedback-row-text'
    playerFeedback = text.find('div', attrs={'class': feedbackText})
# storing Player Name
    Player = text.find('div', attrs={'class': 'text-md-nowrap'})
# Appending data into lists
    Week.append(Week.text)
    playerFeedback.append(playerFeedback.text)
    Player.append(Player.text)

print(Week)
print(playerFeedback)
print(Player)

# storing data into CSV
# df = pd.DataFrame({'Week': Week, 'Feedback': playerFeedback, 'Player': Player})
# df.to_csv('Pioneer.csv', index=False, encoding='utf-8')
