from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Use Service object for geckodriver
service = Service('/Users/apple/Downloads/geckodriver')
driver = webdriver.Firefox(service=service)

url = 'https://www.myntra.com/towel-set'
driver.get(url)

# Initialize empty list to store product data
l = []

# Loop through pagination
nextpage = True
while nextpage:
    # Wait for the product list to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//li[@class="product-base"]'))
    )
    
    # Get all products on the current page
    all_product = driver.find_elements(By.XPATH, '//li[@class="product-base"]')
    for i in all_product:
        try:
            Title = i.find_element(By.XPATH, './/h4[@class="product-product"]').text
        except:
            Title = " "
        try:
            Product_link = i.find_element(By.XPATH,'.//a').get_attribute('href')
        except:
            Product_link = ''
        
        try:
            Product_brand = i.find_element(By.XPATH,'.//h3[@class= "product-brand"]').text
        except:
            Product_brand = " "
        
        try:
            Product_Dis_price = i.find_element(By.XPATH,'.//div[@class="product-price"]//span[@class="product-discountedPrice"]').text
        except:
            Product_Dis_price = ''

        d = {
            'Title': Title,
            'Product_link':Product_link,
            'Product_brand':Product_brand,
            'Product_Dis_price':Product_Dis_price
        }
        l.append(d)
        print(l)

    # Check if "Next" button is available and enabled
    try:
        next_button = driver.find_element(By.XPATH, '//li[@class="pagination-next"]')
        if next_button.is_enabled():
            next_button.click()
        else:
            nextpage = False
    except Exception as e:
        # If no "Next" button, stop the loop
        print(f"No next button found: {e}")
        nextpage = False

# Convert list to DataFrame and export to Excel
df = pd.DataFrame(l)
df.to_excel('myntra_Selenium1.xlsx', index=False)

# Close the driver
driver.quit()
