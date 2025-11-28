from selenium import webdriver
from selenium.webdriver.common.by import By

# set driver for firefox
driver = webdriver.Firefox()
# set cons
CLIPCHAMP_LOGIN_URL = 'https://app.clipchamp.com/login'
DATA_ATTRIBUTE = "data-testid"
OUTLOOK_DATA_ATTR = "provider-Microsoft1P"
BTN_DATA_ATTR = "primaryButton"
EMAIL_ID = "usernameEntry"
VERIFICATION_EMAIL_ID = "proof-confirmation-email-input"
TAG_BTN = "button"
# set vars
#user_email = ""
#user_verification_email = ""


def main():
    # clipchamp login
    #driver.get(CLIPCHAMP_HOME_URL)
    #driver.implicitly_wait(3)
    # create new project
    #create_new_project()
    #driver.implicitly_wait(3)


def go_outlook():
    btn_action = elem_by_xpath(TAG_BTN, DATA_ATTRIBUTE, OUTLOOK_DATA_ATTR)
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


def create_new_project():
    #btn_action = driver.find_element(By.XPATH, "//button[@data-testid='create-project-button']")


if __name__ == "__main__":
    main()
