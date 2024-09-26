import pickle

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Correct import


def test_Amazon_Search():
    # Initialize Chrome Driver
    driver = webdriver.Chrome()

    # Set implicit wait only once
    driver.implicitly_wait(5)

    # Open Amazon
    driver.get('https://www.amazon.com/')

    # Load cookies if you've already saved them
    try:
        with open('amazon_cookies.pkl', 'rb') as file:
            cookies = pickle.load(file)
            for cookie in cookies:
                driver.add_cookie(cookie)
        # Refresh the page to apply cookies
        driver.get('https://www.amazon.com/')
    except FileNotFoundError:
        print("Cookies file not found. Make sure to log in and save cookies first.")

    # Perform the search
    search = driver.find_element(By.ID, 'twotabsearchtextbox')
    search.send_keys('monitor', Keys.ENTER)

    # Verify if the expected text is in search result
    expected_text = '"monitor"'
    actual_text = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text

    # Perform assertion
    assert expected_text == actual_text, f'Error: Expected text {expected_text}, but got {actual_text}'



    # Close the driver
    driver.quit()

# Call the function to execute
test_Amazon_Search()
