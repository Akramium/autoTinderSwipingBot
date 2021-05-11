from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
PATH = "/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH)

# Login to Facebook
driver.get(url="https://web.facebook.com/?_rdc=1&_rdr")
email = driver.find_element_by_name("email")
email.send_keys(EMAIL)
password = driver.find_element_by_name("pass")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

# Login to Tinder
time.sleep(5)
driver.get(url="https://tinder.com/")
log_in = driver.find_element_by_link_text("LOG IN")
log_in.click()
time.sleep(3)
facebook = driver.find_elements_by_css_selector("span div")[2]
facebook.click()
time.sleep(3)

# Handle Likes and matches
body = driver.find_element_by_tag_name("body")
body.click()
# Allow Location, Notification popup
for i in range(2):
    body.send_keys(Keys.SHIFT)
    body.send_keys(Keys.SHIFT)
    body.send_keys(Keys.ENTER)
body.send_keys(Keys.ESCAPE)
# Do 100 likes per day
for i in range(100):
    time.sleep(3)
    body.click()
    body.send_keys(Keys.ESCAPE)
    body.send_keys(Keys.RIGHT)
