from Tkinter import Tk, Label, Button

counter = 0

# Geneste functies dat blijven loopen
def counter_label(label):
    
    # count() gaat de counter verhogen en de inhoud van het meegegeven label aanpassen
    # after() wacht een aantal miliseconden (1000) en voert dan een functie uit (count())
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)
    count()

root = Tk()
root.title("Counting Seconds")
label = Label(root, fg="green")
label.pack()

# Uitvoeren van de oneindig doorlopende functie op het label
counter_label(label)

# Toevoegen van Button Widget
# command is de functionaliteit uitgevoerd bij het klikken op de knop
# root.destroy beindigd de applicatie
button = Button(root, text="Stop", width=25, command=root.destroy)
button.pack()

root.mainloop()