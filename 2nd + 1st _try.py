import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm',
        'preferredquality': '320',
    }],
}

def download_song(song_name, artist):
    search_query = song_name + " " + artist
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_query])

# Example usage
download_song("https://youtu.be/6CqXgs-7ico", "Queen") 
