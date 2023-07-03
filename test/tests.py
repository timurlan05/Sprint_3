from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pages import LoginPage
import pytest

# Регистрация и вход
def test_login_page(browser, email, password_reg, home_page):
    email, name = email
    login_page = LoginPage(browser)
    browser.get(home_page)
    wait = WebDriverWait(browser, 10)
    login_page.click_button()
    wait.until(EC.url_to_be(f"{home_page}/login"))
    login_page.click_link()
    wait.until(EC.url_to_be(f"{home_page}/register"))
    login_page.enter_name(name)
    login_page.enter_email(email)
    login_page.enter_password(password_reg)
    login_page.click_register_button()
    wait.until(EC.url_to_be(f"{home_page}/login"))
    login_page.enter_email(email)
    login_page.enter_password(password_reg)
    login_page.click_register_button()
    wait.until(EC.url_to_be(f"{home_page}/"))
    login_page.click_button_lk()
    email_value = login_page.element_email_lk() # логин указанный в личном кабитене после авторизации
    expected_email = email # логин при регистрации
    assert email_value == expected_email, f"Expected email: {expected_email}, Actual email: {email_value}"

# Некорректный пароль при регистарции
def test_incorrect_password(browser, email, home_page, incorrect_password):
    email, name = email
    login_page = LoginPage(browser)
    browser.get(home_page)
    wait = WebDriverWait(browser, 10)
    login_page.click_button()
    wait.until(EC.url_to_be(f"{home_page}/login"))
    login_page.click_link()
    wait.until(EC.url_to_be(f"{home_page}/register"))
    login_page.enter_name(name)
    login_page.enter_email(email)
    login_page.enter_password(incorrect_password)
    login_page.click_register_button()
    text = login_page.incorrect_password()
    expected_text = "Некорректный пароль"
    assert text == expected_text

# вход по кнопке «Войти в аккаунт» на главной
def test_login_main_page(browser, email, password_reg, home_page):
    email, name = email
    login_page = LoginPage(browser)
    browser.get(home_page)
    wait = WebDriverWait(browser, 10)
    login_page.click_button()
    wait.until(EC.url_to_be(f"{home_page}/login"))
    login_page.click_link()
    wait.until(EC.url_to_be(f"{home_page}/register"))
    login_page.enter_name(name)
    login_page.enter_email(email)
    login_page.enter_password(password_reg)
    login_page.click_register_button()
    browser.get(f'{home_page}')
    login_page.click_button()
    wait.until(EC.url_to_be(f"{home_page}/login"))
    login_page.enter_email(email)
    login_page.enter_password(password_reg)
    login_page.click_register_button()
    login_page.click_button_lk()
    email_value = login_page.element_email_lk()  # логин указанный в личном кабитене после авторизации
    expected_email = email  # логин при регистрации
    assert email_value == expected_email, f"Expected email: {expected_email}, Actual email: {email_value}"

# вход через кнопку «Личный кабинет»
def test_login_lk_page(browser, email, password_reg, home_page):
    email, name = email
    login_page = LoginPage(browser)
    browser.get(home_page)
    wait = WebDriverWait(browser, 10)
    login_page.click_button()
    wait.until(EC.url_to_be(f"{home_page}/login"))
    login_page.click_link()
    wait.until(EC.url_to_be(f"{home_page}/register"))
    login_page.enter_name(name)
    login_page.enter_email(email)
    login_page.enter_password(password_reg)
    login_page.click_register_button()
    browser.get(f'{home_page}')
    login_page.click_button_lk()
    wait.until(EC.url_to_be(f"{home_page}/login"))
    login_page.enter_email(email)
    login_page.enter_password(password_reg)
    login_page.click_register_button()
    login_page.click_button_lk()
    email_value = login_page.element_email_lk()  # логин указанный в личном кабитене после авторизации
    expected_email = email  # логин при регистрации
    assert email_value == expected_email, f"Expected email: {expected_email}, Actual email: {email_value}"


# вход через кнопку в форме регистрации
def test_login_registr_page(browser, email, password_reg, home_page):
    email, name = email
    login_page = LoginPage(browser)
    browser.get(home_page)
    wait = WebDriverWait(browser, 10)
    login_page.click_button()
    wait.until(EC.url_to_be(f"{home_page}/login"))
    login_page.click_link()
    wait.until(EC.url_to_be(f"{home_page}/register"))
    login_page.enter_name(name)
    login_page.enter_email(email)
    login_page.enter_password(password_reg)
    login_page.click_register_button()

    browser.get(f"{home_page}/register")
    wait = WebDriverWait(browser, 10)
    button = browser.find_element_by_link_text("Войти").click()
    wait.until(EC.url_to_be(f"{home_page}/login"))

    login_page.enter_email(email)
    login_page.enter_password(password_reg)
    login_page.click_register_button()
    login_page.click_button_lk()
    email_value = login_page.element_email_lk()  # логин указанный в личном кабитене после авторизации
    expected_email = email  # логин при регистрации
    assert email_value == expected_email, f"Expected email: {expected_email}, Actual email: {email_value}"

# вход через кнопку в форме восстановления пароля
def test_login_forgot_password_page(browser, email, password_reg, home_page):
    email, name = email
    login_page = LoginPage(browser)
    browser.get(home_page)
    wait = WebDriverWait(browser, 10)
    login_page.click_button()
    wait.until(EC.url_to_be(f"{home_page}/login"))
    login_page.click_link()
    wait.until(EC.url_to_be(f"{home_page}/register"))
    login_page.enter_name(name)
    login_page.enter_email(email)
    login_page.enter_password(password_reg)
    login_page.click_register_button()

    browser.get(f"{home_page}/forgot-password")
    wait = WebDriverWait(browser, 10)
    button = browser.find_element_by_link_text("Войти").click()
    wait.until(EC.url_to_be(f"{home_page}/login"))

    login_page.enter_email(email)
    login_page.enter_password(password_reg)
    login_page.click_register_button()
    login_page.click_button_lk()
    email_value = login_page.element_email_lk()  # логин указанный в личном кабитене после авторизации
    expected_email = email  # логин при регистрации
    assert email_value == expected_email, f"Expected email: {expected_email}, Actual email: {email_value}"

# Переход в личный кабинет
def test_login_page(browser, email, password_reg, home_page):
    email, name = email
    login_page = LoginPage(browser)
    browser.get(home_page)
    wait = WebDriverWait(browser, 10)
    login_page.click_button()
    wait.until(EC.url_to_be(f"{home_page}/login"))
    login_page.click_link()
    wait.until(EC.url_to_be(f"{home_page}/register"))
    login_page.enter_name(name)
    login_page.enter_email(email)
    login_page.enter_password(password_reg)
    login_page.click_register_button()
    wait.until(EC.url_to_be(f"{home_page}/login"))
    login_page.enter_email(email)
    login_page.enter_password(password_reg)
    login_page.click_register_button()
    wait.until(EC.url_to_be(f"{home_page}/"))
    login_page.click_button_lk()
    email_value = login_page.element_email_lk() # логин указанный в личном кабитене после авторизации
    expected_email = email # логин при регистрации
    assert email_value == expected_email, f"Expected email: {expected_email}, Actual email: {email_value}"

#Переход из личного кабинета в конструктор
def test_login_page(browser, email, password_reg, home_page):
    email, name = email
    login_page = LoginPage(browser)
    browser.get(home_page)
    wait = WebDriverWait(browser, 10)
    login_page.click_button()
    wait.until(EC.url_to_be(f"{home_page}/login"))
    login_page.click_link()
    wait.until(EC.url_to_be(f"{home_page}/register"))
    login_page.enter_name(name)
    login_page.enter_email(email)
    login_page.enter_password(password_reg)
    login_page.click_register_button()
    wait.until(EC.url_to_be(f"{home_page}/login"))
    login_page.enter_email(email)
    login_page.enter_password(password_reg)
    login_page.click_register_button()
    wait.until(EC.url_to_be(f"{home_page}/"))
    login_page.click_button_lk()
    wait.until(EC.url_to_be(f"{home_page}/account/profile"))
    login_page.click_constructor_button()
    wait.until(EC.url_to_be(f"{home_page}/"))
    assert browser.current_url == f"{home_page}/"

# Выход из аккаунта
def test_exit_account(browser, email, password_reg, home_page):
    email, name = email
    login_page = LoginPage(browser)
    browser.get(home_page)
    wait = WebDriverWait(browser, 10)
    login_page.click_button()
    wait.until(EC.url_to_be(f"{home_page}/login"))
    login_page.click_link()
    wait.until(EC.url_to_be(f"{home_page}/register"))
    login_page.enter_name(name)
    login_page.enter_email(email)
    login_page.enter_password(password_reg)
    login_page.click_register_button()
    wait.until(EC.url_to_be(f"{home_page}/login"))
    login_page.enter_email(email)
    login_page.enter_password(password_reg)
    login_page.click_register_button()
    wait.until(EC.url_to_be(f"{home_page}/"))
    login_page.click_button_lk()
    wait.until(EC.url_to_be(f"{home_page}/account/profile"))
    login_page.click_button_exit()
    wait.until(EC.url_to_be(f'{home_page}/login'))
    element = browser.find_element(By.CSS_SELECTOR, 'a.Auth_link__1fOlj[href="/register"]').click()
    wait.until(EC.url_to_be(f'{home_page}/register'))
    assert browser.current_url == f"{home_page}/register"


# Проверка раздела Булки
def test_tab_navigation_bulki(browser, home_page):
    browser.get(home_page)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.url_to_be(f'{home_page}/'))

    # Найти элемент по тексту

    element_locator = (By.XPATH, f"//p[@class='BurgerIngredient_ingredient__text__yp3dH' and text()='Флюоресцентная булка R2-D3']")
    element = wait.until(EC.element_to_be_clickable(element_locator))

    # Нажать на элемент
    element.click()

    element_locator = (By.XPATH, f"//p[@class='text text_type_main-medium mb-8' and text()='Флюоресцентная булка R2-D3']")
    element = wait.until(EC.visibility_of_element_located(element_locator))

    # Нажать на элемент
    element.click()

    element_locator = (By.CLASS_NAME, "Modal_modal__contentBox__sCy8X")
    element = wait.until(EC.visibility_of_element_located(element_locator))
    assert element.is_displayed()

 # Проверка перехда в раздел Соусы
def test_tab_navigation_sauce(browser, home_page):
    browser.get(home_page)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.url_to_be(f'{home_page}/'))

    # Определение локатора элемента
    element_locator = (By.XPATH, "//span[@class='text text_type_main-default' and text()='Соусы']")
    element = wait.until(EC.element_to_be_clickable(element_locator))

    # Нажать на элемент
    element.click()

    element_locator = (By.XPATH,
                       "//a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8' and p[@class='BurgerIngredient_ingredient__text__yp3dH' and text()='Соус Spicy-X']]")

    # Ожидание появления элемента и его сделанный клик
    wait = WebDriverWait(browser, 10)
    element = wait.until(EC.element_to_be_clickable(element_locator))
    element.click()

    # Определение локатора элемента
    element_locator = (By.XPATH, "//p[@class='text text_type_main-medium mb-8' and text()='Соус Spicy-X']")

    # Ожидание появления элемента
    wait = WebDriverWait(browser, 10)
    element = wait.until(EC.presence_of_element_located(element_locator))
    assert element.is_displayed()

#Проверка перехода в раздел начинки
def test_tab_navigation_fillings(browser, home_page):
    browser.get(home_page)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.url_to_be(f'{home_page}/'))

    # Определение локатора элемента
    element_locator = (By.XPATH, "//span[@class='text text_type_main-default' and text()='Начинки']")

    # Ожидание появления элемента
    wait = WebDriverWait(browser, 10)
    element = wait.until(EC.element_to_be_clickable(element_locator))

    # Нажатие на элемент
    element.click()

    # Определение локатора элемента
    element_locator = (By.XPATH,
                       "//img[contains(@class, 'BurgerIngredient_ingredient__image__3e-07') and contains(@class, 'ml-4') and contains(@class, 'mr-4') and @src='https://code.s3.yandex.net/react/code/meat-02.png']")

    # Ожидание появления элемента
    wait = WebDriverWait(browser, 10)
    element = wait.until(EC.element_to_be_clickable(element_locator))

    # Нажатие на элемент
    element.click()

    # Определение локатора элемента
    element_locator = (
    By.XPATH, "//p[@class='text text_type_main-medium mb-8' and text()='Мясо бессмертных моллюсков Protostomia']")

    # Ожидание появления элемента
    wait = WebDriverWait(browser, 10)
    element = wait.until(EC.presence_of_element_located(element_locator))

    # Выполнение assert, проверяющего отображение элемента
    assert element.is_displayed()

