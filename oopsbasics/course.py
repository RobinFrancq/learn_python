class Course:
    
    # Constructor met parameters
    def __init__(self, name, ratings):
        self.name = name
        self.ratings = ratings
    
    def average(self):
        numberOfRatings = len(self.ratings)
        average = sum(self.ratings)/numberOfRatings
        print("Average Ratings For " +self.name+ " Is " +str(average))

# Meegeven van parameters
c1 = Course("Python", [1, 2, 3, 4, 5])
print(c1.name)
print(c1.ratings)
c1.average()

c2 = Course("Java", [4, 5])
print(c2.name)
print(c2.ratings)
c2.average()