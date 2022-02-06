from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium.webdriver.common.proxy import Proxy, ProxyType
from config import *

BROWSER = config["browser"]["name"]
HEADLESS = config["browser"]["headless"]

def get_web_driver(proxy: str=None):
    if BROWSER == "chrome":
        capabilities = webdriver.DesiredCapabilities.CHROME
    elif BROWSER == "firefox":
        capabilities = webdriver.DesiredCapabilities.FIREFOX

    if HEADLESS:
        capabilities
    if proxy:
        p=Proxy()
        p.proxyType=ProxyType.MANUAL
        p.add_to_capabilities(capabilities)


    if BROWSER == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=capabilities)
    elif BROWSER == "firefox":
        driver = webdriver.Chrome(GeckoDriverManager().install(), desired_capabilities=capabilities)

    return driver



    driver.get("https://www.unieuro.it/")
    driver.fullscreen_window()
    sleep(5)
    driver.quit()



if __name__ == "__main__":
    get_web_driver()

