from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
PATH=r"C:\Users\91962\Downloads\chromedriver_win32\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.get("https://www.techwithtim.net")
wait = WebDriverWait(driver, 3)
visible = EC.visibility_of_element_located
print(driver.title)
search =driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main")))
    print(main.text)
    
finally:
    driver.quit()
