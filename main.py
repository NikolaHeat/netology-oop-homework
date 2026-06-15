class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        grades = []
        for course_grades in self.grades.values():
            grades += course_grades
        if len(grades) == 0:
            return 0
        return sum(grades) / len(grades)

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.average_grade()}
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}
Завершенные курсы: {", ".join(self.finished_courses)}'''

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        grades = []
        for course_grades in self.grades.values():
            grades += course_grades
        if len(grades) == 0:
            return 0
        return sum(grades) / len(grades)

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.average_grade()}'''

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}'''


def average_student_grade(students, course):
    grades = []
    for student in students:
        if course in student.grades:
            grades += student.grades[course]
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)


def average_lecturer_grade(lecturers, course):
    grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            grades += lecturer.grades[course]
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)


student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Ivan', 'Petrov', 'male')
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Git']

lecturer1 = Lecturer('Some', 'Buddy')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Petr', 'Sidorov')
lecturer2.courses_attached += ['Python']

reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Anna', 'Ivanova')
reviewer2.courses_attached += ['Python']

student1.rate_lecture(lecturer1, 'Python', 10)
student1.rate_lecture(lecturer1, 'Python', 9)

student2.rate_lecture(lecturer2, 'Python', 10)
student2.rate_lecture(lecturer2, 'Python', 8)

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)

reviewer2.rate_hw(student2, 'Python', 8)
reviewer2.rate_hw(student2, 'Python', 9)

print(reviewer1)
print()
print(lecturer1)
print()
print(student1)
print()

print(student1 > student2)
print(lecturer1 > lecturer2)

students = [student1, student2]
lecturers = [lecturer1, lecturer2]

print('Средняя оценка студентов по Python:', average_student_grade(students, 'Python'))
print('Средняя оценка лекторов по Python:', average_lecturer_grade(lecturers, 'Python'))