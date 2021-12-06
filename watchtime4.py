from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/c/Coffee%E6%9E%97%E8%8A%8A%E5%A6%A4yoga/videos?view=0&sort=p&flow=grid")
element = driver.find_elements_by_xpath('//*[@class="yt-simple-endpoint style-scope ytd-grid-video-renderer"]')
href=[]
con=[]
for i in range(10):
    h = element[i].get_attribute('href')
    c = element[i].get_attribute('text')
    href.append(h)
    con.append(c)
f1 = open('href4.txt','w', encoding='utf8')
f2 = open('text4.txt','w', encoding='utf8')
for j in range(10):
    f1.write(href[j])
    f1.write("\n")
    f2.write(con[j])
    f2.write("\n")
f1.close()
f2.close()
driver.quit()