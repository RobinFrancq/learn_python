mathGrade = int(raw_input("Enter the grade for math: "))
physicsGrade = int(raw_input("Enter the grade for physics: "))
chemistryGrade = int(raw_input("Enter the grade for chemistry: "))

if mathGrade < 35 or physicsGrade < 35 or chemistryGrade < 35:
    print("You failed the full exam!")
else:
    avg = (mathGrade + physicsGrade + chemistryGrade)/3
    
    if avg <= 59:
        print("Your grade is C")
    elif avg <= 69:
        print("Your grade is B")
    else:
        print("Your grade is A")