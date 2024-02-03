from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")


events_time = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
events_desc = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {}
for i in range(len(events_time)):
    events[i] = {
        "time": events_time[i].text,
        "name": events_desc[i].text,
    }
print(events)
#driver.close()
driver.quit()
