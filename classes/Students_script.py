from Students import Students

fudma = Students('fudma', 1500, 900)
print (fudma.school_name, fudma.male_students, fudma.female_students)

# printing the method that solves for the total_students in the object
print (fudma.Calculate_total_students())
