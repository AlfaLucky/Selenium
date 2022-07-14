from selenium import webdriver
import pytest

from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture
def get_chrome_options():
    """"
    In this method, configure the launch of the webdriver

    chrome: renders the browser as it looks
    """
    options = chrome_options()
    options.binary_location = '/usr/bin/google-chrome'
    options.add_argument('--no-sandbox')  # Use headless if you do not need a browser UI
    options.add_argument('--headless')
    options.add_argument('--start-maximized')  # Starts the browser maximized, regardless of any previous settings.
    options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--window-size=1650,900')  # Sets the initial window size. Provided as string in the format "800,600".
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options) # usr->local->bin if any locations, you need "use executable_path='locate'"
    return driver


@pytest.fixture(scope='function')  # function: the default scope, the fixture is destroyed at the end of the test.
def setup(request, get_webdriver):
    """
    Stores messages on the site
      if our request goes and sees if our tests are in the class
      If the class, then we give the driver
      If not, then we go to our yurl
      Returns our driver
      Close our driver (will close the browser window)
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
