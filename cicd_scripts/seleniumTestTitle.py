from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options,  service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])


driver.get('https://google.org')
print(driver.title)
