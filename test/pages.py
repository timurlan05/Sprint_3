from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from conftest import browser
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)



    def click_button(self):
        button = self.driver.find_element(By.CLASS_NAME, "button_button__33qZ0") # Войти в аккаунт
        button.click()

    def click_link(self):
        link = self.driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj")
        link.click()

    def enter_name(self, name):
        input_element = self.driver.find_element(By.CLASS_NAME, "text.input__textfield.text_type_main-default")
        input_element.clear()
        input_element.send_keys(name)

    def enter_email(self, email):
        input_element = self.driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")
        input_element.clear()
        input_element.send_keys(email)

    def enter_password(self, password):
        input_element = self.driver.find_element(By.CSS_SELECTOR, 'input.text.input__textfield.text_type_main-default[type="password"][name="Пароль"]')
        input_element.clear()
        input_element.send_keys(password)

    def click_register_button(self):
        button_element = self.driver.find_element(By.CSS_SELECTOR, 'button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa')
        button_element.click()

    def click_button_lk(self):
        button_locator = self.driver.find_element(By.CSS_SELECTOR, 'a.AppHeader_header__link__3D_hX[href="/account"]')
        wait = WebDriverWait(browser, 10)
        button = wait.until(EC.element_to_be_clickable(button_locator))
        button.click()

    def click_constructor_button(self):
        click_button = self.driver.find_element(By.CSS_SELECTOR, "p.AppHeader_header__linkText__3q_va.ml-2")
        click_button.click()

    def click_button_exit(self):
        button = self.driver.find_element(By.CSS_SELECTOR,
                                 'button.Account_button__14Yp3.text.text_type_main-medium.text_color_inactive')
        button.click()

    def element_email_lk(self):
        email_input_locator = (By.CSS_SELECTOR, 'input.text.input__textfield.text_type_main-default[name="name"]')
        wait = WebDriverWait(self.driver, 10)
        email_input = wait.until(EC.visibility_of_element_located(email_input_locator))
        email_value = email_input.get_attribute("value")
        return email_value

    def incorrect_password(self):
        locator = (By.XPATH, '//p[@class="input__error text_type_main-default" and text()="Некорректный пароль"]')
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(locator))
        # Получение текста элемента
        text = element.text
        return text










