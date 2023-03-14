from tkinter import *

root = Tk()
root.title('Home')
root.state('zoomed')

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

main_page = Frame(root)

header = Label(main_page, text='Welcome to Holly', font='times 50 bold', bg='Skyblue', anchor=N, pady=50)
header.pack(fill='both')

root.mainloop()