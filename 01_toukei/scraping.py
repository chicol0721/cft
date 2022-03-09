###########################################
# ちんこ
# ページ内の全試合の情報をCSVに出力
#
#
###########################################
import time
from selenium import webdriver 

startyear = 2020 #開始年
endyear = 2021   #終了年
list = []
driver = webdriver.Chrome()

#for year in range(startyear, endyear+1):
#    for month in range(1,13):
#        time.sleep(5)
#driver.get("https://race.netkeiba.com/top/calendar.html?pid=race_calendar&year="+str(year)+"&month="+str(month))
driver.get("https://race.netkeiba.com/top/calendar.html?pid=race_calendar&year=2020&month=12")

        #getした要素の配列
elems = driver.find_elements_by_xpath("//td[@class='RaceCellBox']") #("//a[@href]")
        #配列の各要素ごとに出力
print(elems)
driver.quit()