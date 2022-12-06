'''Класс студентов   '''


class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

# Метод который подсчитывает средний бал за домашнее задание

    def average_stud(self):
        average = [str(sum(b) / len(b)) for a, b in self.grades.items()]
        return average

# Переопределение __str__

    def __str__(self):
        ret = f'Имя =  {self.name} \nФамилия = {self.surname} \nСредняя оценка за лекции: {", ".join(self.average_stud())} \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return ret

# Метод оценки лекторов

    def rate_lect(self, lecturer, course, grade):
        if isinstance(
                lecturer, Lecturer
        ) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades and grade <= 10:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

# Переопределение __lt__  Сравнения студентов по среднему балу

    def __lt__(self, other):
        if isinstance(other, Student) and isinstance(self, Student):
            return self.average_stud() < other.average_stud()
        return 'Ошибка'


#  Родительский класс
class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

# Переопределение __str__

    def __str__(self):
        ret = (
            f'Имя =  {self.name} \nФамилия = {self.surname} \nСредняя оценка за лекции: {", ".join(self.average_lec())}'
        )
        return ret

# Переопределение __lt__  Сравнения студентов по среднему балу

    def __lt__(self, other):
        if isinstance(other, Lecturer) and isinstance(self, Lecturer):
            return self.average_lec() < other.average_lec()
        return 'Ошибка'


# Метод который подсчитывает средний бал за лекции у лекторов

    def average_lec(self):
        average = [str(sum(b) / len(b)) for a, b in self.grades.items()]
        return average


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

# Переопределение __str__

    def __str__(self):
        ret = (f'Имя =  {self.name} \nФамилия = {self.surname} ')
        return ret

    def rate_hw(self, student, course, grade):
        if isinstance(
                student, Student
        ) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Задание 4. Средний бал за домашку у студентов по опроделенному курсу
def all_average_stud(stud_list, course):
    z = [
        round(sum(y) / len(y), 2) for x in stud_list if isinstance(x, Student)
        for x, y in x.grades.items() if x == course
    ]
    if z == []:  # Проверка если нет оценок и пустой  список  получаеться
        return 'Ошибка'
    else:
        return z[0]


# Задание 4. Средний бал у лекторов по определенному курсу
def all_average_lect(lect_list, course):
    z = [
        round(sum(y) / len(y), 2) for x in lect_list
        if isinstance(x, Lecturer) for x, y in x.grades.items() if x == course
    ]
    if z == []:  # Проверка если нет оценок и пустой  список  получаеться
        return 'Ошибка'
    else:
        return z[0]


# Создание 2х студентов
student_one = Student('Ruoy', 'Eman', 'm')
student_one.courses_in_progress += ['Python']  # Изучает и Python и  Git
student_one.courses_in_progress += ['Git']
student_one.finished_courses += ['C#']
student_one.finished_courses += ['C++']

student_two = Student('Denis', 'Stepanov', 'm')
student_two.courses_in_progress += ['C#']  # Изучает только C#
student_two.finished_courses += ['C++']

# Создание 2х Лекторов
lecturer_one = Lecturer('Petr', 'Sidorov')
lecturer_one.courses_attached += ['Python']  # Читает лекции   на курсе Python

lecturer_two = Lecturer('Marina', 'Petrova')
lecturer_two.courses_attached += ['C#']  # Читает лекции на курсе С#

# Создание 2х Проверяющих (Проверяет  студентов на курсе Python)
reviewer_one = Reviewer('Liza', 'Ivanova')
reviewer_one.courses_attached += ['Python'
                                  ]  # Проверяет  студентов на курсе Python

reviewer_two = Reviewer('Andrey', 'Chetkiy')
reviewer_two.courses_attached += ['C#']
reviewer_two.courses_attached += [
    'Python'
]  # Проверяет  студентов на курсе Python и С#

#  Создание общих списков студентов и лекторов
student_list = [student_one, student_two]
lecturer_list = [lecturer_one, lecturer_two]

# Выставил оценки первый проверяющий
reviewer_one.rate_hw(student_one, 'Python', 10)
reviewer_one.rate_hw(student_one, 'Python', 2)
reviewer_one.rate_hw(student_two, 'C#',
                     3)  # Проверка тк Первый проверяющий не может проверить C#
reviewer_one.rate_hw(student_two, 'C#',
                     3)  # Проверка тк Первый проверяющий не может проверить C#

# Выставил оценки второй проверяющий
reviewer_two.rate_hw(student_one, 'Python', 9)
reviewer_two.rate_hw(student_one, 'Python', 8)
reviewer_two.rate_hw(student_two, 'C#', 9)
reviewer_two.rate_hw(student_two, 'C#', 3)

# Выставил оценки первый студент
student_one.rate_lect(lecturer_one, 'Python', 10)
student_one.rate_lect(lecturer_one, 'Python', 8)
student_one.rate_lect(
    lecturer_two, 'Python', 5
)  # Проверка тк первый студент  не может  ставить оценки за курс который  не ведёт лектор
student_one.rate_lect(
    lecturer_two, 'Python', 7
)  # Проверка тк первый студент  не может  ставить оценки за курс который  не ведёт лектор

# Выставил оценки второй студент
student_two.rate_lect(
    lecturer_one, 'Python', 4
)  # Проверка тк второй студент  не может  ставить оценки за курс который он не проходит
student_two.rate_lect(
    lecturer_one, 'Python', 4
)  # Проверка тк второй студент  не может  ставить оценки за курс который он не проходит
student_two.rate_lect(lecturer_two, 'C#', 2)
student_two.rate_lect(lecturer_two, 'C#', 2)

# Задание 3. Переопределен метод __str__ у студентов
print()
print(student_one)
print()
print(student_two)
print()

# Задание 3. Переопределен метод __str__ у лекторов
print(lecturer_one)
print()
print(lecturer_two)
print()

# Задание 3. Переопределен метод __str__ у проверяющих
print(reviewer_one)
print()
print(reviewer_two)
print()

# Выводим Задание 4. Средний бал у студентов
print('Средний бал у студентов за домашнеe заданиe по Python:', end=" ")
print(all_average_stud(student_list, 'Python'))

# Выводим Задание 4. Средний бал у лекторов
print('Средний бал у лекторов за лекции по Python:', end=" ")
print(all_average_lect(lecturer_list, 'Python'))
print()


# Сравниваем студентов
print(student_one < student_two)
print(student_one > student_two)
print()

# Сравниваем лектиоров
print(lecturer_one < lecturer_two)


