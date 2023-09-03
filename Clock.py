from tkinter import *
from time import strftime

mywindow = Tk()
mywindow.title('Myclock')

def time():
    mytime = strftime('%H:%M:%S %p')
    clock.config(text= mytime)
    clock.after(1000, time)

clock = Label(mywindow, font= ('ariel', 40, 'bold'),
             background = 'skyblue',
             foreground = 'white')

clock.pack(anchor='center')     
time()

mainloop()