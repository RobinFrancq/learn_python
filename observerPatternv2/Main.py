from Tkinter import Tk
from GUI import GUI

# Starting the program by initializing the GUI class which automaticaly runs the thread

root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
app = GUI(root, w, h)
root.mainloop()