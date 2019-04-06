from Tkinter import Tk, Frame, Label

app = Tk()

w, h = app.winfo_screenwidth(), app.winfo_screenheight()

app.overrideredirect(1)
app.geometry("%dx%d+0+0" % (w, h))
app.title("DISPLAY")

print(w, h)

# 1920, 1200

frameLeftTop        =   Frame(app,    bg="yellow",   width=w/6,      height=h/6)
frameMiddleTop      =   Frame(app,    bg="green",    width=w*4/6,    height=h/6)
frameRightTop       =   Frame(app,    bg="blue",     width=w/6,      height=h/6)
frameLeftMiddle     =   Frame(app,    bg="brown",    width=w/6,      height=h*4/6)
frameMiddleMiddle   =   Frame(app,    bg="black",    width=w*4/6,    height=h*4/6)
frameRightMiddle    =   Frame(app,    bg="brown",    width=w/6,      height=h*4/6)
frameBottomLeft     =   Frame(app,    bg="yellow",   width=w/6,      height=h/6)
frameBottomMiddle   =   Frame(app,    bg="green",    width=w*4/6,    height=h/6)
frameBottomRight    =   Frame(app,    bg="blue",     width=w/6,      height=h/6)

frameLeftTop.grid       (row=0, column=0)
frameMiddleTop.grid     (row=0, column=1)
frameRightTop.grid      (row=0, column=2)
frameLeftMiddle.grid    (row=1, column=0)
frameMiddleMiddle.grid  (row=1, column=1)
frameRightMiddle.grid   (row=1, column=2)
frameBottomLeft.grid    (row=2, column=0)
frameBottomMiddle.grid  (row=2, column=1)
frameBottomRight.grid   (row=2, column=2)

"""
timeFrame = Frame(app,bg="yellow",width=w/5,height=h/5)
timeFrame.grid(row=0,column=0)

mainMessageFrame = Frame(app,bg="green",width=w*3/5,height=h/5)
mainMessageFrame.grid(row=0,column=1)

updateTimeFrame = Frame(app,bg="blue",width=w/5,height=h/5)
updateTimeFrame.grid(row=0,column=2)

time = Label(timeFrame,text="12:59",font=("Helvetica", (w/h)*75))
time.place(x=(w/5)/2, y=(h/5)/2, anchor="center")

mainMessage = Label(mainMessageFrame,text="Good Morning",font=("Helvetica", (w/h)*100))
mainMessage.place(x=(w*3/5)/2, y=(h/5)/2, anchor="center")

updateTime = Label(updateTimeFrame,text="0.123456789",font=("Helvetica", (w/h)*25))
updateTime.place(x=(w/5)/2, y=(h/5)/2, anchor="center")
"""
app.mainloop()