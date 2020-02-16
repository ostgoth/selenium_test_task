import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_selecting_process_tab():
    email = input('\nEnter email: ')
    password = input('Enter password: ')
    
    driver = webdriver.Chrome()
    driver.get("https://www.blueworkslive.com/sLogin.html")
    wait = WebDriverWait(driver, 10)

    element = wait.until(EC.visibility_of_element_located((By.NAME, 'txtLogin')))
    element.clear()
    element.send_keys(email)
    
    driver.find_element_by_id("loginButton").click()
    
    elem = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    elem.clear()
    elem.send_keys(password)
    driver.find_element_by_id("signinbutton").click()
        
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="spacePage"]/div[5]/div/div/div[1]/table/tbody/tr/td'))).click()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#pageHeaderContent > ul > li:nth-child(3)"))).click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.GPYEFSACHS.tableCell li:nth-child(2)"))).click()

    assert driver.find_elements_by_css_selector("div.GPYEFSACHS.tableCell > ul > li.selected"), '"Procesess" tab is not selected'
    header_text = driver.find_elements_by_css_selector("div.activeArchiveHeader > div.titleLabel.headerElement")[1].text.split(" ")[0]
    assert header_text.lower() == 'processes'
    driver.quit()


if __name__ == "__main__":
    test_check_selecting_process_tab()
