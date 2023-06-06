from pytube import YouTube
import tkinter as tk
import threading
from tkinter import messagebox

progress = 0         
def showProgress(stream,chunk,bytes_remaining):
    size = stream.filesize
        
    global progress
    preProgress = progress
        
    currentProgress = (size - bytes_remaining)*100 // size
    progress = currentProgress
        
    if progress == 100:
        print("下載完成！")
        return
    
    if preProgress != progress:
        scale.set(progress)
        window.update()
        print("目前進度： " + str(progress) + "%")

def onClick():
    
    global var
    var.set(entry.get())

    button.config(state=tk.DISABLED)
    try:
        yt = YouTube(var.get(),
                     on_progress_callback=showProgress)
        
        if onlyMusic.get():
            stream = yt.streams.filter(only_audio=True).first()
        else:
            stream = yt.streams.first()
            
        stream.download()
        
        tk.messagebox.showinfo(title="下載完成",message="Youtube影片下載完成")
        button.config(state=tk.NORMAL)
    except:
        print("下載失敗")
        
        tk.messagebox.showerror(title="錯誤",message="下載時發生不可預期的錯誤")
        button.config(state=tk.NORMAL)
        

def th():
    threading.Thread(target=onClick).start()

window = tk.Tk()

window.title("YouTube下載器")
window.geometry("500x150")
window.resizable(False,False)

label = tk.Label(window,
                 text = "請輸入YouTube影片網址")
label.pack()

var = tk.StringVar()
entry = tk.Entry(window, width = 50)
entry.pack()

onlyMusic = tk.BooleanVar()
check = tk.Checkbutton(window, text = "只有音樂", variable = onlyMusic,
                       onvalue = True, offvalue = False)
check.pack()

button = tk.Button(window, text = "下載",
                   command = th)
button.pack()

scale = tk.Scale(window, label='進度條', from_=0, to=100,
             orient=tk.HORIZONTAL,
             length=200, showvalue=False,
             tickinterval=0)
scale.pack()

window.mainloop()

