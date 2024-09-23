import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import pickle

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open Amazon
driver.get('https://www.amazon.com/')
driver.implicitly_wait(5)

# Load cookies if you've already saved them
try:
    with open('amazon_cookies.pkl', 'rb') as file:
        cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
except FileNotFoundError:
    print("Cookies file not found. Make sure to log in and save cookies first.")

# Refresh the page to apply cookies
driver.get('https://www.amazon.com/')
driver.implicitly_wait(5)

# Perform the search
search = driver.find_element(By.ID, 'twotabsearchtextbox')
search.send_keys('monitor', Keys.ENTER)


#more verification
expected_text ='"monitor"'
actual_text=driver.find_element(By.XPATH,"//span[@class='a-color-state a-text-bold']").text


#is it okay
assert expected_text==actual_text, f'Error, Expected text{expected_text}, actual text{actual_text}'


# Keep the browser open
input("Press Enter to close the browser...")

# Close the driver
driver.quit()