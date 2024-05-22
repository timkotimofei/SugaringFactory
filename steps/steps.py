from time import sleep
from behave import step
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker


# @step('Open "{url}" url')
# def open_url(context, url):
#     context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     context.driver.maximize_window()
#     context.driver.get(url)
#
#


@step('Open "{url}" url')
def open_url(context, url):
    # Создаем опции для Chrome
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,  # Отключаем службу учетных данных
        "profile.password_manager_enabled": False,  # Отключаем менеджер паролей
        "autofill": {"enabled": False},  # Отключаем автозаполнение
        "profile.default_content_settings.popups": 0,  # Отключаем попапы
        "profile.default_content_setting_values.notifications": 2,  # Отключаем уведомления
        "profile.default_content_setting_values.automatic_downloads": 1  # Разрешение автоматических загрузок
    })
    chrome_options.add_argument("--disable-popup-blocking")  # Отключаем блокировку всплывающих окон
    chrome_options.add_argument("--disable-save-password-bubble")  # Отключение всплывающего окна сохранения пароля

    # Инициализация WebDriver с указанными опциями
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    context.driver.maximize_window()
    context.driver.get(url)

@step('Open "{env}" environment')
def open_env(context, env):
    """
    Open environment in browser by the dict and run def open_url(context, url)
    :param context:
    :param env:
    :return:
    """
    environments = {
        'prod': 'https://lifetwig.com/',
        'staging': 'https://test.sugaringfactory.com/index.php?route=account%2Flogin',
        'dev': 'development.lifetwig.com',
        'uat': 'uat.lifetwig.com',
        'sug_main': 'https://test.sugaringfactory.com/',
        'sug_login': 'https://test.sugaringfactory.com/index.php?route=account%2Flogin'
    }

    open_url(context, environments[env])


@step('Wait for "{timeout}" seconds')
def wait_sec(context, timeout):
    sleep(int(timeout))


@step('Page contains element "{xpath}"')
def page_contains_element(context, xpath):
    """
    Here I check if the element is present in the page.
    I have timeout  and trigger TimeoutException to run assert message
    :param context:
    :param xpath:
    :return:
    """
    try:
        element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, f"{xpath}")))
        assert element, f"Element with xpath {xpath} is not found"
    except TimeoutException:
        assert False, f"Element with xpath {xpath} is not found within the given time"


@step('Verify "{page_name}" page is exists')
def verify_page_exists(context, page_name):
    """
    Here I check if the page exists. By creating the dict with some pages and xPath
    At the end I check if the page exists by the run def page_contains_element(context, xpath)
    :param context:
    :param page_name:
    :return:
    """
    pages = {
        'login': "//h1[contains(text(), 'Account Login')]",
        'my account': "//h1[contains(text(), 'My Account')]",
        'suga_login': "//h2[contains(text(), 'Returning Customer')]",
        'sug_forgot_pass': "//a[contains(text(), 'Forgotten Password')]",
        'app_sugar': "//a[contains(text(), 'Edit Account')]"
    }
    page_contains_element(context, pages[page_name])


@step('Click on element "{xpath}"')
def click_element(context, xpath):
    try:
        element = WebDriverWait(context.driver, 7).until(EC.element_to_be_clickable((By.XPATH, f"{xpath}")))
    except TimeoutException:
        raise AssertionError(f"Element with xpath {xpath} is not found")
    element.click()


@step('Type "{text}" in field "{xpath}"')
def type_in(context, text, xpath):
    elements = context.driver.find_elements(By.XPATH, f"{xpath}")
    assert elements, f"Element with xpath {xpath} is not found"
    elements[0].send_keys(text)


@step('Login as "{role}"')
def step_impl(context, role):
    credentials = {
        'admin': ('pcs.automationclass+10@gmail.com', '!Qwerty7890'),
        'tester': ('timkotimofeytest@gmail.com', '12345'),
        'user': ('qwertyuiop@yahoo.com', 'Sotirov1!'),
        'tester@artem': ('testforlifetwig.com@gmail.com', ''),
    }

    if role == 'admin':
        type_in(context, credentials[role][0], "//input[@id='login_email']")
        type_in(context, credentials[role][1], "//input[@id='login_password']")
        click_element(context, "//span[text()='Login']")
    elif role == 'tester':
        type_in(context, credentials[role][0], "//input[@name='email']")
        type_in(context, credentials[role][1], "//input[@name='password']")
        click_element(context, "//div[@class='login-buttons']/a[@class='button-cont-right']")

    elif role == 'tester@artem':
        type_in(context, credentials[role][0], "//input[@name='email']")
        sleep(int(3))
        click_element(context, "//span[contains(text(), 'Continue')]")


@step('Scroll to element "{xpath}"')
def scroll_to_element(context, xpath):
    element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, f"{xpath}")))
    context.driver.execute_script("arguments[0].scrollIntoView(true);", element)


@step('Type random "{field}" to "{xpath}"')
def type_random_name(context, field, xpath):
    fake = Faker('En')
    data_dict = {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'company': fake.company(),
        'address_1': fake.address(),
        'address_2': fake.address(),
        'city': fake.city(),
        'postcode': fake.postcode(),
        'email': fake.email()
    }
    if field == 'first_name':
        type_in(context, data_dict['first_name'], xpath)
    elif field == 'last_name':
        type_in(context, data_dict['last_name'], xpath)
    elif field == 'company':
        type_in(context, data_dict['company'], xpath)
    elif field == 'address_1':
        type_in(context, data_dict['address_1'], xpath)
    elif field == 'address_2':
        type_in(context, data_dict['address_2'], xpath)
    elif field == 'city':
        type_in(context, data_dict['city'], xpath)
    elif field == 'postcode':
        type_in(context, data_dict['postcode'], xpath)


