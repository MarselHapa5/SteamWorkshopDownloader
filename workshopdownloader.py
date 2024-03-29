import os

filePath = input("Введите путь до директории с SteamCMD: ")
print("Введите название исполняемого файла SteamCMD")
steamcmdName = input("(С расширением): ")
gameId = input("Введите ID игры или приложения: ")


os.chdir(filePath)
while True:
    print(" ")
    modIdWSymb = input("Введите ссылку на мод в мастерской: ")
    modId = modIdWSymb.replace("https://steamcommunity.com/sharedfiles/filedetails/?id=", "")
    os.system(f"{steamcmdName} +login anonymous +workshop_download_item {gameId} {modId} +quit")
    