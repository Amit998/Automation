from selenium import webdriver
import time


chrome_browser= webdriver.Chrome(executable_path='../webDriver/chromedriver')
chrome_browser.get('https://web.whatsapp.com/')
time.sleep(15)

user_name='Notes'

user=chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
user.click()

message_box=chrome_browser.find_element_by_xpath('//div[@class="_3FRCZ"]')
message_box.send_keys('Hi i Am Whatsapp Bot')
message_box.send_keys(Keys.ENTER)
# message_box=chrome_browser.find_element_by_xpath('//div[@class="_3FRCZ"]')
