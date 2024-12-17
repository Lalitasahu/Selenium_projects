from selenium import webdriver
from selenium.webdriver.common.by import By 
driver = webdriver.Firefox(executable_path='/Users/apple/Downloads/geckodriver')

def listpage():
    url = 'https://www.fnp.com/gifts-bestsellers-lp?utm_source=insider_popup&utm_medium=popup_mobile&utm_campaign=bestsellers_exit15_14feb2023'
    driver.get(url)
    # driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    has_nxt = True
    while has_nxt:
        for i in driver.find_elements(By.XPATH,'//div[@class = "product-card_product-title__32LFp"]'):
            name = i.text
        
            print(name)
        # try:
        #     driver.execute_script("window.scrollTo(0, 3095);")
        # except:
        #     has_nxt = False
listpage()