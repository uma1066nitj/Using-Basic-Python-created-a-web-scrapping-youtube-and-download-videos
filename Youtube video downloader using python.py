from pytube import YouTube

link = input("Enter link of youtube video: ")
yt = YouTube(link)

#title of video
print("Title: ",yt.title)

#to get number of views
print("No of views: ",yt.views)

#to get length of video
print("Length: ", yt.length)

#to get description about video
print("Description: ",yt.description)

#to get rating
print("Rating: ",yt.rating)


#to download the video with highest resolution

stream = yt.streams.get_highest_resolution()
stream.download()
print("Download Completed!!")