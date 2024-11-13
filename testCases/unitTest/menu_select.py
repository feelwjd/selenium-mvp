from selenium.webdriver.common.by import By
import time

class MenuSelect:
    def __init__(self, driver, screen_shot):
        self.driver = driver
        self.screen_shot = screen_shot

    def select_user_manage_menu(self, menu_user_manage, menu_item_user):
        self.driver.find_element(By.ID, menu_user_manage).click()
        time.sleep(1)
        self.driver.find_element(By.ID, menu_item_user).click()
        time.sleep(1)
        self.screen_shot.take_screenshot("userManage_page")
