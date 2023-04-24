# type: ignore
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Links úteis:
# https://peter.sh/experiments/chromium-command-line-switches/
# https://selenium-python.readthedocs.io/

# caminho do driver e pasta raíz
ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXE = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'


# configuração básica do Selenium
def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(executable_path=str(CHROMEDRIVER_EXE))

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options,
    )

    return browser


if __name__ == '__main__':
    TIME_TO_WAIT = 10

    # exemplo de options:
    # options = ('--disable-gpu', '--no-sandbox',)
    options = ()

    # executa funcao
    browser = make_chrome_browser(*options)
    browser.get('https://www.google.com/')

    # esperar para encontrar o input
    search_box = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')
        )
    )

    # digitar na search box e pressiona enter
    search_box.send_keys('Hello World!')
    search_box.send_keys(Keys.ENTER)

    # busca por elementos (links - tag name <a> (HTML))
    results = browser.find_element(By.ID, 'search')
    links = results.find_elements(By.TAG_NAME, 'a')
    links[0].click()

    # sleep 10seg
    sleep(TIME_TO_WAIT)
