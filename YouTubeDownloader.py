import pytube
import os

iURL = input("Please enter the URL: ")

while True:
    choice = input("Would you like to run stream or download? or type 'exit' to quit: ")
    if choice.lower() == "stream":
        print("Script starting... ")
        youtube = pytube.YouTube(iURL)
        streams = youtube.streams.all()
        for i in streams:
            print(i)
        HDStream = youtube.streams.get_highest_resolution()
        print("This is the highest resolution: \n", HDStream)
    elif choice.lower() == "download":
        itag = int(input("Please enter the itag number: "))
        video = youtube.streams.get_by_itag(itag)
        string = str(os.path.splitext("""insert PATH of where you want the video downloaded here in quotes""")[0])
        print("video found starting download...")
        video.download(string)
        print('video downloaded')
    elif choice.lower() == "exit":
        quit()