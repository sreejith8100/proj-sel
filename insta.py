from time import sleep
from selenium import webdriver
class LoginPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

    def login(self, username, password):
        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        sleep(5)

def test_login_page(browser):
    login_page = LoginPage(browser)
    login_page.login("user", "pass") #Enter the username and password

    errors = browser.find_elements_by_css_selector('#error_message')
    assert len(errors) == 0

browser=webdriver.Firefox()
browser.implicitly_wait(5)
test_login_page(browser)
