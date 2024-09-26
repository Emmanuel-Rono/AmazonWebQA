import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestAmazon:
    driver = ''  # Class variable (not specific to any instance)

    def setup_method(self):
        # Initialize Chrome Driver
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)  # Set implicit wait
        self.driver.get('https://www.amazon.com/')  # Open Amazon

    def test_amazon_search(self):
        # Load cookies if you've already saved them
        try:
            with open('amazon_cookies.pkl', 'rb') as file:
                cookies = pickle.load(file)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)  # Use self to access driver
            self.driver.get('https://www.amazon.com/')  # Refresh the page to apply cookies
        except FileNotFoundError:
            print("Cookies file not found. Make sure to log in and save cookies first.")

        # Perform the search
        search_box = self.driver.find_element(By.ID, 'twotabsearchtextbox')  # Accessing driver instance
        search_box.send_keys('monitor', Keys.ENTER)  # Perform search

        # Verify if the expected text is in the search result
        expected_text = '"monitor"'
        actual_text = self.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text  # Accessing driver instance

        # Perform assertion
        assert expected_text == actual_text, f'Error: Expected text {expected_text}, but got {actual_text}'

    def teardown_method(self):
        # Close the driver after the test
        self.driver.quit()