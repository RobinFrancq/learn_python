from Tkinter import Tk, Frame, Label

app = Tk()
f = Frame(app,bg="yellow",width=50,height=50)
f.grid(row=0,column=0,sticky="NE")
f.grid_propagate(0)
f.update()
l = Label(f,text="123",bg="yellow")
l.place(x=25, y=25, anchor="center")
app.mainloop()