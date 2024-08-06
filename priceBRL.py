from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
from datetime import datetime

def config_webdriver():
    # Opções de configuração do driver
    options_webdriver = [
    '--block-new-web-contents',
    '--disable-notifications',
    '--no-default-browser-check',
    '--lang=pt-BR',
    '--headless',
    '--window-position=36,68',
    '--window-size=1100,850',]
    
    # Configura o WebDriver
    options = Options()
    options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])
    for option in options_webdriver:
        options.add_argument(option)
        
    # Inicializa o Webdriver
    driver = webdriver.Chrome(options=options)
    return driver
    
def format_date():
    date_today = datetime.now()
    date_today = date_today.strftime("%d-%m-%Y %H:%M:%S")
    
    date_today = date_today.replace(":", '')
    date_today = date_today.replace(" ", '-')
    
    return date_today

def price_dolar_brl():
    price_brl = 'text-success' 
    link = 'https://wise.com/br/currency-converter/usd-to-brl-rate?amount=1'   
    
    # Configura e inicializa o webdriver
    driver = config_webdriver()
    driver.get(link)
    
    # Pega o valor do Real
    value_brl = driver.find_element(By.CLASS_NAME, price_brl).text
    date = format_date()
    
    # Cria um diretorio para salvar as screenshots
    if os.path.isdir(f'{os.getcwd()}/screenshot'): 
        driver.save_screenshot(f"{os.getcwd()}/screenshot/{date}.png")
    else:
        os.mkdir('screenshot')
        driver.save_screenshot(f"{os.getcwd()}/screenshot/{date}.png")
    
    return value_brl, date      