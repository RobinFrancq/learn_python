from Tkinter import Tk, Label, PhotoImage

root = Tk()

imgPath = "hacker.gif"
photo = PhotoImage(file=imgPath)
label = Label(root, image=photo)
label.pack()

root.mainloop()