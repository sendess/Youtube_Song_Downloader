from selenium import webdriver
import time
import csv
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.common import options
import time
# from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time
import sys
import os


def download_song(Song_name, Artist ,Language, flag):
    name_song = Song_name + ' by ' + Artist
    path_driver = r"C:\Program Files (x86)\chromedriver.exe"

    chromeOptions = webdriver.ChromeOptions()
    Download_Location = "D:\\Songs\\" + Language
    prefs = {"download.default_directory" : Download_Location}
    chromeOptions.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(executable_path=path_driver, options=chromeOptions)

    driver.minimize_window()
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
    # print(title_result)
    set = [0,1,2]

    for i in set:
        print(str(i+1) + " --- " +title_result[i])

    sys.stdin.flush()
    desire_choice = input("\n1 ,2 or 3? :")
    desire_choice = int(desire_choice)

    while desire_choice > 3 or desire_choice < 1:
        desire_choice = input("\n1 ,2 or 3? :")
        desire_choice = int(desire_choice)
    desire_choice_link = list(result_dict.values())[int(desire_choice)-1]  
    #pass till here


    dict = {
        "desire_choice_link" : desire_choice_link,
        'Artist_Name' : Artist,
        "Song_name" : Song_name
    }
    ## Find the data in csv file
    csv_file_1 = csv.reader(open(r'C:\Users\sande\Desktop\mail_delete\downloaded_songs\english.csv', "r+"), delimiter=",") 
    #loop through the csv list
    for row in csv_file_1:
        if desire_choice_link == row[0]:
            flag = 2
            print("\n\t That version is already present.. Sure want to download it again?\n")
            print(row)
            sure_var = input("\ny or n?")
            if sure_var.lower() == 'y':
                break
            elif sure_var.lower() == 'n':
                pass
            else:
                print("\nIllegal Choice... Avoiding download. Try Again.")
            time.sleep(3)
            show_menu()
    




    #now actual downloading code begins from yt5s.io
    # driver = webdriver.Chrome(executable_path=path_driver)
    mp3_download_link = "https://mp3fromyou.tube/file/mp3"
    desire_choice_link = desire_choice_link.replace("watch?v=","")
    driver.get(mp3_download_link + desire_choice_link)
    time.sleep(3)

    driver.find_element(By.ID, "btn-0").click()
    time.sleep(10)
    
    print("\n\tDownload Successful")
    driver.close()
    field_names = ["desire_choice_link","Artist_Name","Song_name"]
    if flag == 0:
        with open(r'C:\Users\sande\Desktop\mail_delete\downloaded_songs\f_english.csv', 'a+', newline= '') as csv_file:
            dict_object = csv.DictWriter(csv_file, fieldnames=field_names) 
            dict_object.writerow(dict)
    return flag

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

    already_download_flag = 0
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
    for row in csv_file_1:
        if Song.lower() == row[0].lower() and Artist.lower() == row [1].lower():
            already_download_flag = 1
            print("\n\t Already in list., check csv file. Are you Sure download again?\n")
            print(row)
            sure_var = input("\ny or n?")
            if sure_var.lower() == 'y':
                break
            elif sure_var.lower() == 'n':
                pass
            else:
                print("\nIllegal Choice... Avoiding download. Try Again.")
            time.sleep(3)
            show_menu()
    state = download_song(Song, Artist, "English",already_download_flag)
    if already_download_flag == 0:
        with open(r'C:\Users\sande\Desktop\mail_delete\downloaded_songs\english.csv', 'a+', newline= '') as csv_file:
            dict_object = csv.DictWriter(csv_file, fieldnames=field_names) 
            dict_object.writerow(dict)
    return 0

def download_nepali():
    already_download_flag = 0
    Song = input("Enter the Song Title:  ")
    Artist = input ("Enter the Artist's Name:  ")
    field_names = ['Song_Name','Artist_Name']
    
    dict = {
        'Song_Name' : Song,
        'Artist_Name' : Artist
    }
    ## Find the data in csv file
    csv_file_1 = csv.reader(open(r'C:\Users\sande\Desktop\mail_delete\downloaded_songs\nepali.csv', "r+"), delimiter=",") 
    #loop through the csv list
    for row in csv_file_1:
        if Song.lower() == row[0].lower() and Artist.lower() == row [1].lower():
            already_download_flag = 1
            print("\n\t Already in list., check csv file. Are you Sure download again?\n")
            print (row)
            sure_var = input("\ny or n?")
            if sure_var.lower() == 'y':
                break
            elif sure_var.lower() == 'n':
                pass
            else:
                print("\nIllegal Choice... Avoiding download. Try Again.")
            time.sleep(3)
            show_menu()
    download_song(Song, Artist, "Nepali")
    if already_download_flag == 0:
        with open(r'C:\Users\sande\Desktop\mail_delete\downloaded_songs\nepali.csv', 'a+', newline= '') as csv_file:
            dict_object = csv.DictWriter(csv_file, fieldnames=field_names) 
            dict_object.writerow(dict)
    return 0

def download_hindi():
    already_download_flag = 0
    Song = input("Enter the Song Title:  ")
    Artist = input ("Enter the Artist's Name:  ")
    field_names = ['Song_Name','Artist_Name']
    
    dict = {
        'Song_Name' : Song,
        'Artist_Name' : Artist
    }
    ## Find the data in csv file
    csv_file_1 = csv.reader(open(r'C:\Users\sande\Desktop\mail_delete\downloaded_songs\hindi.csv', "r+"), delimiter=",") 
    #loop through the csv list
    for row in csv_file_1:
        if Song.lower() == row[0].lower() and Artist.lower() == row [1].lower():
            already_download_flag = 1
            print("\n\t Already in list., check csv file. Are you Sure download again?\n")
            print (row)
            sure_var = input("\ny or n?")
            if sure_var.lower() == 'y':
                break
            elif sure_var.lower() == 'n':
                pass
            else:
                print("\nIllegal Choice... Avoiding download. Try Again.")
            time.sleep(3)
            show_menu()
    download_song(Song, Artist, "Hindi")
    if already_download_flag == 0:
        with open(r'C:\Users\sande\Desktop\mail_delete\downloaded_songs\hindi.csv', 'a+', newline= '') as csv_file:
            dict_object = csv.DictWriter(csv_file, fieldnames=field_names) 
            dict_object.writerow(dict)
    return 0    

def download_other():
    already_download_flag = 0
    Song = input("Enter the Song Title:  ")
    Artist = input ("Enter the Artist's Name:  ")
    field_names = ['Song_Name','Artist_Name']
    
    dict = {
        'Song_Name' : Song,
        'Artist_Name' : Artist
    }
    ## Find the data in csv file
    csv_file_1 = csv.reader(open(r'C:\Users\sande\Desktop\mail_delete\downloaded_songs\other.csv', "r+"), delimiter=",") 
    #loop through the csv list
    for row in csv_file_1:
        if Song.lower() == row[0].lower() and Artist.lower() == row [1].lower():
            already_download_flag = 1
            print("\n\t Already in list., check csv file. Are you Sure download again?\n")
            print (row)
            sure_var = input("\ny or n?")
            if sure_var.lower() == 'y':
                break
            elif sure_var.lower() == 'n':
                pass
            else:
                print("\nIllegal Choice... Avoiding download. Try Again.")
            time.sleep(3)
            show_menu()
    download_song(Song, Artist, "Other")
    if already_download_flag == 0:
        with open(r'C:\Users\sande\Desktop\mail_delete\downloaded_songs\other.csv', 'a+', newline= '') as csv_file:
            dict_object = csv.DictWriter(csv_file, fieldnames=field_names) 
            dict_object.writerow(dict)
    return 0

def from_csv():   #csv wala pachi halamla too much lang lang
    

    return 1

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
    os.system('clear')
    print("\n`````````````````````````Song downloader`````````````````````````")
    print("\n````````````````````````````Options:`````````````````````````````")
    print("\n````1.Input name of song")
    print("\n````2.Download from csv")
    print("\n````3.Exit")
    choice = input("\nEnter your choice: ")
    if choice == '1':
        song_name()
    if choice == '3':
        from_csv()
    return 0

def main():
    show_menu()

if __name__ == "__main__":
    main()