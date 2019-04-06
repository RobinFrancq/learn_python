from Tkinter import Tk, PhotoImage, Label, LEFT, CENTER

root = Tk()
logo = PhotoImage(file="img/broken_clouds.gif")

"""
w1 = Label(root, image=logo).pack(side="right")
"""

explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""

# justify wordt gebruikt om inhoud te plaatsen links, rechts of in het midden (devault CENTER)
# padx is de padding links en rechts in pixels (default 1px)
"""
w2 = Label(root,
           justify=LEFT,
           padx=10,
           text=explanation).pack(side="left")
"""

# Indien je zowel de image als de text in hetzelfde label wilt
# Gebruik van compound op het label
"""
w2 = Label(root,
           compound = CENTER,
           text=explanation,
           image=logo).pack(side="right")
"""

# Dit is de beste manier om een label en een image samen te zetten (in 1 label)
w = Label(root,
          justify=LEFT,
          compound=LEFT,
          padx=10,
          text=explanation,
          image=logo).pack(side="right")           
 
root.mainloop()