import time
from selenium import webdriver 
from selenium.webdriver.common.by import By

list = []
driver = webdriver.Chrome()

driver.get("https://jp.finalfantasyxiv.com/lodestone/worldstatus/")

#getした要素の配列(可否)
elems = driver.find_elements(by=By.XPATH, value="//div[@class = 'world-list__create_character']/i")

#getした要素の配列(鯖名)
servers = driver.find_elements(by=By.XPATH, value="//div[@class = 'world-list__world_name']/p")



#配列の各要素ごとに出力
for elem in elems:
    elem = elem.get_attribute("data-tooltip")
    list.append(elem)
    
print(list[24])
driver.quit()
