import tkinter as tk
from time import strftime

def time():
    current_time = strftime('%H: %M: %S')
    
    label.config(text=current_time)
    label.after(1000, time)
    
root = tk.Tk()
root.title('Digital Clock')
    
label = tk.Label(root, font=('Arial',60),background= 'black', foreground= 'red')
label.pack(anchor= 'center')
    
time()
    
root.mainloop()
