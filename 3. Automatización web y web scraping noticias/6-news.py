from importlib.resources import path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = "https://www.thesun.co.uk/sport/football/"
path = "C:/Users/Carlos Giles/Documents/Herramientas/chromedriver"

service=Service(executable_path=path)
driver=webdriver.Chrome(service=service)
driver.get(website)