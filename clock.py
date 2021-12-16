# Import Libraries

from tkinter import  * 
from tkinter.ttk import * 

from time import strftime

root = Tk()
root.title("Clock")

# declare function 
def time():
  string = strftime('%H:%M:%S:%p')
  label.config(text=string)
  label.after(1000, time)
  
label = Label(root)
label.pack(anchor='center')
time()    #function call

mainloop()
