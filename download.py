import csv

flag = 0
Song_name = "Tunak Tunak tun" 
Artist = "Dhaler Mehndi"
field_names = ["desire_choice_link","Artist_Name","Song_name"]
name_song = Song_name + ' by ' + Artist
search_string = name_song
search_string = search_string.replace(' ', '+')
desire_choice = 1

while desire_choice > 3 or desire_choice < 1:
    desire_choice = input("\n1 ,2 or 3? :")
    desire_choice = int(desire_choice)
desire_choice_link = "/watch?v=vTIIMJ9tUc8" 
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
    if desire_choice_link.lower() == row[0].lower():
        flag = 1
        print("\n\t That version is already present.. Sure want to download it again?\n")
        print(row)
        sure_var = input("\ny or n?")
        if sure_var.lower() == 'y':
            break
        elif sure_var.lower() == 'n':
            pass
        else:
            print("\nIllegal Choice... Avoiding download. Try Again.")




#now actual downloading code begins from yt5s.io
# driver = webdriver.Chrome(executable_path=path_driver)

print("\n\tDownload Successful")
field_names = ["desire_choice_link","Artist_Name","Song_name"]
if flag == 0:
    with open(r'C:\Users\sande\Desktop\mail_delete\downloaded_songs\f_english.csv', 'a+', newline= '') as csv_file:
        dict_object = csv.DictWriter(csv_file, fieldnames=field_names) 
        dict_object.writerow(dict)