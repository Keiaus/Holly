from tkinter import *

class GUI:
    def __init__(self, root):
        root.title('Home')
        root.state('zoomed')

        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)

        header_font = ("Gills Sans", 50, "bold")
        Label(text='Holly says hi', font=header_font).pack(pady=40)

        user_input = Entry(font='times 30', width=50, bd=20).pack(pady=250)

class Chatbot:
    def all_greetings():
        greetings = [
            "Goodmorning",
            "How are you?",
            "How have you been",
            "What's up",
            "Wake up"
        ]
    
root = Tk()
GUI(root)
root.mainloop()