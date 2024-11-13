from module import screenShot
from testCases.unitTest.login import Login
from testCases.unitTest.menu_select import MenuSelect
from testCases.unitTest.search import Search
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

# load .env
load_dotenv()

"""
시나리오 : 사용자 관리 조회
로그인 > 메뉴 선택 > (사용자 관리 > 사용자) > 조회 조건 입력 후 조회
"""
class userManagePage:
    """
    화면 요소 ID 설정
    """
    input_department    = "MVP9000_inp_department"
    input_userId        = "MVP9000_inp_userId"
    input_userNm        = "MVP9000_inp_userNm"
    button_search       = "MVP9000_btn_search"
    menu_user_manage    = "MVP0111_group_user_manage"
    menu_item_user      = "MVP0111_item_user"
    select_use_yn       = "MVP9000_sel_useYn"
    select_lock_lock    = "MVP9000_sel_accountLockYn"
    select_delete_yn    = "MVP9000_sel_deleteYn"
    select_item_perPage = "MVP9000_sel_itemsPerPage"
    button_pagnation    = "MVP9000_btn_pagination"
    
    select_list_first   = ".rounded-0:nth-child(2)"
    select_list_second  = ".rounded-0:nth-child(3)"
    select_list_third   = ".rounded-0:nth-child(4)"
    
    select_page_first   = ".v-pagination__item:nth-child(2)"
    select_page_second  = ".v-pagination__item:nth-child(3)"
    select_page_third   = ".v-pagination__item:nth-child(4)"
    select_page_next    = ".mdi-chevron-right"
    select_page_prev    = ".mdi-chevron-left"
    
    """
    INPUT 값 설정
    """
    val_loginId         = "bizmob"
    val_loginPw         = "12345"
    val_department      = "사업"
    val_userId          = "test"
    val_userNm          = "테스트"
    
    test_url            = os.getenv('TEST_URL')

    def setup_method(self, test_name):
        chrome_options = Options()
        chrome_options.add_argument("window-size=1920,1080")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(self.test_url)
        self.screen_shot = screenShot(self.driver, test_name)
        """
        테스트 수행 클래스 호출
        """
        self.login          = Login(self.driver, self.screen_shot)
        self.menu_select    = MenuSelect(self.driver, self.screen_shot)
        self.search         = Search(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_userManageSelect(self):
        try:
            #로그인
            self.login.perform_login(self.val_loginId, self.val_loginPw)
            
            #메뉴 선택
            self.menu_select.select_user_manage_menu(self.menu_user_manage, self.menu_item_user)
            
            #사용자 조회
            ## 조회 조건 - 부서
            self.search.perform_input(self.input_department, self.val_department)
            self.driver.find_element(By.ID, self.button_search).click()
            self.screen_shot.take_screenshot(f"userManage_page_add_{self.input_department}")
            
            ## 조회 조건 - 사용자 아이디
            self.search.perform_input(self.input_userId, self.val_userId)
            self.driver.find_element(By.ID, self.button_search).click()
            self.screen_shot.take_screenshot(f"userManage_page_add_{self.input_userId}")
            
            ## 조회 조건 - 사용자 이름
            self.search.perform_input(self.input_userNm, self.val_userNm)
            self.driver.find_element(By.ID, self.button_search).click()
            self.screen_shot.take_screenshot(f"userManage_page_add_{self.input_userNm}")
            
            ## 조회 조건 - 사용 여부
            self.search.perform_list(self.select_use_yn, self.select_list_second)
            self.driver.find_element(By.ID, self.button_search).click()
            self.screen_shot.take_screenshot(f"userManage_page_add_{self.select_use_yn}")
            
            ## 조회 조건 - 잠김 여부
            self.search.perform_list(self.select_lock_lock, self.select_list_third)
            self.driver.find_element(By.ID, self.button_search).click()
            self.screen_shot.take_screenshot(f"userManage_page_add_{self.select_lock_lock}")
            
            ## 조회 조건 - 삭제 여부
            self.search.perform_list(self.select_delete_yn, self.select_list_third)
            self.driver.find_element(By.ID, self.button_search).click()
            self.screen_shot.take_screenshot(f"userManage_page_add_{self.select_delete_yn}")
            
            # 조회 조건 초기화
            self.search.perform_input(self.input_department, "")
            self.search.perform_input(self.input_userId, "")
            self.search.perform_input(self.input_userNm, "")
            self.search.perform_list(self.select_use_yn, self.select_list_first)
            self.search.perform_list(self.select_lock_lock, self.select_list_first)
            self.search.perform_list(self.select_delete_yn, self.select_list_first)
            self.driver.find_element(By.ID, self.button_search).click()
            
            ## 조회 조건 - 페이지네이션
            self.search.perform_list(self.select_item_perPage, self.select_list_first)
            self.screen_shot.take_screenshot(f"userManage_page_add_{self.select_item_perPage}")
            
            ## 조회 조건 - 2번 탭
            self.driver.find_element(By.CSS_SELECTOR, self.select_page_second).click()
            self.screen_shot.take_screenshot(f"userManage_page_add_{self.button_pagnation}_pageSecond")
            ## 조회 조건 - 1번 탭
            self.driver.find_element(By.CSS_SELECTOR, self.select_page_first).click()
            self.screen_shot.take_screenshot(f"userManage_page_add_{self.button_pagnation}_pageFirst")
            ## 조회 조건 - 다음 페이지
            self.driver.find_element(By.CSS_SELECTOR, self.select_page_next).click()
            self.screen_shot.take_screenshot(f"userManage_page_add_{self.button_pagnation}_pageNext")
            ## 조회 조건 - 이전 페이지
            self.driver.find_element(By.CSS_SELECTOR, self.select_page_prev).click()
            self.screen_shot.take_screenshot(f"userManage_page_add_{self.button_pagnation}_pagePrev")
            
        except Exception as e:
            print('  Failed to compile, exception is %s' % repr(e))
