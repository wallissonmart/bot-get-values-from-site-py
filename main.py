import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions

options = EdgeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Edge(options=options)

valores_passados = []

driver.get("https://www.zoom.com.br/notebook/notebook-gamer-acer-aspire-nitro-5-an515-57-52lc-intel-core-i5-11400h-15-6-8gb-ssd-512-gb-windows-11-geforce-gtx-1650?_lc=88&searchterm=acer%20%20nitro%20")

time.sleep(1)

previous = driver.find_element(
    By.CSS_SELECTOR, "#__next > div.ProductPageBody_ContentBody__De_1M > div.ProductPageBody_GraySection__31ulA > div.ProductPageBody_BlockSectionWrapper__BK4Qx.container-lg > div > div > section.BlockSection_BlockSection__frjNL.OffersListSection_BlockSection__T5HZT.OffersListSection_OffersListSection__NNIAM.BlockSection_BlockSection--AlwaysOpen__c_PI0 > div")

values = previous.find_elements(
    By.CSS_SELECTOR, ".Text_Text__h_AF6.Text_MobileHeadingS__Zxam2")

for v in values:
    if v.text != "":
        valores_passados.append(v.text.split("à")[0])

# print(valores_passados[::-1])
print(valores_passados)

driver.quit()
