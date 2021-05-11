from pytube import YouTube
link = input("https://www.youtube.com/watch?v=2mNNwzslyPo")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()
