from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# driver = webdriver.Firefox(executable_path='Selenium_projects /chromedriver')
driver = webdriver.Firefox(executable_path='geckodriver.log')
url = 'https://www.amazon.com/s?k=Shoes&rh=p_36%3A-5000&_encoding=UTF8&content-id=amzn1.sym.b0c3902d-ae70-4b80-8f54-4d0a3246745a&crid=1QEZIUFPCL3YZ&pd_rd_r=01e5c7b9-56cc-4480-98d5-eff91ef45249&pd_rd_w=k5YZ5&pd_rd_wg=IaFs8&pf_rd_p=b0c3902d-ae70-4b80-8f54-4d0a3246745a&pf_rd_r=BZNQAGAQQZ6C1N4CD7QW&qid=1684823927&rnid=2661611011&sprefix=shoes%2Caps%2C145&ref=pd_gw_unk'
driver.get(url)
time.sleep(5)
driver.page_source
product = driver.find_elements(By.XPATH,'//div[@class = "sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 AdHolder sg-col s-widget-spacing-small sg-col-4-of-20"]')
data = {}
l = []
for i in product:
    link = i.find_element(By.XPATH,'.//d[@class ="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]').get_attribute('href')
    name = i.find_element(By.XPATH,'.//span[@class = "a-size-base-plus a-color-base a-text-normal"]').text
    # price = i.find_element(By.XPATH,'.//span[@class = "a-offscreen"]').text
    price = i.find_element(By.XPATH,'.//div[@class = "a-row"]//a//span[@class = "a-price"]//span[@class ="a-offscreen"]]').text
    # no_OF_Comment = i.find_element(By.XPATH,'.//sapn[@class = "aria-label"]').text
    # stars = i.find_element(By.XPATH,'.//span[@class ="d-icon-alt"]').text
    stars = i.find_element(By.XPATH,'.//div[@class = "a-section a-spacing-small puis-padding-left-small puis-padding-right-small"]//div[@class ="a-section a-spacing-none a-spacing-top-micro"]//span//a//i//span[@class="a-icon-alt"]').text
    dis = find_element(By.XPATH,'.//div[@class = "a-section a-spacing-small puis-padding-left-small puis-padding-right-small"]//div[@class ="a-section a-spacing-none a-spacing-top-micro"]//span//a//i//span[@class="a-icon-alt"]').click
    
    data = {
        'link':link,
        'name':name,
        'price':price,
        # 'no_OF_Comment':no_OF_Comment,
        'stars':stars
    }
    print(data)
driver.close()