class Students:

    def __init__(self, school_name, male_students: int, female_students: int):

        # instance attr
        self.school_name = school_name
        self.male_students = male_students
        self.female_students = female_students

    def Calculate_total_students(self):
        total_students = self.male_students + self.female_students
        return total_students

