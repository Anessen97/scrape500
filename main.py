import time

from getpass import getpass

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.firefox.options import Options as FirefoxOptions
#import selenium.webdriver.common.expected_conditions as ExpectedConditions

from bs4 import BeautifulSoup

options = webdriver.FirefoxOptions()
options.headless = True

url = 'https://app.plus500.com'

driver = webdriver.Firefox(options=options)
#driver = webdriver.Firefox()
#driver.get(url)
driver.get(url + '/closed-positions')

driver.implicitly_wait(5)

driver.maximize_window()

log = driver.find_element_by_id("realMoney")

log.click()

#ExpectedConditions.element_to_be_clickable(driver.find_element_by_id("newUserCancel")
try:
    account = driver.find_element_by_id("newUserCancelExperiment")

    ActionChains(driver).move_to_element(account)

    driver.implicitly_wait(2)

    account.click()
except ElementNotInteractableException as exception:

    account = driver.find_element_by_id("newUserCancel")

    ActionChains(driver).move_to_element(account)

    driver.implicitly_wait(2)

    account.click()

email = driver.find_element_by_id("email")

mail = input("Mail: ")

email.send_keys(mail)

passwd = driver.find_element_by_id("password")

pswd = getpass()

passwd.send_keys(pswd)

login = driver.find_element_by_id("submitLogin")

login.click()

#driver.get(url + '/closed-positions')
time.sleep(10)

#driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
title = driver.find_element_by_id("closedPositionsScrollWrapper")

title.send_keys(Keys.END)

time.sleep(2)

source = driver.page_source

soup = BeautifulSoup(source, 'html.parser')

#out = open("pl.html", "w")
#out.write(source)
#out.close()

#values = driver.find_element_by_id("closedPositionsScrollWrapper")
#poss = driver.find_elements_by_class_name("net-pl")

poss = soup.find_all(class_ = "net-pl")

for pos in poss:
    print(pos.text)

driver.close()
