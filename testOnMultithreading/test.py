from Tkinter import Label, Tk
from threading import Thread
from Publisher import Publisher
from Subscriber import Subscriber

class App(Thread):

    def __init__(self, tk_root):
        self.root = tk_root
        Thread.__init__(self)
        self.start()

    def run(self):
        loop_active = True
        while loop_active:
            print("test")
            
            '''
            user_input = raw_input("Give me your command! Just type \"exit\" to close: ")
            if user_input == "exit":
                loop_active = False
                self.root.quit()
                self.root.update()
            else:
                label = Label(self.root, text=user_input)
                label.pack()
            '''    

ROOT = Tk()
APP = App(ROOT)
LABEL = Label(ROOT, text="Hello, world!")
LABEL.pack()
ROOT.mainloop()