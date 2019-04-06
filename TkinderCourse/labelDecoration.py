from Tkinter import Tk, Label

root = Tk()

# fg (foreground) is de kleur van de text zelf
# bg (background) is de kleur van de achtergrond van de text
# font is de naam van het lettertype, de lettergrootte en extra gegevens (bold, italic...)

Label(root,
      text="Red Text in Times Font",
      fg="red",
      font="Times").pack()

Label(root,
      text="Green Text in Helvetica Font",
      fg="light green",
      bg="dark green",
      font="Helvetica 16 bold italic").pack()

Label(root,
      text="Blue Text in Verdana bold",
      fg="blue",
      bg="yellow",
      font="Verdana 10 bold").pack()

root.mainloop()