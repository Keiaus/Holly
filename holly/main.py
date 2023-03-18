from tkinter import *
from chatbot_utils import *

class GUI:
    def __init__(self, root):
        root.title('Home')
        root.state('zoomed')

        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)

        header_font = ("Gills Sans", 50, "bold")
        Label(text='Holly', bg="grey", font=header_font).pack(pady=40)
        text_box = Text(root, height=30, width=70).pack(pady=70)
        # output = generated response based on the user's input
        user_input = Entry(font='times 20', width=50, bd=20, background="Skyblue", fg='Black').pack(pady=10)
        generate_user_input = Button(text="Generate", font='times 20', background='Skyblue', fg='black').pack()
    
root = Tk()
root.configure(bg="Grey")
GUI(root)
root.mainloop()