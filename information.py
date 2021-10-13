from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
#1
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/channel/UCFd-9jAfbuUjwDZjisOwv1w/videos")
element = driver.find_elements_by_xpath('//*[@class="yt-simple-endpoint style-scope ytd-grid-video-renderer"]')
href=[]
con=[]
for i in range(10):
    h = element[i].get_attribute('href')
    c = element[i].get_attribute('text')
    href.append(h)
    con.append(c)
f1 = open('href.txt','w', encoding='utf8')
f2 = open('text.txt','w', encoding='utf8')
for j in range(10):
    f1.write(href[j])
    f1.write("\n")
    f2.write(con[j])
    f2.write("\n")
f1.close()
f2.close()
driver.quit()
