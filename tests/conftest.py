from selenium import webdriver
import pytest

from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture
def get_chrome_options():
    """"
    В этом методе настройки запуска вебдрайвера

    chrome: выводит браузер, так как он выглядит
    """
    options = chrome_options()
    options.add_argument('chrome')  # Use headless if you do not need a browser UI
    options.add_argument('--start-maximized')  # Starts the browser maximized, regardless of any previous settings.
    options.add_argument('--window-size=1650,900')  # Sets the initial window size. Provided as string in the format "800,600".
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options) # usr->local->bin if any locations, you need "use executable_path='locate'"
    return driver


@pytest.fixture(scope='function')  # function: the default scope, the fixture is destroyed at the end of the test.
def setup(request, get_webdriver):
    """
    Хранит ссылку на сайт
    если наш реквест который пойдет и посмотрит не являются ли наши тесты в классе
    Если класс, то даем драйвер
    Если нет, то мы заходим в наш юрл
    Возвращаем наш драйвер
    Закрываем наш драйвер(закроет окно брайзера)
    """
    driver = get_webdriver
    url = 'https://www.next.us/en'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()  # The driver.close() command is used to close the current browser window having focus.
    # The driver.quit() is used to quit the whole browser session along with all the associated browser windows,
    # tabs and pop-ups.



