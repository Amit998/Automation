# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# user_name = "damitlucky998@gmail.com"
# password = "Amitdutta@998"
# driver = webdriver.Edge()
# driver.get("http://exam.tiutel.org/login/index.php")

# element = driver.find_element_by_id("email")
# element.send_keys(user_name)
# element = driver.find_element_by_id("pass")
# element.send_keys(password)
# element.send_keys(Keys.RETURN)
# element.close()
# import webbrowser
# webbrowser.open('http://exam.tiutel.org/login/index.php')
# from selenium.webdriver.common.keys import Keys
# user_name = "181001011010"
# password = "Amitdutta@998"
# element = webbrowser.find_element_by_id("username")
# element.send_keys(user_name)
# element = webbrowser.find_element_by_id("password")
# element.send_keys(password)

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
from selenium import webdriver

browser = webdriver.Edge()
browser.get('http://seleniumhq.org/')