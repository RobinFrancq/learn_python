from Tkinter import Tk, Frame, Button, LEFT

def write_slogan():
    print("Tkinder is easy to use!")

root = Tk()
frame = Frame(root)
frame.pack()

button = Button(frame, 
                text="QUIT",
                fg="red",
                command=quit)
button.pack(side=LEFT)

slogan = Button(frame,
                text="Hello",
                command=write_slogan())
slogan.pack(side=LEFT)

root.mainloop()