from selenium import webdriver

import page
driver = webdriver.Chrome()


def test_check_selecting_process_tab():
    email = 'bezpalyva@gmail.com'
    password = '7k#*qLN7$B!RVaw'

    page.EmailPage(driver).enter_with_mail(email)
    page.PasswordPage(driver).enter_with_password(password)

    page.MainPage(driver).close_intro_modal()
    page.MainPage(driver).open_library()

    lib_page = page.LibraryPage(driver)
    lib_page.select_processes_tab()

    assert lib_page.is_tab_selected(2), '"Procesess" tab is not selected'

    header_text = lib_page.tab_title().split(" ")[0]
    assert header_text.lower() == 'processes'


def teardown_module():
    driver.quit()


if __name__ == "__main__":
    test_check_selecting_process_tab()
