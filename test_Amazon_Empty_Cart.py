import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAmazon_for_Empty_Cart:

    driver = ''  # Class variable (not specific to any instance)

    def setup_method(self):
        # Initialize Chrome Driver
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)  # Set implicit wait
        self.driver.get('https://www.amazon.com/')  # Open Amazon

    def test_check_if_Empty(self):
        try:
            with open('amazon_cookies.pkl', 'rb') as file:
                cookies = pickle.load(file)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)  # Use self to access driver

            self.driver.get('https://www.amazon.com/')  # Refresh the page to apply cookies
            self.driver.find_element(By.ID, 'nav-cart').click()
            actual_text = self.driver.find_element(By.XPATH, "//div[@id='sc-empty-cart']//h3").text
            expected_text = "Your Amazon Cart is empty"
            assert expected_text == actual_text, f'Error: Expected text {expected_text}, but got {actual_text}'



        except FileNotFoundError:
            print("Cookies file not found. Make sure to log in and save cookies first.")






    def teardown_method(self):
        # Close the driver after the test
        self.driver.quit()