from selenium import webdriver
from selenium.webdriver.common.by import By 
import pandas as pd

driver = webdriver.Firefox(executable_path='/Users/apple/Downloads/geckodriver')
url = 'https://bambinifashion.com/boy/shoes-1'
driver.get(url)
driver.page_source
total_items = int(driver.find_element(By.XPATH,'//h2[@class = "category-list-title"]').text.replace(' Items',''))//60
l = []        
for i in range(total_items+1):
    product = driver.find_elements(By.XPATH,'//div[@class = "category-list-product has-size-tooltip product-card"]')
    for i  in product:
        name = i.find_element(By.XPATH,'.//div[@class = "product-card-title"]')
        price = i.find_element(By.XPATH,'.//div[@class = "product-price product-card-price"]')
        # print(name.text,price.text)
        data = {
            'name':name.text,
            'price':price.text,
        }
        l.append(data)
        print(data)
df=pd.DataFrame(l)
df.to_excel('Bambinifasiobs.xlsx',index=False)
