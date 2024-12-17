from selenium import webdriver
from selenium.webdriver.common.by import By 
import pandas as pd

driver = webdriver.Firefox(executable_path='/Users/apple/Downloads/geckodriver')
url = 'https://www.coupang.com/np/categories/497135?page=17'
driver.get(url)
driver.page_source
# total_items = int(driver.find_element(By.XPATH,'//h2[@class = "category-list-title"]').text.replace(' Items',''))//60
total_items = driver.find_elements(By.XPATH,'//ul[@id="productList"]//li')
l = []
for i in total_items:
    # item = i.text   
     
    Name = i.find_element(By.XPATH,'.//div[@class="name"]').text
    Image = i.find_element(By.XPATH,'.//dt[@class="image"]//img').get_attribute('src')
    link = i.find_element(By.XPATH,'.//a[@class="baby-product-link"]').get_attribute('href')
    price = i.find_element(By.XPATH,'.//strong[@class="price-value"]').text
    
    data = {
            'Name':Name,
            'Image':Image,
            'link':link,
            'price':price,
        }
    l.append(data)
    print(data)
df=pd.DataFrame(l)
df.to_excel('coupang_laptop_17_.xlsx',index=False)

