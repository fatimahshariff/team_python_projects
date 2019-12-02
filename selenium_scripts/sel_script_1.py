from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome('chromedriver')
browser.get('https://www.wikipedia.org/')
search = browser.find_element_by_id('searchInput')
search.send_keys('seether')
search.send_keys(Keys.ENTER)
body = browser.find_element_by_id('bodyContent')
f = open('testfile.txt', 'w+')
f.write(body.text)