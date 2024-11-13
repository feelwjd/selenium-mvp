import time, os
from config import baseDir

class screenShot:
    
    def __init__(self, driver, test_name):
        self.driver = driver
        self.screenshot_step = 1
        self.folder_path = os.path.join(baseDir, test_name)
        
        # 폴더가 없으면 생성
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def take_screenshot(self, action_description):
        time.sleep(2)
        file_path = f"{self.folder_path}/step_{self.screenshot_step}_{action_description}.png"
        self.driver.save_screenshot(file_path)
        self.screenshot_step += 1
    
    # 네비게이션 테스트 때 수행
    def check_url_change_and_capture(self, action_description):
        current_url = self.driver.current_url
        if current_url != self.previous_url:
            self.take_screenshot(action_description)
            self.previous_url = current_url  # 업데이트된 URL로 설정