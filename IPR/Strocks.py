from selenium import webdriver
import json
import time
import math

options = webdriver.ChromeOptions()
chrome_driver_binary = 'C:\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(chrome_driver_binary)

link = "https://ru.investing.com/equities/russia"

class Stocks:

    def __init__(self, id, name, price, link):
        self.id = id
        self.name = name
        self.price = price
        self.link = link

    def __str__(self):
        return "Stock: id = {}, name = {}, price = {}".format(self.id, self.name, self.price) #f"Stock: id = {self.id}, name = {}self.name, price = {self.price}]"

    def pars(self, pars):
        self.pars = driver.find_element_by_xpath(f'//*[@id="cross_rate_markets_stocks_1"]/tbody/')


driver.get(link)
all_stock = []

count_tr = driver.find_elements_by_xpath('//*[@id="cross_rate_markets_stocks_1"]//tbody//tr')

for i in range(1, 5): #len(count_tr)+1):
    name = driver.find_element_by_xpath(f'//*[@id="cross_rate_markets_stocks_1"]/tbody/tr[{i}]/td[2]').text
    price = driver.find_element_by_xpath(f'//*[@id="cross_rate_markets_stocks_1"]/tbody/tr[{i}]/td[3]').text
    link = driver.find_element_by_xpath(f'//*[@id="cross_rate_markets_stocks_1"]/tbody/tr[{i}]/td[2]/a').get_attribute('href')
    id_s = driver.find_element_by_xpath(f'//*[@id="cross_rate_markets_stocks_1"]/tbody/tr[{i}]').get_attribute('id')[5:]
    stock = Stocks(id_s, name, price, link)
    all_stock.append(stock)

for stock in all_stock:
    print(stock)

driver.quit()

