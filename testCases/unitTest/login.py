from selenium.webdriver.common.by import By
import time

class Login:
    def __init__(self, driver, screen_shot):
        self.driver = driver
        self.screen_shot = screen_shot

    def perform_login(self, login_id, login_pw):
        self.screen_shot.take_screenshot("initial_page")
        
        self.driver.find_element(By.ID, "input-3").click()
        self.driver.find_element(By.CSS_SELECTOR, ".v-field--focused .mdi-close-circle").click()
        self.driver.find_element(By.ID, "input-3").send_keys(login_id)
        
        self.driver.find_element(By.ID, "input-5").click()
        self.driver.find_element(By.CSS_SELECTOR, ".v-field--focused .mdi-close-circle").click()
        self.driver.find_element(By.ID, "input-5").send_keys(login_pw)
        
        self.driver.find_element(By.CSS_SELECTOR, ".v-btn--block").click()
        time.sleep(1)
        
        self.screen_shot.take_screenshot("home_page")
