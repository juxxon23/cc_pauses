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
# set vars
btn_action = None
xpath_q = ""
inpt_email = None
user_email = ""
user_verification_email = ""


def main():
    # clipchamp login
    driver.get(CLIPCHAMP_LOGIN_URL)
    driver.implicitly_wait(3)
    # with outlook
    go_outlook()
    driver.implicitly_wait(3)
    # outlook email
    enter_email(EMAIL_ID, user_email)
    driver.implicitly_wait(3)
    # with email verification
    #enter_email(VERIFICATION_EMAIL_ID, user_verification_email)
    #driver.implicitly_wait(15)


def go_outlook():
    btn_action = elem_by_xpath(DATA_ATTRIBUTE, OUTLOOK_DATA_ATTR)
    btn_action.click()


def enter_email(id_email, val_email):
    inpt_email = driver.find_element(By.ID, id_email)
    inpt_email.send_keys(val_email)
    btn_action = elem_by_xpath(DATA_ATTRIBUTE, BTN_DATA_ATTR)
    btn_action.click()


def elem_by_xpath(attr, val):
    xpath_q = f"//button[@{attr}='{val}']"
    elem = driver.find_element(By.XPATH, xpath_q)
    return elem


# outlook password
#btns = driver.find_elements(By.CLASS_NAME, "fui-Body1")
#for btn in btns:
#    print(btn.text)
#    if btn.text == "Other ways to sign in":
#        btn_action = btn
#        break


# create new project
#btn_action = driver.find_element(By.XPATH, "//button[@data-testid='create-project-button']")
#btn_action.click()
#btns = driver.find_elements(By.CLASS_NAME, "fui-Button")
#btn_action = None
#for btn in btns:
#    print(btn.text)
#    if btn.text == "Send code":
#        print("I'm Here")
#        btn_action = btn
#        break
#btn_action.click()
#driver.implicitly_wait(2)


if __name__ == "__main__":
    main()
