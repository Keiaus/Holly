from tkinter import *

root = Tk()
root.title('Home')
root.wm_attributes('-fullscreen', 1)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

def show_frame(frame):
    frame.tkraise()

main_page = Frame(root)

show_frame(main_page)

for frame in (main_page):
    frame.grid(row=0, column=0, sticky='nsew')

header = Label(main_page, text='Welcome to Holly', font='times 50 bold', bg='Skyblue', anchor=N, pady=50)
header.pack(fill='BOTH')

root.mainloop()