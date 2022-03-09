###########################################
# うんこ
# カレンダーの全日程を確認し、取得すべきリンク先をリストに格納
#
#
###########################################
import time
from selenium import webdriver 

startyear = 2020 #開始年
endyear = 2021   #終了年
list = []
driver = webdriver.Chrome()

for year in range(startyear, endyear+1):
    for month in range(1,2):
        time.sleep(5)
        driver.get("https://race.netkeiba.com/top/calendar.html?pid=race_calendar&year="+str(year)+"&month="+str(month))

        #getした要素の配列
        elems = driver.find_elements_by_xpath("//a[@href]")

        #配列の各要素ごとに出力
        for elem in elems:
            href = elem.get_attribute("href")
            if "race/sum" in href or "race_list.html" in href: #2010年くらいを境にリンクの表現が変わっていたのでOR条件で補完
                list.append(href)

print(list)
driver.quit()