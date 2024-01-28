# YouTube Downloader
This Python script allows users to download YouTube videos, audio, or entire playlists using the Pytube library. Users can choose from various options, including video download, audio download, or playlist download.


## Requirements
 - Pytube
Install Pytube using:

```bash
  pip install pytube
```
## Usage
##### 1.Run the script: python youtube_downloader.py.
##### 2.Enter your choice:
 - 1: Download a video.
 - 2: Download audio.
 - 3: Download a playlist.
 - 4: Exit.

 ## Features
- **Download Video:** Users can provide a YouTube video link and choose from available video streams to download.

- **Download Audio:** Users can input a YouTube video link to download the audio stream only.

- **Download Playlist:** Users can enter a YouTube playlist link, and the script will download all videos in the playlist.

- **Exit:** Allows the user to exit the program.

## Examples

**Downloading a Video**

```bash
Enter What you want to Download:
1. Video
2. Audio
3. Playlist
4. Exit
Enter your choice (1/2/3/4): 1

Enter the YouTube video link: [Insert video link]
Title: [Video Title]
[Available Video Streams]
Enter the index of the video stream to download: [Selected Index]
Video Downloaded Successfully
```

**Downloading a Audio**

```bash
Enter What you want to Download:
1. Video
2. Audio
3. Playlist
4. Exit
Enter your choice (1/2/3/4): 2

Enter the YouTube video link for audio: [Insert video link]
Title: [Video Title]
[Available Audio Streams]
Enter the index of the audio stream to download: [Selected Index]
Audio Downloaded Successfully
```

**Downloading a Playlist**

```bash
Enter What you want to Download:
1. Video
2. Audio
3. Playlist
4. Exit
Enter your choice (1/2/3/4): 3

Enter the YouTube playlist link: [Insert playlist link]
Title: [Playlist Title]
[Downloading each video in the playlist...]
Playlist Downloaded Successfully
```

##
Feel free to customize this documentation according to your needs and provide more details if necessary. Also, ensure to include the appropriate license file in your repository.

