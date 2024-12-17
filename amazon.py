from selenium import webdriver
from selenium.webdriver.common.by import By 
driver = webdriver.Firefox(executable_path='/Users/apple/Downloads/geckodriver')
# url = 'https://www.amazon.com/s?k=Shoes&rh=p_36%3A-5000&_encoding=UTF8&content-id=amzn1.sym.b0c3902d-ae70-4b80-8f54-4d0a3246745a&crid=1QEZIUFPCL3YZ&pd_rd_r=01e5c7b9-56cc-4480-98d5-eff91ef45249&pd_rd_w=k5YZ5&pd_rd_wg=IaFs8&pf_rd_p=b0c3902d-ae70-4b80-8f54-4d0a3246745a&pf_rd_r=BZNQAGAQQZ6C1N4CD7QW&qid=1684823927&rnid=2661611011&sprefix=shoes%2Caps%2C145&ref=pd_gw_unk'
url ='https://www.meesho.com/women-clothing/pl/hizpr'
print(driver.get(url))
