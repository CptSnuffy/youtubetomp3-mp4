import os
import tkinter as tk
from tkinter import Button, Canvas, Frame
from tkinter.constants import BOTH, RIGHT, X
import tkinter.messagebox

import youtube_dl


class YoutubeToMP3():
    def __init__(self):
        pass

    def run(self):
        self.draw_gui()


    def window_setup(self):
        
        def move_window(event):
            root_window.geometry('+{0}+{1}'.format(event.x_root-250, event.y_root))

        def download_audio():
            ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors':[{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
        }
            url = user_entry_box.get()

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                tkinter.messagebox.showinfo(title='Download complete!', message='Download complete!')

        def download_video():
            url = user_entry_box.get()
            ydl_opts = {}

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                tkinter.messagebox.showinfo(title='Download complete!', message='Download complete!')

    
        root_window = tk.Tk()

        root_window.overrideredirect(True)

        title_bar = Frame(root_window,bg ='#292726', relief='flat', bd=2, highlightthickness=0)
        close_button = Button(title_bar, text='X', bg='#292726', activebackground='red', relief='flat', font='bold',fg='white', highlightthickness=0, command=root_window.destroy)

        window = Canvas(root_window,bg ='#343130', highlightthickness=0)
        
        # select_button = Button(window, text='Select File',bg='#343130', activebackground='#292726',relief='flat', font='bold', fg='#c4c4c4', activeforeground='#4764f5', command=placeholder_button)
        # encrypt_button = Button(window, text='Encrypt',bg='#343130', activebackground='#292726',relief='flat', font='bold', fg='#c4c4c4', activeforeground='#4764f5', command=placeholder_button)
        # decrypt_button = Button(window, text='Decrypt',bg='#343130', activebackground='#292726',relief='flat', font='bold', fg='#c4c4c4', activeforeground='#4764f5', command=placeholder_button)
        download_mp3 = Button(window, text='Convert To MP3',bg='#343130', activebackground='#292726',relief='flat', font='bold', fg='#ffffff', activeforeground='#d4d4d4', command=download_audio)
        download_mp4 = Button(window, text='Convert To MP4',bg='#343130', activebackground='#292726',relief='flat', font='bold', fg='#ffffff', activeforeground='#d4d4d4', command=download_video)
        user_entry_box = tk.Entry(root_window, font=('Helvetica 15'))

        root_window.geometry('500x250+600+200')
        root_window.title('Youtube to MP3/MP4')
        root_window['background'] = '#343130'

        # select_button.place(x=75,y=90)
        # encrypt_button.place(x=375,y=90)
        # decrypt_button.place(x=225,y=90)
        user_entry_box.place(x=50, y=90, width=400, height=30)
        download_mp3.place(x=50, y=155)
        download_mp4.place(x=325, y=155)
        
        # select_button.pack
        # encrypt_button.pack
        # decrypt_button.pack
        user_entry_box.pack
        download_mp3.pack
        download_mp4.pack

        title_bar.pack(expand=0, fill=X)
        close_button.pack(side=RIGHT)
        window.pack(expand=1, fill=BOTH)

        title_bar.bind('<B1-Motion>', move_window)

        root_window.attributes("-topmost", True)

        return root_window    

    def draw_gui(self):
        root_window = self.window_setup()
        root_window.mainloop()

    