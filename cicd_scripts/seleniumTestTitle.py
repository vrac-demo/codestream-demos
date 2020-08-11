from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome('/usr/lib/chromedriver', chrome_options=chrome_options,  service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])


driver.get('https://google.org')
print(driver.title)
