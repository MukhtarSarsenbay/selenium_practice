from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
button = driver.find_element(By.XPATH, "/html/body/form/button")

first_name.send_keys("Mukhtar", Keys.ENTER)
last_name.send_keys("Sarsenbay", Keys.ENTER)
email.send_keys("test@gmail.com", Keys.ENTER)
# button.send_keys(Keys.ENTER)


