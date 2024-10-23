# YouTube Downloader & Audio Separator using YT-dlp and Demucs

This Python project allows you to download audio and video from YouTube using [YT-dlp](https://github.com/yt-dlp/yt-dlp), and it can also perform audio separation using [Demucs](https://github.com/facebookresearch/demucs). It supports downloading individual videos, entire playlists, and extracting MP3 files. You can optionally separate audio into different stems (e.g., vocals, drums) using Demucs.

## Features
- **Download MP3 files** from YouTube videos or playlists.
- **Download MP4 videos** with video information.
- **Audio Separation**: Use Demucs to split audio into separate stems such as vocals, drums, bass, etc.
- **Playlist Support**: Process entire playlists for audio download and separation.

## Requirements
- Python 3.x
- YT-dlp
- Demucs
- ffmpeg (for audio and video processing)
- Other required libraries (listed in `requirements.txt`)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install `ffmpeg`** (Required for audio and video processing):
   - For Windows, download from [FFmpeg.org](https://ffmpeg.org/download.html) and add it to your system's PATH.
   - For Linux/macOS, use your package manager:
     ```bash
     # Ubuntu/Debian
     sudo apt install ffmpeg
     
     # macOS
     brew install ffmpeg
     ```

4. **Install `Demucs`**:
   ```bash
   pip install demucs
   ```

## Usage

### 1. Download and Separate Audio from a YouTube Playlist

This function will download all videos from a YouTube playlist, convert them to MP3, and optionally use Demucs to separate the audio stems.

```python
demucs_playlist("https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID")
```

### 2. Download and Separate Audio from a Single YouTube Video

You can download and separate audio from a single YouTube video using the following function:

```python
demucs_single("https://www.youtube.com/watch?v=YOUR_VIDEO_ID")
```

### 3. Download MP3 from a YouTube Playlist

This function downloads only MP3 files from a playlist without performing any separation.

```python
ytdl.download_mp3_playlist("https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID", output_dir)
```

### 4. Download MP4 with Video Info

To download an MP4 video along with its metadata (such as title, description, etc.), use this:

```python
ytdl.download_mp4_with_info("https://www.youtube.com/watch?v=YOUR_VIDEO_ID", output_dir)
```

## Functions Overview

- **`demucs_playlist(playlist_url)`**: Downloads all videos from a playlist and separates the audio using Demucs.
- **`demucs_single(url)`**: Downloads a single video and separates the audio using Demucs.
- **`extract_video_id(url)`**: Extracts the video ID from a YouTube URL.
- **`ytdl.download_mp3_playlist(playlist_url, output_dir)`**: Downloads MP3 files from a YouTube playlist.
- **`ytdl.download_mp4_with_info(video_url, output_dir)`**: Downloads an MP4 video along with its metadata.

## Notes
- Ensure that `ffmpeg` is installed and accessible via your system's PATH.
- Demucs is used for audio separation and might require high computational resources depending on the size of the audio files.

## License
This project is licensed under the MIT License.

---

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgments
- [YT-dlp](https://github.com/yt-dlp/yt-dlp) for providing a powerful YouTube downloader.
- [Demucs](https://github.com/facebookresearch/demucs) for their state-of-the-art audio separation model.

---

This template should be a good start for your project documentation. You can adjust it according to your specific needs.