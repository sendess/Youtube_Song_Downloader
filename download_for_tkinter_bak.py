from selenium import webdriver
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time
import sys

# import tqdm #for loading meter at download
#menu
# show menu to user and figure out whats the purpose
# options will be
# input from user
#   genre input 1 English  or 2 Nepali  or 3 Hindi  or other (separate csv for each)
#   check if the song is in csv 
#   if yes, then tell already downloaded
#   if not, proceed to download into genre folder and add to csv
#
# download link direct via link to a remaining folder

def download_song(Song_name, Artist):#parameter artist ra song name pass garna baaki
    name_song = Song_name + ' by ' + Artist
    path_driver = r"C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=path_driver)
    driver.maximize_window()
    search_string = name_song
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
    # print(res)#for checking if res ma data aaira cha ki nai, if in case id haru change vayera content vetna sakena
    res = res [:3]
    result_dict = {}
    for r in res:
        res2 = r.find("a",attrs = key2 , href = True)
        temp = res2["href"]
        temp2 = str(res2.text)
        temp2 = temp2.replace("\n","")
        result_dict[temp2] = temp
    
    print("\n\t Displaying your results here...\n \t\t Which is your desired media?\n")
    title_result = list(result_dict.keys())
    print(title_result)
    set = [0,1,2]

    for i in set:
        print(str(i+1) + " --- " +title_result[i])
    # flush_temp_ip = input()
    sys.stdin.flush()
    desire_choice = input("\n1 ,2 or 3? :")
    desire_choice = int(desire_choice)

    while desire_choice > 3 or desire_choice < 1:
        desire_choice = input("\n1 ,2 or 3? :")
        desire_choice = int(desire_choice)
    desire_choice_link = list(result_dict.values())[int(desire_choice)-1]  

    # print(title_result[desire_choice-1] + " on " + desire_choice_link) #code while debugging
    # driver.close()

    #now actual downloading code begins from yt5s.io
    # driver = webdriver.Chrome(executable_path=path_driver)
    driver.maximize_window()
    mp3_download_link = "https://mp3fromyou.tube/file/mp3"
    desire_choice_link = desire_choice_link.replace("watch?v=","")
    driver.get(mp3_download_link + desire_choice_link)
    time.sleep(3)

#for the previous (1st) site was plaanning to use 
    # search_box = driver.find_element(By.ID, "s_input")
    # search_box.send_keys(desire_choice_link)    
    # search_box.send_keys(Keys.ENTER)
    # time.sleep(5)
    # select = Select(driver.find_element(By.ID, "formatSelect"))
    # select.select_by_index(0)
    # time.sleep(1)

    driver.find_element(By.ID, "btn-0").click()
    time.sleep(10)
    
    print("\n\tDownload Successful")
    while(True):
        pass
    driver.close()


def display_genre_coding():
    # os.system('cls')
    print("\n`````````````````````````Song downloader`````````````````````````")
    print("\nMethod  :  Input name of song")
    print("\n\tGenre listing:\n\t\t")
    print("\t\t1 == English")
    print("\t\t2 == Nepali")
    print("\t\t3 == Hindi")
    print("\t\t4 == Other")
    return 0

def download_english():
    Song = input("Enter the Song Title:  ")
    Artist = input ("Enter the Artist's Name:  ")
    field_names = ['Song_Name','Artist_Name']
    
    dict = {
        'Song_Name' : Song,
        'Artist_Name' : Artist
    }
    ## Find the data in csv file
    csv_file_1 = csv.reader(open(r'C:\Users\sande\Desktop\mail_delete\downloaded_songs\english.csv', "r+"), delimiter=",") 
    #loop through the csv list
    print(csv_file_1)
    for row in csv_file_1:
        if Song.lower() == row[0].lower() and Artist.lower() == row [1].lower():
            print("\n\t Already in list., check csv file. \n")
            print (row)
            time.sleep(3)
            show_menu()
    ##Write in csv
    with open(r'C:\Users\sande\Desktop\mail_delete\downloaded_songs\english.csv', 'a+', newline= '') as csv_file:
        dict_object = csv.DictWriter(csv_file, fieldnames=field_names) 
        dict_object.writerow(dict)
       
    download_song(Song, Artist)
    return 0

def download_nepali():

    return 0

def download_hindi():

    return 0    

def download_other():

    return 0

def song_name():
    display_genre_coding()
    choice = input("\nEnter your choice: ")
    if choice == '1':
        download_english()
    elif choice == '2':
        download_nepali()
    elif choice == '3':
        download_hindi()
    elif choice == '4':
        download_other()    
    else:
        # os.system('cls')
        print("\n\n\t\tPlease enter valid input !!")
        time.sleep(2)
        song_name()

def show_menu():
    print("\n`````````````````````````Song downloader`````````````````````````")
    print("\n````````````````````````````Options:`````````````````````````````")
    print("\n````1.Input name of song")
    print("\n````2.Download from url")
    print("\n````3.Exit")
    choice = input("\nEnter your choice: ")
    if choice == '1':
        song_name()
    return 0

def main():
    show_menu()

if __name__ == "__main__":
    main()