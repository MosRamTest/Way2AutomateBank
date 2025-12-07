from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait, Select


class LoginPage:

    btn_customer_login_xpath = "//button[text()='Customer Login']"
    user_select_id= "userSelect"

    def __init__(self,driver):
        self.driver= driver

    def click_CustomerLogin(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.btn_customer_login_xpath)))
        element.click()

    def select_dropdown_by_text(driver, visible_text):
        wait = WebDriverWait(self.driver, 10)
        dropdown = wait.until(EC.visibility_of_element_located((By.ID, self.user_select_id)))
        select = Select(dropdown)
        select.select_by_visible_text(visible_text)
