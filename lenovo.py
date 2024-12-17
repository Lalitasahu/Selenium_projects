from selenium import webdriver
from selenium.webdriver.common.by import By 
import pandas as pd

driver = webdriver.Firefox(executable_path='/Users/apple/Downloads/geckodriver')
url = 'https://www.lenovo.com/us/en/laptops/subseries-results?visibleDatas=993:Work'
driver.get(url)
driver.page_source
# print(data)
# id = products[product].get('id')
#             name = products[product].get('productName')
#             pro_url = 'https://www.lenovo.com/us/en'+products[product].get('url')
#             pro_code = products[product].get('productCode')
#             price = products[product].get('miniPrice')
#             ratingStar = products[product].get('ratingStar')
#             commentCount = products[product].get('commentCount')
#             marketingShortDescription = products[product].get('marketingShortDescription')
#             image = 'https:'+products[product].get('media').get('listImage')[0].get('imageAddress')
# driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")# for the sroldown 
# driver.find_element(By.XPATH,'//button[@class = "evidon-banner-acceptbutton"]').click
products = driver.find_elements(By.XPATH,'//li[@class = "product_item product_item_PC product_item_22TP2X1X1T1   product_reverse"]')
for product in products:
    Pro_id = product.find_element(By.XPATH,'//span[@class = ""]')
    Name = product.find_element(By.XPATH,'//a[@class= "lazy_href"]')
    # print(Pro_id.text)
    # print(Name.text)
    data ={
        'Pro_id':Pro_id,
        'Name':Name
    }
    print(data)