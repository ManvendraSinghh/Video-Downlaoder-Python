# Video-Downlaoder-Python-GUI-Based

![image](https://github.com/ManvendraSinghh/Video-Downlaoder-Python/assets/117578356/4f2adb8f-8e62-44ce-a8aa-3cceeabec9df)


# !! Important Note !! 
There is a bug in the recent update of PyTube so we have to make slight changes for it to work.
In order to solve the problem of 
" __init__: could not find match for ^\w+\W ", 
you have to edit a line in cipher.py file which is located in

C:\Users\#####\AppData\Local\Programs\Python\Python311\Lib\site-packages\pytube\cipher.py
 
replace the line 30, which is:

var_regex = re.compile(r"^\w+\W")

with this line :

var_regex = re.compile(r"^\$*\w+\W")

It will work again.

# GUI Based Video Downloader Python 🎵📽️
It is a Python-based graphical user interface (GUI) application designed to make downloading YouTube videos a breeze. With a touch of Lofi inspiration in its UI, this tool offers a seamless experience for downloading both individual videos and playlists from YouTube. 🎧🎬

# Features:
**_Easy Video Downloading_**: Download single videos or entire playlists effortlessly.__
**_Lofi-Themed UI_**: The UI design carries a soothing Lofi vibe, inspired by the creator's development journey accompanied by Lofi songs. 🎶🎨__
**_Playlist Enhancements_**: Each video downloaded from a playlist is prefixed with a sequence number for easy organization.__
**_Music-Only Downloads_**: Download audio tracks from videos to create your personal music library.__
**_Multi-threading Enabled_**: Download up to 4 videos in parallel, optimizing your download time.__


# Technologies Used:
**_Python_**: The backbone of the application.__
**_Tkinter_**: Creating the user-friendly graphical interface.__
**_Pytube_**: Handling YouTube video downloads efficiently.__


# How to Use:
Launch the application.__
Enter the URL of the video or playlist you want to download.__
Choose your desired options: individual video, entire playlist, music-only, etc.__
Sit back and relax as LofiTunes works its magic! 🎶✨__


# Installation:
Clone this repository to your local machine.__
Ensure you have Python and the required libraries (Tkinter, Pytube) installed.__
Run the main script to start using LofiTunes YouTube Downloader.__


# Contribution:
Contributions are welcome! Whether you want to add features, fix bugs, or improve the UI, feel free to submit a pull request.

# Future Enhancements:
Support for additional video platforms.__
Enhanced playlist handling and sorting options.__
User-customizable themes and UI presets.__

Download your favorite videos and tunes in style with LofiTunes YouTube Downloader. Spread the Lofi vibes! 🎶📽️
