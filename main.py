import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# set cons
CLIPCHAMP_LOGIN_URL = 'https://app.clipchamp.com/login'

DATA_ATTRIBUTE = "data-testid"
OUTLOOK_DATA_ATTR = "provider-Microsoft1P"
EMAIL_DATA_ATTR = "tile"
PROJECT_DATA_ATTR = "create-project-button"
BTN_DATA_ATTR = "primaryButton"

EMAIL_ID = "usernameEntry"
VERIFICATION_EMAIL_ID = "proof-confirmation-email-input"
RECORD_CREATE_ID = "sidebar-button-recordCreate"
VOICEOVER_ID = "voiceover"

TAG_BTN = "button"
TAG_DIV = "div"

# set vars
#user_email = ""
#user_verification_email = ""
user_path = os.path.expanduser('~user') 
user_profile = "Profile #"

# init driver
driver = None 


def main():
    driver.get(CLIPCHAMP_LOGIN_URL)
    driver.implicitly_wait(3)
    select_outlook()
    driver.implicitly_wait(3)
    select_email()
    driver.implicitly_wait(8)
    create_new_project()
    driver.implicitly_wait(3)
    select_record_create()
    driver.implicitly_wait(1)
    select_voiceover()
    driver.implicitly_wait(2)
    #todo
    #agregar texto 
    #agregar pausas


def set_chrome_driver():
    options = Options()
    options.add_argument(f"user-data-dir={user_path}/.config/chromium/")
    options.add_argument(f"profile-directory={user_profile}")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    return driver


def set_firefox_driver():
    profile_path = f"{user_path}/.mozilla/firefox/{user_profile}.default"
    options = Options()
    firefox_profile = FirefoxProfile(profile_path)
    options.profile = firefox_profile
    driver = webdriver.Firefox(options=options)
    return driver


def select_outlook():
    btn_action = elem_by_xpath(TAG_BTN, DATA_ATTRIBUTE, OUTLOOK_DATA_ATTR)
    btn_action.click()


def select_email():
    btn_action = elem_by_xpath(TAG_DIV, DATA_ATTRIBUTE, EMAIL_DATA_ATTR)
    btn_action.click()


def create_new_project():
    btn_action = elem_by_xpath(TAG_BTN, DATA_ATTRIBUTE, PROJECT_DATA_ATTR)
    btn_action.click()


def select_record_create():
    btn_action = driver.find_element(By.ID, RECORD_CREATE_ID)
    btn_action.click()


def select_voiceover():
    btn_action = driver.find_element(By.ID, VOICEOVER_ID)
    btn_action.click()


def enter_email(id_email, val_email):
    inpt_email = driver.find_element(By.ID, id_email)
    inpt_email.send_keys(val_email)
    btn_action = elem_by_xpath(TAG_BTN, DATA_ATTRIBUTE, BTN_DATA_ATTR)
    btn_action.click()


def elem_by_xpath(tag, attr, val):
    xpath_q = f"//{tag}[@{attr}='{val}']"
    elem = driver.find_element(By.XPATH, xpath_q)
    return elem


def all_elem_by_xpath(tag, attr, val):
    xpath_q = f"//{tag}[@{attr}='{val}']"
    elems = driver.find_elements(By.XPATH, xpath_q)
    return elems


if __name__ == "__main__":
    driver = set_chrome_driver()
    main()
