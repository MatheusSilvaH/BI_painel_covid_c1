from logging import info
from pathlib import Path

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import SessionNotCreatedException


class ChromeDriver:
    __driver: webdriver.Chrome

    def _init_(self, root_dir: str):
        self.profile = None
        self.__chrome_options = Options()
        self.__root_dir = root_dir
        # self.__chrome_options.add_experimental_option('debuggerAddress', f'localhost:{port}')

        # Configuration para caminho de download de arquivo por click.
        self.__prefs = {"download": {
            "default_directory": str(Path(self.__root_dir, 'downloads')),
            "directory_upgrade": True,
            "extensions_to_open": "",
            "prompt_for_download": False
        }, "plugins.always_open_pdf_externally": True}

    def driver(self) -> webdriver.Chrome:
        try:
            chromedriver_autoinstaller.install()
            options = Options()
            options.add_argument("--start-maximized")
            # options.add_argument(r"--user-data-dir=C:\Users\rpa\AppData\Local\Google\Chrome\User Data")
            # options.add_experimental_option("prefs", self.__prefs)

            driver = webdriver.Chrome(options=options)

        except SessionNotCreatedException:
            raise Exception('Versão do Chrome incompatível com a do driver')

        except Exception:
            raise Exception('Não foi possível inicializar o Chrome Driver do Selenium')

        else:
            info('Sessão do Chrome iniciada com sucesso!')

            return driver
