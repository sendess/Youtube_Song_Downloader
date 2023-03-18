import youtube_dl
import requests
from pydub import AudioSegment

def download_song(song_name, artist, language, folder):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'aac',
            'preferredquality': '128',
        }],
        'default_search': 'ytsearch',
        'outtmpl': folder + '/%(title)s.%(ext)s',
    }

    search_query = song_name + " " + artist
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            result = ydl.extract_info(search_query, download=True)
        except youtube_dl.utils.DownloadError as e:
            print(e)
            return

        if 'title' not in result:
            print("Video not found")
            return

        audio_file = result['title'] + '.' + result['ext']
        audio = AudioSegment.from_file(audio_file, format=result['ext'][1:])
        audio.export(
            audio_file,
            format='aac',
            tags={
                'artist': artist,
                'title': song_name,
                'genre': language,
            },
        )

# Example usage
# download_song("Bohemian Rhapsody", "Queen", "English", "./English Songs")


# download_song("Kun faya kun", "A.R. Rahman", "English", "./English Songs")

download_song("Tunak Tunak Tun", "Daler Mehdi", "Hindi", "./Hindi Songs")
