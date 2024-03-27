import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image



root = tk.Tk()
root.title("Spherical Manipulator Calculator")
root.geometry('800x500')
img = PhotoImage(file='icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)
root.config(bg='#262626')

image_icon= Image.open('gui_icon.png')
image_icon= ImageTk.PhotoImage(image_icon)


header_text= Label(root, text='SPHERICAL', 
              font= ('Helvetica', '27', 'bold'),
              fg='#52FF00',
              pady=15,
              anchor='w',
              bg= '#262626')
header_text.grid(row= 0, column=1)


root.mainloop()