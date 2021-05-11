from selenium import webdriver

PATH = "/Development/chromedriver.exe"

driver = webdriver.Chrome(executable_path=PATH)
driver.get("")