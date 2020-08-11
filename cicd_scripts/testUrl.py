from selenium import webdriver
import sys

urlToTry = 'https://google.org'

# Get the URL to try
if len(sys.argv) == 2:
    urlToTry = sys.argv[1]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options,  service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])


driver.get(urlToTry)
print(driver.title)
