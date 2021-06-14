from pytube import YouTube

url="https://www.youtube.com/watch?v=jNQXAC9IVRw"
my_video=YouTube(url)

print(my_video.title)
print(my_video.thumbnail_url)

my_video=my_video.streams.get_highest_resolution()
# for stream9 in my_video.streams:
#     print(stream9)
my_video.download()