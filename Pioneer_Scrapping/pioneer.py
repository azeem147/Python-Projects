# using selenium to open chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException

# using BeautifulSoap for Scrapping
# from bs4 import BeautifulSoup

# using pandas to create CSV
# import pandas as pd

# importing requests
# import requests

# importing time
import time


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

# Viewing Current URL on a new tab
time.sleep(2)
browser.switch_to.window(browser.window_handles[-1])  # swtiching tabs


# extracting dates


def extract_week():
    week_element = browser.find_elements_by_class_name('mb-3')
    dates = []
    for date in week_element:
        print(date.text)
        dates.append(date.text)
    return dates

# extracting feedback text


def extract_feedback():
    feedback_element = browser.find_elements_by_class_name('feedback-row-text')
    feedbacks = []
    for feedback in feedback_element:
        print(feedback.text)
        feedbacks.append(feedback.text)
    return feedback


extract_week()
extract_feedback()
