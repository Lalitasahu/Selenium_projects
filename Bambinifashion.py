from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
driver = webdriver.Firefox(executable_path='/Users/apple/Downloads/geckodriver')
url = 'https://bambinifashion.com/girl'
driver.get(url)
driver.page_source

nextpage = True
while nextpage:
    time.sleep(5)
    product = driver.find_elements(By.XPATH,'//div[@class = "category-list-product has-size-tooltip product-card"]')
    for i  in product:
        name = i.find_element(By.XPATH,'.//div[@class = "product-card-title"]')
        price = i.find_element(By.XPATH,'.//div[@class = "product-price product-card-price"]')
        print(name.text,price.text)
        nextpage = driver.find_element(By.XPATH,'//li[@class = "pagination-item--next"]')
        # while nextpage:
        #     if nextpage:
        if nextpage:
            accept_buton = driver.find_element(By.XPATH,'//button[@class="gdpr-sheet-cta"]')
            if accept_buton:
                accept_buton.click()
            nextpage.click()
            driver.refresh()
        else:
            nextpage = False