import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from test import data

@pytest.fixture
def browser():
    # Создание экземпляра веб-драйвера Chrome
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.set_window_size(1920, 1080)
    # Открытие URL-адреса
    browser.get(f"{data.home_page}/")
    # Ожидание загрузки страницы (максимум 10 секунд)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.url_to_be(f"{data.home_page}/"))
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






