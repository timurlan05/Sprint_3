from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import home_page

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.home_page = f"{home_page}"
        self.button_locator = (By.CLASS_NAME, "button_button__33qZ0")
        self.link_locator = (By.CLASS_NAME, "Auth_link__1fOlj")
        self.name_input_locator = (By.XPATH, ".//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input")
        self.email_input_locator = (By.XPATH, "//label[text()='Email']/following-sibling::input")
        self.password_input_locator = (By.CSS_SELECTOR, 'input.text.input__textfield.text_type_main-default[type="password"][name="Пароль"]')
        self.register_button_locator = (By.CSS_SELECTOR, 'button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa')
        self.button_lk_locator = (By.CSS_SELECTOR, 'a.AppHeader_header__link__3D_hX[href="/account"]')
        self.constructor_button_locator = (By.CSS_SELECTOR, "p.AppHeader_header__linkText__3q_va.ml-2")
        self.exit_button_locator = (By.CSS_SELECTOR, 'button.Account_button__14Yp3.text.text_type_main-medium.text_color_inactive')
        self.email_lk_locator = (By.CSS_SELECTOR, 'input.text.input__textfield.text_type_main-default[name="name"]')
        self.incorrect_password_locator = (By.XPATH, '//p[@class="input__error text_type_main-default" and text()="Некорректный пароль"]')
        self.bulka_element_locator = (By.XPATH, ".//*[@id='root']/div/main/section[1]/div[2]/ul[1]/a[1]/p") #Флюоресцентная булка R2-D3
        self.bulka_text_element_locator = (By.XPATH, ".//*[@id='root']/div/section[1]/div[1]/div/p")#Название в форме Флюоресцентная булка R2-D3
        self.modal_element_locator = (By.CLASS_NAME, "Modal_modal__contentBox__sCy8X")
        self.sauce_tab_element_locator = (By.XPATH, ".//*[@id='root']/div/main/section[1]/div[1]/div[2]/span") # раздел соусы
        self.spicy_x_sauce_element_locator = (By.XPATH, ".//*[@id='root']/div/main/section[1]/div[2]/ul[2]/a[1]") # Соус Spicy-X
        self.spicy_x_sauce_text_element_locator = (By.XPATH, ".//*[@id='root']/div/section[1]/div[1]/div/p") # название в форме Соус Spicy-X
        self.fillings_tab_element_locator = (By.XPATH, ".//*[@id='root']/div/main/section[1]/div[1]/div[3]/span")#раздел Начинки
        self.meat_fillings_element_locator = (By.XPATH, ".//*[@id='root']/div/main/section[1]/div[2]/ul[3]/a[1]/img")#мясо бессмертных малюсков. бессметритие не помогло
        self.meat_fillings_text_element_locator = (By.XPATH, ".//*[@id='root']/div/section[1]/div[1]/div/p")#текст форме "Мясо бессмертных моллюсков Protostomia"

    def click_button(self):
        button = self.driver.find_element(*self.button_locator)
        button.click()

    def click_link(self):
        link = self.driver.find_element(*self.link_locator)
        link.click()

    def enter_name(self, name):
        input_element = self.driver.find_element(*self.name_input_locator)
        input_element.clear()
        input_element.send_keys(name)

    def enter_email(self, email):
        input_element = self.driver.find_element(*self.email_input_locator)
        input_element.clear()
        input_element.send_keys(email)

    def enter_password(self, password):
        input_element = self.driver.find_element(*self.password_input_locator)
        input_element.clear()
        input_element.send_keys(password)

    def click_register_button(self):
        button_element = self.driver.find_element(*self.register_button_locator)
        button_element.click()

    def click_button_lk(self):
        button_locator = self.driver.find_element(*self.button_lk_locator)
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable(button_locator))
        button.click()

    def click_constructor_button(self):
        click_button = self.driver.find_element(*self.constructor_button_locator)
        click_button.click()

    def click_button_exit(self):
        button = self.driver.find_element(*self.exit_button_locator)
        button.click()

    def element_email_lk(self):
        email_input = self.wait.until(EC.visibility_of_element_located(self.email_lk_locator))
        email_value = email_input.get_attribute("value")
        return email_value

    def incorrect_password(self):
        element = self.wait.until(EC.visibility_of_element_located(self.incorrect_password_locator))
        text = element.text
        return text

    def register(self, name, email, password_reg):
        self.click_button()
        self.wait.until(EC.url_to_be(f"{self.home_page}/login"))
        self.click_link()
        self.wait.until(EC.url_to_be(f"{self.home_page}/register"))
        self.enter_name(name)
        self.enter_email(email)
        self.enter_password(password_reg)
        self.click_register_button()

    def login(self, email, password):
        self.wait.until(EC.url_to_be(f"{self.home_page}/login"))
        self.enter_email(email)
        self.enter_password(password)
        self.click_register_button()
        self.wait.until(EC.url_to_be(f"{self.home_page}/"))