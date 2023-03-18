from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

path_driver = r"C:\Program Files (x86)\chromedriver.exe"
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# song_artist = song_to_download_name + " by " + song_to_download_artist 
driver = webdriver.Chrome(executable_path=path_driver)
# driver.set_window_size(1920, 1080)
driver.minimize_window()
search_string = 'cheap thrills by sia'
search_string = search_string.replace(' ', '+')
driver.get("https://www.youtube.com/results?search_query="+ search_string + "&sp=EgIQAQ%253D%253D") 

time.sleep(7)
soup = BeautifulSoup(driver.page_source,features = "html.parser")
key1 = {
    "id" : "dismissible"
}
key2 = {
    "id" : "video-title"
}
res = soup.find_all("div", attrs = key1)
# print(res)             #for checking if res ma data aaira cha ki nai, if in case id haru change vayera content vetna sakena
res = res [:3]
result_dict = {}
for r in res:
    res2 = r.find("a",attrs = key2 , href = True)
    temp = "youtube.com"+res2["href"]
    temp2 = str(res2.text)
    temp2 = temp2.replace("\n","")
    result_dict[temp2] = temp

print("\n\t Displaying your results here...\n \t\t Which is your desired media?\n")
title_result = list(result_dict.keys())
for i in range (0,3):
    print(str(i+1) + " --- " +title_result[i])

desire_choice = input("\n1 ,2 or 3? :")
desire_choice = int(desire_choice)


while desire_choice > 3 or desire_choice < 1:
    desire_choice = input("\n1 ,2 or 3? :")
    desire_choice = int(desire_choice)
desire_choice_link = list(result_dict.values())[int(desire_choice)-1]   
# print(title_result[desire_choice-1] + " on " + desire_choice_link)
driver.close()
driver = webdriver.Chrome(executable_path=path_driver)
driver.minimize_window()
driver.get("https://yt5s.io/en5/youtube-to-mp3")
time.sleep(3)
search_box = driver.find_element(By.ID, "s_input")
search_box.send_keys(desire_choice_link)
search_box.send_keys(Keys.ENTER)
time.sleep(5)
select = Select(driver.find_element(By.ID, "formatSelect"))
select.select_by_index(0)
time.sleep(1)
driver.find_element(By.ID, "btn-action").click()
time.sleep(3)
driver.find_element(By.ID,"asuccess").click()
while(True):
    pass
driver.close()