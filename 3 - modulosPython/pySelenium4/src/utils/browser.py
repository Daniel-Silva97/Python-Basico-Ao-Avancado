from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Caminho para a raiz do projeto
# Parent volta uma pasta igual ao (../)
ROOT_FOLDER = Path(__file__).parent.parent.parent
# print(ROOT_FOLDER)
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'bin' / 'chromedriver.exe'


# print(CHROME_DRIVER_PATH)

# Instanciando o Chrome
def makeChromeBrowser(*options: str) -> webdriver.chrome:
    # Chamando o chromeOptions
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)
        # Criando o serviço do Chrome com o caminho do ChromeDriver
        chrome_service = Service(
            executable_path=CHROME_DRIVER_PATH
        )
    # Criando o browser com as opçoes e serviço configurado
    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )
    # Retorno o resultado
    return browser


if __name__ == '__main__':
    options = ('--disable-gpu', '--no-sandbox')  # Criando options de exemplo
    browser = makeChromeBrowser(*options) # instanciando com as options que criei acima

    # Utilizando o selenium
    browser.get('https://www.google.com/')
    inputElement = browser.find_element(by=By.NAME, value='q')
    inputElement.send_keys('Selenium')
    inputElement.send_keys(Keys.ENTER)
    sleep(5)
    browser.quit()
