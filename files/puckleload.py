import pickle

f = open("student.dat", "rb")

# een binaire file unpickelen
obj = pickle.load(f)
obj.display()

f.close()