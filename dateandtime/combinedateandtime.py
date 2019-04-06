from datetime import *

# jaar,maand,dag
d = date(2018,7,21)
# uur, minuten
t = time(12,45)

# returnt een datetime-object
dt = datetime.combine(d, t)
print(dt)