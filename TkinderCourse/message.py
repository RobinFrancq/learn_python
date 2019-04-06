# De message widget is hetzelfde als het Label maar biedt meer flexibiliteit voor text

from Tkinter import Tk, Message

master = Tk()
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = Message(master, text=whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack()

master.mainloop()

# Alle magelijke opties voor de config van een message widget, kunnen hier teruggevonden worden:
# https://www.python-course.eu/tkinter_message_widget.php
