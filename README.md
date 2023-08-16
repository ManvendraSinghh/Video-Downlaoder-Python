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
✦ **_Easy Video Downloading_**: Download single videos or entire playlists effortlessly.  
✦ **_Lofi-Themed UI_**: The UI design carries a soothing Lofi vibe, inspired by the creator's development journey accompanied by Lofi songs. 🎶🎨  
✦ **_Playlist Enhancements_**: Each video downloaded from a playlist is prefixed with a sequence number for easy organization.  
✦ **_Music-Only Downloads_**: Download audio tracks from videos to create your personal music library.  
✦ **_Multi-threading Enabled_**: Download up to 4 videos in parallel, optimizing your download time.  


# Technologies Used:
✦ **_Python_**: The backbone of the application.  
✦ **_Tkinter_**: Creating the user-friendly graphical interface.  
✦ **_Pytube_**: Handling YouTube video downloads efficiently.  


# How to Use:
✦ Launch the application.  
✦ Enter the URL of the video or playlist you want to download.  
✦ Choose your desired options: individual video, entire playlist, music-only, etc.  
✦ Sit back and relax as LofiTunes works its magic! 🎶✨  


# Installation:
✦ Clone this repository to your local machine.  
✦ Ensure you have Python and the required libraries (Tkinter, Pytube) installed.  
✦ Run the main script to start using LofiTunes YouTube Downloader.  


# Contribution:
Contributions are welcome! Whether you want to add features, fix bugs, or improve the UI, feel free to submit a pull request.

# Future Enhancements:
✦ Support for additional video platforms.  
✦ Enhanced playlist handling and sorting options.  
✦ User-customizable themes and UI presets.  

Download your favorite videos and tunes in style with LofiTunes YouTube Downloader. Spread the Lofi vibes! 🎶📽️
