from time import sleep
from chromedrive.chromedriver import ChromeDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


def baixa_dataset():
    driver = ChromeDriver().driver()
    driver.get('https://coronavirus.es.gov.br/painel-covid-19-es')

    btn_download_csv = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div[3]/div/article/div/div/div/div/div/div[1]/p/a[1]')))

    btn_download_csv.click()

    #Espera o download por 8 minutos
    sleep(420)

    driver.close()
