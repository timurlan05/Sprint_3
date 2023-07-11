from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pages import LoginPage
import pytest
from data import password_reg, incorrect_password, home_page

# Регистрация и вход
def test_login_page(browser, email):
    email, name = email
    login_page = LoginPage(browser)
    browser.get(home_page)
    login_page.register(name, email)
    login_page.login(email, password_reg)
    login_page.click_button_lk()
    email_value = login_page.element_email_lk()
    expected_email = email
    assert email_value == expected_email, f"Expected email: {expected_email}, Actual email: {email_value}"

# Некорректный пароль при регистарции
def test_incorrect_password(browser, email):
    email, name = email
    login_page = LoginPage(browser)
    browser.get(home_page)
    login_page.register(name, email, incorrect_password)
    text = login_page.incorrect_password()
    expected_text = "Некорректный пароль"
    assert text == expected_text

# вход по кнопке «Войти в аккаунт» на главной
def test_login_main_page(browser, email):
    email, name = email
    login_page = LoginPage(browser)
    browser.get(home_page)
    login_page.register(name, email, password_reg)
    browser.get(f'{home_page}')
    login_page.click_button()
    login_page.login(email, password_reg)
    login_page.click_button_lk()
    email_value = login_page.element_email_lk()  # логин указанный в личном кабитене после авторизации
    expected_email = email  # логин при регистрации
    assert email_value == expected_email, f"Expected email: {expected_email}, Actual email: {email_value}"

# вход через кнопку «Личный кабинет»
def test_login_lk_page(browser, email):
    email, name = email
    login_page = LoginPage(browser)
    browser.get(home_page)
    login_page.register(name, email, password_reg)
    browser.get(f'{home_page}')
    login_page.click_button_lk()
    login_page.login(email, password_reg)
    login_page.click_button_lk()
    email_value = login_page.element_email_lk()  # логин указанный в личном кабитене после авторизации
    expected_email = email  # логин при регистрации
    assert email_value == expected_email, f"Expected email: {expected_email}, Actual email: {email_value}"

# вход через кнопку в форме регистрации
def test_login_registr_page(browser, email):
    email, name = email
    login_page = LoginPage(browser)
    browser.get(home_page)
    login_page.register(name, email, password_reg)
    browser.get(f"{home_page}/register")
    button = browser.find_element_by_link_text("Войти").click()
    login_page.login(email, password_reg)
    login_page.click_button_lk()
    email_value = login_page.element_email_lk()  # логин указанный в личном кабитене после авторизации
    expected_email = email  # логин при регистрации
    assert email_value == expected_email, f"Expected email: {expected_email}, Actual email: {email_value}"

# вход через кнопку в форме восстановления пароля
def test_login_forgot_password_page(browser, email):
    email, name = email
    login_page = LoginPage(browser)
    browser.get(home_page)
    login_page.register(name, email, password_reg)
    browser.get(f"{home_page}/forgot-password")
    button = browser.find_element_by_link_text("Войти").click()
    login_page.login(email, password_reg)
    login_page.click_button_lk()
    email_value = login_page.element_email_lk()  # логин указанный в личном кабитене после авторизации
    expected_email = email  # логин при регистрации
    assert email_value == expected_email, f"Expected email: {expected_email}, Actual email: {email_value}"

# Переход в личный кабинет
def test_login_page(browser, email):
    email, name = email
    login_page = LoginPage(browser)
    browser.get(home_page)
    login_page.register(name, email, password_reg)
    login_page.login(email, password_reg)
    login_page.click_button_lk()
    email_value = login_page.element_email_lk() # логин указанный в личном кабитене после авторизации
    expected_email = email # логин при регистрации
    assert email_value == expected_email, f"Expected email: {expected_email}, Actual email: {email_value}"

#Переход из личного кабинета в конструктор
def test_login_page(browser, email):
    email, name = email
    login_page = LoginPage(browser)
    browser.get(home_page)
    login_page.register(name, email, password_reg)
    login_page.login(email, password_reg)
    login_page.click_button_lk()
    login_page.wait.until(EC.url_to_be(f"{home_page}/account/profile"))
    login_page.click_constructor_button()
    login_page.wait.until(EC.url_to_be(f"{home_page}/"))
    assert browser.current_url == f"{home_page}/"

# Выход из аккаунта
def test_exit_account(browser, email):
    email, name = email
    login_page = LoginPage(browser)
    browser.get(home_page)
    login_page.register(name, email, password_reg)
    login_page.login(email, password_reg)
    login_page.click_button_lk()
    login_page.wait.until(EC.url_to_be(f"{home_page}/account/profile"))
    login_page.click_button_exit()
    login_page.wait.until(EC.url_to_be(f'{home_page}/login'))
    login_page.click_link()
    login_page.wait.until(EC.url_to_be(f'{home_page}/register'))
    assert browser.current_url == f"{home_page}/register"

# Проверка раздела Булки
def test_tab_navigation_bulki(browser):
    login_page = LoginPage(browser)
    browser.get(home_page)
    login_page.wait.until(EC.url_to_be(f'{home_page}/'))
    element_locator = login_page.bulka_element_locator
    element = login_page.wait.until(EC.element_to_be_clickable(element_locator)).click()
    element_locator = login_page.bulka_text_element_locator
    element = login_page.wait.until(EC.visibility_of_element_located(element_locator)).click()
    element_locator = login_page.modal_element_locator
    element = login_page.wait.until(EC.visibility_of_element_located(element_locator))
    assert element.is_displayed()

# Проверка раздела Соусы
def test_tab_navigation_sauce(browser):
    login_page = LoginPage(browser)
    browser.get(home_page)
    login_page.wait.until(EC.url_to_be(f'{home_page}/'))
    element_locator = login_page.sauce_tab_element_locator
    element = login_page.wait.until(EC.element_to_be_clickable(element_locator)).click()
    element_locator = login_page.spicy_x_sauce_element_locator
    element = login_page.wait.until(EC.element_to_be_clickable(element_locator)).click()
    element_locator = login_page.spicy_x_sauce_text_element_locator
    element = login_page.wait.until(EC.presence_of_element_located(element_locator))
    assert element.is_displayed()

# Проверка раздела Начинки
def test_tab_navigation_fillings(browser):
    login_page = LoginPage(browser)
    browser.get(home_page)
    login_page.wait.until(EC.url_to_be(f'{home_page}/'))
    element_locator = login_page.fillings_tab_element_locator
    element = login_page.wait.until(EC.element_to_be_clickable(element_locator)).click()
    element_locator = login_page.meat_fillings_element_locator
    element = login_page.wait.until(EC.element_to_be_clickable(element_locator)).click()
    element_locator = login_page.meat_fillings_text_element_locator
    element = login_page.wait.until(EC.presence_of_element_located(element_locator))
    assert element.is_displayed()
