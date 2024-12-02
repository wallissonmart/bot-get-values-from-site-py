import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

options = FirefoxOptions()
options.add_argument('-headless')

driver = webdriver.Firefox(options=options)

data = []

driver.get("https://www.magazineluiza.com.br/selecao/ofertasdodia/?filters=promotion---promocao_sazonal_2")

time.sleep(2)

products = driver.find_elements(By.CSS_SELECTOR, "li.sc-iNIeMn")

for product in products:
    try:
        title = product.find_element(By.CSS_SELECTOR, "h2[data-testid='product-title']").text
    except Exception as e:
        title = None

    try:
        price = product.find_element(By.CSS_SELECTOR, "p[data-testid='price-value']").text
    except Exception as e:
        price = None

    try:
        link = product.find_element(By.CSS_SELECTOR, "a[data-testid='product-card-container']").get_attribute("href")
    except Exception as e:
        link = None

    if title and price and link:
        data.append({"title": title, "price": price, "link": link})

print(data)

driver.quit()
