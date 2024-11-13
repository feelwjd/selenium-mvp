from testCases.senarioTest.userManagePage import userManagePage

def main():
    test_class = userManagePage()
    test_class.setup_method("test_userManageSelect")
    test_class.test_userManageSelect()
    test_class.teardown_method()

if __name__ == "__main__":
    main()
