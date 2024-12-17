from selenium import webdriver
from selenium.webdriver.common.by import By 
driver = webdriver.Firefox(executable_path='/Users/apple/Downloads/geckodriver')
url = 'https://www.shoptime.com.br/categoria/games/g/marca-ps5'
driver.get(url)
# driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
# print(driver)
products = driver.find_elements(By.XPATH,'//div[@class="src__Wrapper-sc-1l8mow4-0 fsViFX"]')
for i in products:
    Title = i.find_element(By.XPATH,'.//h3')
    # ListPrice = i.find_element(By.XPATH,'.//sapn[@class="src__Text-sc-154pg0p-0 price__Price-sc-h6xgft-0 JbUli"]')
    # salePrice = i.find_element(By.XPATH,'.//span[@class="src__Text-sc-154pg0p-0 price__PromotionalPrice-sc-h6xgft-1 ctBJlj price-info__ListPriceWithMargin-sc-1xm1xzb-2 liXDNM"]').text
    discount = i.find_element(By.XPATH,'.//span[@class="discount-badge__Text-sc-s5bp91-2 YfKws"]')
    # installment = i.find_element(By.XPATH,'.//span[@class="installment__InstallmentUI-sc-1g296bd-0 fNXtFB"]')
    
    # data= {
    #     'Title':Title.text,
    #     'ListPrice':ListPrice.text,
    #     'salePrice':salePrice.text,
    #     'discount':discount.text,
    #     'installment':installment.text
    # }
    print(discount)