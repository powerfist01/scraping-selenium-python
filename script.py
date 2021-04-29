from selenium import webdriver

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--single-process')

chrome_options.binary_location = './executables/headless-chromium'

driver = webdriver.Chrome('./executables/chromedriver', options=chrome_options)

driver.get('https://singhsujeet0.web.app')

html_source = driver.page_source

print(html_source)