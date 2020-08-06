from selenium import webdriver
from selenium.webdriver.chrome.options import Options

print("Starting Selenium test")

options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)
#driver.get("__URL_TO_TEST__")
driver.get("https://www.youtube.com")

time.sleep(5) # wait for page load

print(driver.getTitle())

element_text = driver.find_element_by_id("title").text

print(element_text)
