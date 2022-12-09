#Install pacakge 
#pip install pytube

#import library
import pytube

#Take link
link = input('Enter video Link :')


#store this value into yt_link
yt_link = pytube.YouTube(link)

#yt_link.streams.first().download()
#enter resoulation of file
yt_link.streams.get_highest_resolution().download()
print("Download",link)