import pickle, student

# wb voor een binaire file
f = open("student.dat", "wb")

s = student.Student(123, "Robin", 90)

# pickle gebruiken om een object te dumpen in een file
pickle.dump(s, f)

f.close()