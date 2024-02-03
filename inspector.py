from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_number = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# article_number.click()
print(article_number.text)
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)


# driver.quit()