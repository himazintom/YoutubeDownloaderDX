import yt_dlp
import os
import time
import Scripts.DeleteStringForFiles as dsf
import Scripts.folder_sets as fs

def get_video_duration(youtube_url):
    with yt_dlp.YoutubeDL() as ydl:
        info = ydl.extract_info(youtube_url, download=False)
        duration=info["duration"]
        return duration

def get_video_title(youtube_url):
    with yt_dlp.YoutubeDL() as ydl:
        info = ydl.extract_info(youtube_url, download=False)
        duration=info["title"]
        return duration
    
def download_mp3_with_info(youtube_url, output_dir, retries=3, delay=5):
    out_dir = output_dir or "./output"
    os.makedirs(out_dir, exist_ok=True)
    ydl_opts = {
        "quiet": True,
        "format": "bestaudio/best",
        "outtmpl": f"{out_dir}/%(id)s.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }]
    }
    for attempt in range(retries):
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(youtube_url, download=True)
                return info
        except yt_dlp.utils.DownloadError as e:
            print(f"エラーが発生しました: {e}. {delay}秒後に再試行します。")
            time.sleep(delay)
    return None
    
def download_mp4_with_info(youtube_url, output_dir):
    out_dir = output_dir or "./output"
    os.makedirs(out_dir, exist_ok=True)
    ydl_opts = {
        "quiet": True,
        "outtmpl": f"{out_dir}/%(id)s.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegVideoConvertor",
            "preferedformat": "mp4"
        }]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=True)
        return info

  
def get_playlist_videoids(playlist_url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(playlist_url, download=False)
            if 'entries' in info:
                video_ids = [video_data['id'] for video_data in info['entries']]
            else:
                video_ids = []  # 'entries'キーが存在しない場合は空のリストを返す
            playlist_title = info.get('title', 'unknown_playlist')  # プレイリストのタイトルを取得
    except yt_dlp.utils.DownloadError as e:
        print(f"エラーが発生しました: {e}")
        video_ids = []  # エラーが発生した場合は空のリストを返す
        playlist_title = 'unknown_playlist'
    return {"video_ids": video_ids, "playlist_title": playlist_title}

def download_mp3_playlist(playlist_url, output_dir):
    playlist_data = get_playlist_videoids(playlist_url)
    video_ids=playlist_data["video_ids"]
    print("video_ids",video_ids)
    _output_dir=f"{output_dir}/{playlist_data["playlist_title"]}"
    for video_id in video_ids:
        url = "https://www.youtube.com/watch?v=" + video_id
        if download_mp3(url, _output_dir)=="":
            continue

def download_mp3(url,output_dir):
    movie_info = download_mp3_with_info(url, output_dir)
    if movie_info is None:
        return ""
    movie_name = movie_info["title"]
    file_music_name = dsf.sanitize_filename(movie_name)
    movie_id = movie_info["id"]
    movie_extractor = movie_info["extractor_key"]
    sinput_path = f"{output_dir}/{movie_id}.mp3"
    soutput_dir = f"{output_dir}/{file_music_name}"
    
    fs.rename_file(sinput_path, f"{soutput_dir}.mp3")
  
# with yt_dlp.YoutubeDL() as ydl:
#     info = ydl.extract_info("https://www.youtube.com/watch?v=uAqITu9ypDo", download=False)
#     with open('info.txt', "w", encoding='utf-8') as file:
#         file.write(pformat(info))

