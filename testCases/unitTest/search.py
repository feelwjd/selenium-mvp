from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class Search:
    def __init__(self, driver):
        self.driver = driver

    def perform_input(self, input_id, value):
        self.driver.find_element(By.ID, input_id).click()
        self.driver.find_element(By.ID, input_id).send_keys(value)
        time.sleep(1)
        
    def perform_list(self, input_id, value):
        self.driver.find_element(By.ID, input_id).click()
        time.sleep(0.5)
        self.driver.find_element(By.CSS_SELECTOR, value).click()
        time.sleep(0.5)
