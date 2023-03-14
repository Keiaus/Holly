from tkinter import *

root = Tk()
root.title('Home')
root.state('zoomed')

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

main_page = Frame(root)

def show_frame(frame):
    frame.tkraise()

for frame in (main_page):
    frame.grid(row=0, column=0, sticky='nsew')

header = Label(main_page, text='Welcome to Holly', font='times 50 bold', bg='Skyblue', anchor=N, pady=50)
header.pack(fill='BOTH')

show_frame(main_page)
root.mainloop()