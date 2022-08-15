import youtube_dl

link = input("Enter link: ")

entered_link = [link]

options = {
    "format": "bestaudio/best",
    "extractaudio": True,
    "audioformat": "mp3",
    "noplaylist": True,
    "outtmpl": "%(id)s",
}
with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download(entered_link)