class Student:
    number_of_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = {}
        Student.number_of_students += 1

    def add_grade(self, subject, grade):
        if subject not in self.grades:
            self.grades[subject] = [grade]
        else:
            self.grades[subject].append(grade)
    
    def calculate_average(self):
        sum_of_grades = 0
        amount = 0
        for subj in self.grades:
            sum_of_grades += sum(self.grades[subj])
            amount += len(self.grades[subj])
        return sum_of_grades/amount

    def get_letter_grade(self):
        average = self.calculate_average()
        if average > 90:
            return f'student got A'
        elif average > 80:
            return 'student got B'
        elif average > 70:
            return 'student got C'
        elif average > 60:
            return 'student got D'
        elif average > 50:
            return 'student got E'
        elif average > 40:
            return 'student got FX'
        else:
            return 'student got F'
        
    @classmethod
    def get_student_amount(cls):
        return cls.number_of_students

