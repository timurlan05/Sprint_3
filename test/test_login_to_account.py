from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pages import LoginPage

import time

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


