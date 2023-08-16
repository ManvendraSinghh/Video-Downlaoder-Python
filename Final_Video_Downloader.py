import re  #regular expression, mainly for use in pattern matching with strings, or string matching,i.e.  
#“find and replace”-like operations
import threading
from tkinter.filedialog import *    #to use askdirectory() so that we can get the location to save it
from tkinter import ttk  #progress bar ka use krne ke liye
from pytube import YouTube, request, Playlist
from tkinter import *
from pytube.cli import on_progress #this module contains the built in progress bar
# for creating it an EXE file
import sys
import os

from concurrent.futures import ThreadPoolExecutor # for parallel threading


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


request.default_range_size = 9437184    # this is for chunck size, 9 MegaByte size
filesize = 0

number = 1



def download_video(url,filelocation):
    global is_paused,filesize       #decalaration of variables jinko hum doosri jagah bhi use krenge
    download_video_button['state'] = 'disabled'       #ab hum iss button ko nahin use kr skte
    pause_button['state'] = 'normal'      #ab hum iss button ko use kr skte hain
    cancel_button['state'] = 'normal'     #mode- Disabled (nahin use kr skte) , Normal (use kr skte hain)
    try:
        pbar.config(value=0)
        progress['text'] = 'Downloading Video...'       #ab progress mein text change ho kr ye likh jaayega
        video=YouTube(url)
        
        progress['text']= 'downloading {}'.format(video.title)
        video.register_on_progress_callback(progress_callback)
        global yt
        yt=video.streams.filter(type='video', progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        yt.download(output_path=filelocation)
        video.register_on_complete_callback(complete_callback)      
        progress['text']= 'Done !!'
    except Exception as e:   #agar try wala na hua toh
        print(e)
        progress['text']= 'ERROR !!'
    download_video_button['state'] = 'normal'
    download_playlist_button['state'] = 'normal'
    download_audio_button['state'] = 'normal'
    pause_button['state'] = 'disabled'
    cancel_button['state'] = 'disabled'
####################################################################################################################################
# for playlist using multithreading
def downsingle(video,number,filelocation,escaped_name,progress_var, video_count):
    global yt
    yt=video.streams.filter(type='video', progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    video.streams.\
        filter(type='video', progressive=True, file_extension='mp4').\
        order_by('resolution').\
        desc().\
        first().\
        download(output_path=filelocation+'/'+escaped_name,filename_prefix='{}. '.format(number))
    # Update the progress bar
    progress_var.set(progress_var.get() + 1/video_count*100)    

####################################################################################################################################
def download_playlist_video(url,filelocation,progress_var,number):
    global is_paused, is_cancelled,filesize       #decalaration of variables jinko hum doosri jagah bhi u
    
    download_playlist_button['state'] = 'disabled'
    pause_button['state'] = 'normal'
    cancel_button['state'] = 'normal'

    try:
        progress['text'] = 'Downloading Playlist...'       #ab progress mein text change ho kr ye likh jaayega
        playlist = Playlist(url)        # 'playlist' mein uski url playlisturl_entry wale widget se ismke aake save ho jaayegi   
        video_count = len(playlist.videos) # for relative progress bar 
        global future
        escaped_name = re.sub(r"[\\\/\\:\\*\\?\\<\\>\\|]", "", playlist.title)   # playlist ke title mein se separators ko replace krne ke liye

        with ThreadPoolExecutor(max_workers=4) as executor:
            for video in playlist.videos:
                progress['text']= 'downloading {}'.format(video.title)
                future = executor.submit(downsingle, video,number,filelocation,escaped_name,progress_var, video_count) 
                number+=1
        if(progress['text']!='CANCELLED !!'):
            progress['text']= 'Done !!'    
    except Exception as e:   #agar try wala na hua toh
        print(e)
        progress['text']= 'ERROR !!'
    download_video_button['state'] = 'normal'
    download_playlist_button['state'] = 'normal'
    download_audio_button['state'] = 'normal'
    pause_button['state'] = 'disabled'
    cancel_button['state'] = 'disabled'   

######################################################################################################################################

def download_audio(url,filelocation):
    global is_paused,filesize
    download_audio_button['state'] = 'disabled'
    pause_button['state'] = 'normal'
    cancel_button['state'] = 'normal'
    try:
        progress['text'] = 'Downloading Audio...'       #ab progress mein text change ho kr ye likh jaayega
        video=YouTube(url)
        
        progress['text']= 'downloading {}'.format(video.title)
        video.register_on_progress_callback(progress_callback)
        global yt
        yt=video.streams.get_audio_only()
        yt.download(output_path=filelocation)
        video.register_on_complete_callback(complete_callback)      
        progress['text']= 'Done !!'
    except Exception as e:
        print(e)
        progress['text']= 'ERROR !!'
    download_audio_button['state'] = 'normal'
    pause_button['state'] = 'disabled'
    cancel_button['state'] = 'disabled'
    download_playlist_button['state'] = 'normal'
    download_video_button['state'] = 'normal'

def progress_callback(stream, chunk, bytes_remaining):
    size = yt.filesize
    progress = int(((size - bytes_remaining) / size) * 100)
    pbar.config(value=progress)
    # do call progress bar from GUI here

def complete_callback(stream, file_handle):
    progress['text'] = 'Downloaded!'
    # progress bar stop call from GUI here

def update_progress(downloaded, filesize):
    progress = downloaded / filesize
    pbar.config(value=progress)

def start_video_download():
    filelocation = askdirectory()  #this method is included in filedialog of Tkinter and it returns the directory path of folder user chose
    threading.Thread(target=download_video, args=(url_entry.get(),filelocation), daemon=True).start()
    
    #The Daemon Thread does not block the main thread from exiting and continues to run in the background.
    #from Class Threading use Thread(target,arguments,daemon).start()

def start_playlist_download():
    filelocation = askdirectory()  #this method is included in filedialog of Tkinter and it returns the directory path of folder user chose
    progress_var.set(0) 
    threading.Thread(target=download_playlist_video, args=(playlisturl_entry.get(),filelocation,progress_var,1), daemon=True).start()
        

def start_audio_download():
    filelocation = askdirectory()
    threading.Thread(target=download_audio, args=(url_entry.get(),filelocation), daemon=True).start()

def toggle_download(future,number):
    global is_paused
    is_paused = not is_paused
    pause_button['text'] = 'Resume' if is_paused else 'Pause'
    if(is_paused):
        future.cancel()
        


def cancel_download(future):
    future.cancel()
    download_audio_button['state'] = 'normal'
    pause_button['state'] = 'disabled'
    cancel_button['state'] = 'disabled'
    download_playlist_button['state'] = 'normal'
    download_video_button['state'] = 'normal'
    progress['text']= 'CANCELLED !!'




# gui
root = Tk()
root.title("Video Downloader")
root.geometry("700x700+350+40")
root.config(bg="#1c2659")

# Copyright
originalBtn = Button(root,bg="#1c2659",foreground="white", text="Made by Us \u2764\uFE0F", font="Rockwell", relief="flat")
originalBtn.pack(side=BOTTOM)


# main icon section
file = PhotoImage(file=resource_path("home.png"))
root.iconphoto(False, PhotoImage(file=resource_path("iconpng.png")))
headingIcon = Label(root, image=file)
headingIcon.pack(side=TOP, pady=3)



# Url Field

entry_text=StringVar()

url_entry = Entry(root, textvariable=entry_text,justify=CENTER, bd=5, fg='white',bg="#9824b5")
url_entry.pack(side=TOP, fill=X, padx=10)
url_entry.insert(0, "Paste URL of Video") #to show temp text

def clear_placeholder(event):
    if entry_text.get() == "Paste URL of Video":
        entry_text.set("")

url_entry.bind("<FocusIn>", clear_placeholder)

def set_placeholder(event):
    if not entry_text.get():
        entry_text.set("Paste URL of Video")

url_entry.bind("<FocusOut>", set_placeholder)        

# Playlist Url Field
plentry_text=StringVar()
playlisturl_entry = Entry(root,textvariable=plentry_text,justify=CENTER, bd=5, fg='white',bg="#9824b5")
playlisturl_entry.pack(side=TOP, fill=X, padx=10, pady=10)
playlisturl_entry.insert(0, "Paste URL of Playlist or Video of a Playlist to Download")

def clear_plplaceholder(event):
    if plentry_text.get() == "Paste URL of Playlist or Video of a Playlist to Download":
        plentry_text.set("")

playlisturl_entry.bind("<FocusIn>", clear_plplaceholder)

def set_plplaceholder(event):
    if not plentry_text.get():
        plentry_text.set("Paste URL of Playlist or Video of a Playlist to Download")

playlisturl_entry.bind("<FocusOut>", set_plplaceholder)     



# Progress
progress = Label(root,bg="#1c2659",fg="white",font=("Georgia", 12, "italic", "bold"),text='Welcome to Downloader !')
progress.pack(side=TOP,expand=True,fill=BOTH)

# Download Video Button
download_video_button = Button(root, text='Download Video', width=15, activebackground="#236F21",activeforeground="white", command=start_video_download, font='verdana', relief='ridge', bd=5, bg='#9824b5', fg='white')
download_video_button.pack(side=LEFT, padx=5,pady=10)

# Download Audio Button
download_audio_button = Button(root, text='Download Audio', width=15, activebackground="#236F21",activeforeground="white", command=start_audio_download, font='verdana', relief='ridge', bd=5, bg='#9824b5', fg='white')
download_audio_button.pack(side=RIGHT, padx=5,pady=10)

# Download Playlist Button
download_playlist_button = Button(root, text='Download Playlist', width=15, activebackground="#236F21",activeforeground="white", command=start_playlist_download, font='verdana', relief='ridge', bd=5, bg='#9824b5', fg='white')
download_playlist_button.pack(side=TOP, pady=10)

#progrss_bar

#format => ttk.Progressbar(container, orient, length, mode)
#indeterminate ka mtlb hai bounce back krta rhega
#determinate ka mtlb hai relative progress show krta hai
progress_var = DoubleVar()
pbar = ttk.Progressbar(root,maximum=100,orient = "horizontal",mode = "determinate",variable=progress_var)
pbar.pack(side = TOP,fill = X,padx = 20)

# Pause Button
pause_button = Button(root, text='Pause', command=lambda:toggle_download(future,number),state='disabled', font='verdana', relief='ridge', bd=3, bg='#FFD801', fg='#bfe3ed')
pause_button.pack(side=LEFT,pady=20,padx=5)

# Cancel Button
cancel_button = Button(root, text='Cancel', width=10, command=lambda:cancel_download(future), state='disabled', font='verdana', relief='ridge', bd=3, bg='#C40233', fg='#bfe3ed')
cancel_button.pack(side=RIGHT,pady=20,padx=5)

root.mainloop()
