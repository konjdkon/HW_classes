class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average = 0

    def rate_lector(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
            x, y = 0, 0
            for item in (lector.grades).values():
                for i in range(len(item)):
                    x += item[i]
                    y += 1
            lector.average = float(x/y)
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
            f'Средняя оценка за домашние задания: {self.average:.2f}\n' \
            f'Курсы в процессе изучения: {", ".join(x for x in self.courses_in_progress)}\n' \
            f'Завершенные курсы: {", ".join(x for x in self.finished_courses)}'

    def __add__(self, other):
        return self.average + other.average

    def __verify_data(self, other):
        return other if isinstance(other, int) else other.average

    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.average == sc

    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.average < sc

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.average = 0

class Lecturer(Mentor):
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции {self.average:.2f}'
    def __add__(self, other):
        return self.average + other.average

    def __verify_data(self, other):
        return other if isinstance(other, int) else other.average

    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.average == sc

    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.average < sc

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            x, y = 0, 0
            for item in (student.grades).values():
                for i in range(len(item)):
                    x += item[i]
                    y += 1
            student.average = float(x / y)
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

std1 = Student('Ruoy', 'Eman', 'your_gender')
std1.courses_in_progress += ['Python']
std1.courses_in_progress += ['C++']
std1.courses_in_progress += ['Java']

std2 = Student('Ivan', 'KKK', 'male')
std2.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']



lect1 = Lecturer('Fedor', 'Pavlov')
lect2 = Lecturer('Egor', 'Konstantinov')
rev = Reviewer('Dyadya', 'Vanya')

rev.courses_attached += ['Python']
rev.courses_attached += ['C++']
rev.courses_attached += ['Java']

rev.rate_hw(std1, 'Python', 8)
rev.rate_hw(std1, 'C++', 7)
rev.rate_hw(std1, 'Java', 7)

rev.rate_hw(std2, 'Python', 10)

lect1.courses_attached += ['Python']
lect1.courses_attached += ['C++']
lect1.courses_attached += ['Python']

lect2.courses_attached += ['Python']

std1.rate_lector(lect1, 'Python', 20)
std1.rate_lector(lect1, 'C++', 5)
std1.rate_lector(lect1, 'Python', 6)

std1.rate_lector(lect2, 'Python', 20)

print(rev)
print(lect1)
print(lect2)
print(std1)
print(std2)

t = std1 + std2
#print(t)
t = lect1 + lect2
#print(t)
print(std1<std2)
print(lect1<lect2)


def calc_std_av(students, courses):
    x, z = 0, 0
    for y in range(len(students)):
        for i in range(len(courses)):
            for o in range(len(students[y].grades[courses[i]])):
                x += students[y].grades[courses[i]][o]
                z += 1
    print(f'средняя оценка студентов {", ".join(str(students[p].name) for p in range(len(students)))} '
          f'по предметам {", ".join(str(courses[m]) for m in range(len(courses)))} = {(x / z):.2f}')

calc_std_av([std1, std2], ["Python"])

def calc_lector_av(lect, courses):
    x, z = 0, 0
    for y in range(len(lect)):
        for i in range(len(courses)):
            for o in range(len(lect[y].grades[courses[i]])):
                x += lect[y].grades[courses[i]][o]
                z += 1
    print(f'средняя оценка лекторов {", ".join(str(lect[p].name) for p in range(len(lect)))} '
          f'по предметам {", ".join(str(courses[m]) for m in range(len(courses)))} = {(x / z):.2f}')

calc_lector_av([lect1, lect2], ["Python"])