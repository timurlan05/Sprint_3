import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    # Создание экземпляра веб-драйвера Chrome
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.set_window_size(1920, 1080)
    # Открытие URL-адреса
    browser.get("https://stellarburgers.nomoreparties.site/")
    # Ожидание загрузки страницы (максимум 10 секунд)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
    yield browser
    # Завершение работы браузера после завершения тестов
    browser.quit()


# Создание экземпляра Faker
fake = Faker()

# Фикстура для генерации случайного электронного адреса имени
@pytest.fixture
def email():
    name = fake.first_name()
    surname = fake.last_name()
    domain = "yandex.ru"
    email = f"{name.lower()}_{surname.lower()}@{domain}"
    return email, name

@pytest.fixture
def password_reg():
    passw_reg = "111111"
    return passw_reg

@pytest.fixture
def incorrect_password():
    incorrect_password = "111"
    return incorrect_password




@pytest.fixture
def home_page():
    page = "https://stellarburgers.nomoreparties.site"
    return page


