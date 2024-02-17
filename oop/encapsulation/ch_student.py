class Student:
    def __init__(self, name):
        self.name = name
        self.__courses = {}

    def calculate_letter_grade(self, score):
        grades = { 9: "A", 8: "B", 7: "C", 6: "D"}
        for i in grades:
            if score // 10 >= i:
                return grades[i]
        return "F"

    def add_course(self, course_name, score):
        grade = self.calculate_letter_grade(score)
        self.__courses[course_name] = grade

    def get_courses(self):
        return self.__courses

