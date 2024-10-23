import Scripts.youtubeDL as ytdl
import Scripts.Demucs as SD
import re

output_dir="./output"
def demucs_playlist(playlist_url):
    videoids=ytdl.get_playlist_videoids(playlist_url)
    count=0
    for videoid in videoids:
        url = "https://www.youtube.com/watch?v="+videoid
        temp_movie_datas=SD.make_kalyoke(url, output_dir, count)
        count+=1

def demucs_single(url):
    videoid=extract_video_id(url)
    SD.make_kalyoke(url, output_dir, 0)

def extract_video_id(url):
    # YouTubeのURLからvideoIDを抽出する正規表現パターン
    pattern = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        print("URLからvideoIDを抽出できませんでした。")
        return None

# demucs_playlist("https://www.youtube.com/playlist?list=PLYHLBKVhYyzm9F6qVJlXys8PlPbIoajmD")
# demucs_single("https://www.youtube.com/watch?v=0ozI_3vFPiU")
# ytdl.download_mp3("https://www.youtube.com/watch?v=pmLBczbj7do",output_dir)
ytdl.download_mp3_playlist("https://www.youtube.com/playlist?list=PLbV-A4O8NMU1JtfJJYwM0_B9wdvNazqXs", output_dir)
# ytdl.download_mp4_with_info("https://www.youtube.com/watch?v=jzi6RNVEOtA",output_dir)