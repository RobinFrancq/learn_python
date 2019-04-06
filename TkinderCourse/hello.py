# https://www.python-course.eu/python_tkinter.php

# importeren van de zaken die we nodig hebben uit de Tkinder module
from Tkinter import Tk, Label

# De main root widget. Dit is de window met mogelijke decoraters zoals een title
# Er kan altijd maar 1 root widget aanwezig zijn!
root = Tk()

# Het label widget
# De eerste parameter is de parent widget waardat het label onderdeel van moet zijn
# De tweede (optionele) parameter is de text van het label
w = Label(root, text="Hello Tkinder!")

# pack()-functie is een simpele functie om geween de widget in de parent te steken
# De grootte van de parent past zich aan aan de grote van de child widget
w.pack()

# Het zichtbaar maken van de root (window)
root.mainloop()

# De window blijft zichtbaar zolang we niet op sluiten hebben gedrukt