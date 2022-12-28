from selenium import webdriver
import json
import time
import math

options = webdriver.ChromeOptions()
chrome_driver_binary = 'C:\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(chrome_driver_binary)

link = "https://ru.investing.com/equities/russia"

def find_div():
    div_list = []
    try:
        div = driver.find_element_by_xpath("//*[@data-test='dividend']/div/span").text
        div_list.append(div)
    except:
        div = driver.find_element_by_xpath("//*[@data-test='dividend']/div").text
        div_list.append(div)
    return div_list

driver.get(link)

stocks = {}
all_div_list = []
list_link = []
name_list = []
price_list = []

for i in range(1, 42):
    name = driver.find_element_by_xpath(f'//*/table/tbody/tr[{i}]/td[2]').text
    price = driver.find_element_by_xpath(f'//*/table/tbody/tr[{i}]/td[3]').text
    link = driver.find_element_by_xpath(f'//*/table/tbody/tr[{i}]/td[2]/a').get_attribute('href')
    name_list.append(name)
    price_list.append(price)
    list_link.append(link)


# stocks_json = json.dumps(stocks, ensure_ascii=False)
# with open("stocks.json", "w") as my_file:
#     my_file.write(stocks_json)
# print('Запись завершена')

for i in list_link:
    driver.get(i)
    all_div_list.extend(find_div())

for i in range(len(name_list)):
    stocks[name_list[i]] = [price_list[i], all_div_list[i]]


print(stocks)
# for i in all_div_list:
#     print(i)

driver.quit()

