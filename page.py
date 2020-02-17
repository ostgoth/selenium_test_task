from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


class EmailPage(BasePage):

    def enter_with_mail(self, email):
        self.driver.get("https://www.blueworkslive.com/sLogin.html")

        element = self.wait.until(EC.visibility_of_element_located((By.NAME, 'txtLogin')))
        element.clear()
        element.send_keys(email)

        self.driver.find_element_by_id("loginButton").click()


class PasswordPage(BasePage):

    def enter_with_password(self, password):
        elem = self.wait.until(EC.visibility_of_element_located((By.ID, "password")))
        elem.clear()
        elem.send_keys(password)
        self.driver.find_element_by_id("signinbutton").click()


class MainPage(BasePage):

    def close_intro_modal(self):
        close_modal_selector = (By.CSS_SELECTOR, '.gwt-PopupPanel .bpDialogHeaderXButtonImage')
        self.wait.until(EC.visibility_of_element_located(close_modal_selector)).click()

    def open_library(self):
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#pageHeaderContent > ul > li:nth-child(3)"))).click()


class LibraryPage(BasePage):

    def select_processes_tab(self):
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.GPYEFSACHS.tableCell li:nth-child(2)"))).click()

    def is_tab_selected(self, index):
        return bool(
            self.driver.find_elements_by_css_selector(f"div.GPYEFSACHS.tableCell > ul > li:nth-child({index}).selected")
        )

    def tab_title(self):
        title_selector = "div.activeArchiveHeader > div.titleLabel.headerElement"
        return self.driver.find_elements_by_css_selector(title_selector)[1].text
