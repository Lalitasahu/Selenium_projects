from selenium import webdriver
from selenium.webdriver.common.by import By 
driver = webdriver.Firefox(executable_path='/Users/apple/Downloads/geckodriver')
url = 'https://www.clovia.com/bras/s/'
driver.get(url)
alldata = driver.page_source
# scroldown = driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")# for the sroldown 
# if scroldown:
name = driver.find_elements(By.XPATH,'//ul[@class = "listNone imglist p0 m0 list_view"]//li//div[@class = "catName"]')
# for i in products:
    # name = i.find_element(By.XPATH,'.//div[@class = "catName"]').text
# else:
    # name = ''
print(name)