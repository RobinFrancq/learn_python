from Tkinter import Label, PhotoImage, Frame

from threading import Thread
from Publisher import Publisher
from Subscriber import Subscriber
import time

# Creating the observer (that is connected to a channel)
pub = Publisher(["channel1"])
sub1 = Subscriber('SUB1')
pub.register("channel1", sub1)

# Class GUI which inherts from Thread (to obtained multithreading)
class GUI(Thread):
    
    def __init__(self, master, mw, mh):
        
        # Basic settings of display
        self.root = master
        self.w, self.h = mw, mh
        self.root.overrideredirect(1)
        self.root.geometry("%dx%d+0+0" % (self.w, self.h))
        self.root.configure(background='black')
        master.title("DISPLAY")
        
        self.frameLeftTop        =   Frame(master,    bg="black",   width=self.w/6,      height=self.h/6)
        self.frameMiddleTop      =   Frame(master,    bg="black",    width=self.w*4/6,    height=self.h/6)
        self.frameRightTop       =   Frame(master,    bg="black",     width=self.w/6,      height=self.h/6)
        self.frameLeftMiddle     =   Frame(master,    bg="black",    width=self.w/6,      height=self.h*4/6)
        self.frameMiddleMiddle   =   Frame(master,    bg="black",    width=self.w*4/6,    height=self.h*4/6)
        self.frameRightMiddle    =   Frame(master,    bg="black",    width=self.w/6,      height=self.h*4/6)
        self.frameBottomLeft     =   Frame(master,    bg="black",   width=self.w/6,      height=self.h/6)
        self.frameBottomMiddle   =   Frame(master,    bg="black",    width=self.w*4/6,    height=self.h/6)
        self.frameBottomRight    =   Frame(master,    bg="black",     width=self.w/6,      height=self.h/6)

        self.frameLeftTop.grid       (row=0, column=0)
        self.frameMiddleTop.grid     (row=0, column=1)
        self.frameRightTop.grid      (row=0, column=2)
        self.frameLeftMiddle.grid    (row=1, column=0)
        self.frameMiddleMiddle.grid  (row=1, column=1)
        self.frameRightMiddle.grid   (row=1, column=2)
        self.frameBottomLeft.grid    (row=2, column=0)
        self.frameBottomMiddle.grid  (row=2, column=1)
        self.frameBottomRight.grid   (row=2, column=2)

        # Initialisation of components on display with default options
        self.mainMessage = Label(self.frameMiddleTop,
                                 background="black", 
                                 fg="white", 
                                 font=("Helvetica", (self.w/self.h)*100))
        
        self.time = Label(self.frameBottomLeft, 
                          background="black", 
                          fg="white", 
                          font=("Helvetica", (self.w/self.h)*100))
                          
        self.date = Label(self.frameBottomMiddle, 
                          background="black", 
                          fg="white", 
                          font=("Helvetica", (self.w/self.h)*100))
        
        self.weatherTemp = Label(self.frameLeftTop,
                                 background="black", 
                                 fg="white", 
                                 font=("Helvetica", (self.w/self.h)*100))
        
        """
        self.location = Label(frameLeftTop,
                              background="black",
                              fg="white",
                              font=("Helvetica", 40))
        """
        
        self.weatherImage = Label(self.frameLeftMiddle)
        
        self.updateTime = Label(self.frameRightTop, 
                                background="black", 
                                fg="white", 
                                font=("Helvetica", (self.w/self.h)*20))
        
        # Start of the tread (when object is initialized)
        Thread.__init__(self)
        self.start()
    
    # Overwriting the run method (fired when start() is called)
    def run(self):
        
        # Keep running while the program is active
        print("GUI IS RUNNING...")
        loop_active = True
        while loop_active:
            
            startTime = time.time()
            
            # re-call channel1 to get updated information
            pub.dispatch("channel1")
            
            # config all components on display and show the components with new content from channel1
            self.mainMessage.config(text=sub1.data.mainMessage)
            self.mainMessage.place(x=(self.w*4/6)/2, y=(self.h/6)/2, anchor="center")
            
            self.time.config(text=sub1.data.time)
            self.time.place(x=(self.w/6)/2, y=(self.h/6)/2, anchor="center")
            
            self.date.config(text=sub1.data.date)
            self.date.place(x=(self.w*4/6)/2, y=(self.h/6)/2, anchor="center")
            
            if (sub1.data.weather.currentTemp != None):
                self.weatherTemp.config(text=sub1.data.weather.currentTemp+ u'\N{DEGREE SIGN}'+ "C")
                self.weatherTemp.grid(row=2)
            else:
                self.weatherTemp.config(text="Themperture Not Found!")
                self.weatherTemp.grid(row=2)
            
            """    
            if (sub1.data.weather.country != None or sub1.data.weather.location != None):
                self.location.config(text=sub1.data.weather.country+ " - " +sub1.data.weather.location)
                self.location.grid(row=3)
            else:
                self.location.config(text="Location Not Found!")
                self.location.grid(row=3)
            """
            
            if (sub1.data.weather.imageName != None):
                photo = PhotoImage(file=sub1.data.weather.imageName)
                self.weatherImage.config(image=photo,
                                         borderwidth=0,
                                         highlightthickness=0)
                self.weatherImage.grid(row=4)
            else:
                photo = PhotoImage(file="img/Danger.gif")
                self.weatherImage.config(image=photo,
                                         borderwidth=0,
                                         highlightthickness=0)
                self.weatherImage.grid(row=4)
            
            self.updateTime.config(text=str(time.time() - startTime))
            self.updateTime.grid(row=0, 
                                 column=3)
            
            time.sleep(5)