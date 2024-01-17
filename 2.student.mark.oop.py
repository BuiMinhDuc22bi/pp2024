class Student:
    def __init__(self, student_name, age, student_id):
        self.__student_name = student_name
        self.__age = age
        self.__student_id = student_id
        self.__marks = {}

    def add_mark(self, course_name, mark):
        self.__marks[course_name] = mark

    def get_student_name(self):
        return self.__student_name

    def get_age(self):
        return self.__age

    def get_student_id(self):
        return self.__student_id

    def get_marks(self):
        return self.__marks


class Course:
    def __init__(self, course_name, course_id):
        self.__course_name = course_name
        self.__course_id = course_id
    
    def get_name(self):
        return self.__course_name
    
    def get_course_id(self):
        return self.__course_id


class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def list_students(self):
        print("Student list:")
        for student in self.students:
            print(f"Name: {student.get_student_name()}, ID: {student.get_student_id()}, Age: {student.get_age()}")

    def list_courses(self):
        print("Course list:")
        for course in self.courses:
            print(f"Name of the course: {course.get_name()}, ID of the course: {course.get_course_id()}")

    def input_student_marks(self, course_name):
        for student in self.students:
            mark = float(input(f"Enter marks for student {student.get_student_name()} in course {course_name}: "))
            student.add_mark(course_name, mark)

    def display_student_marks(self, course_name):
        print(f"Student marks for course {course_name}:")
        found = False
        for student in self.students:
            for course, mark in student.get_marks().items():
                if course == course_name:
                    found = True
                    print(f"Student: {student.get_student_name()}, ID: {student.get_student_id()}, Marks: {mark}")
        if not found:
            print("We don't have any marks yet!")

    def print_menu(self):
        print("\n--- MENU ---")
        print("1. Input marks for a course")
        print("2. List courses")
        print("3. List students")
        print("4. Show student marks for a course")
        print("5. Exit")

    def handle_menu_choice(self, choice):
        if choice == 1:
            course_name = input("Enter the course name to input marks for students: ")
            self.input_student_marks(course_name)
        elif choice == 2:
            self.list_courses()
        elif choice == 3:
            self.list_students()
        elif choice == 4:
            course_name = input("Enter the course name to display student marks: ")
            self.display_student_marks(course_name)
        elif choice == 5:
            print("Exiting...")
            return False
        else:
            print("Invalid choice. Please try again.")
        return True

    def run(self):
        num_students = int(input("Enter the number of students: "))
        for _ in range(num_students):
            student_name = input("Enter your name: ")
            student_id = input("Enter your id: ")
            age = int(input("Enter your age: "))
            student = Student(student_name, student_id, age)
            self.add_student(student)

        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course_name = input("Enter your course: ")
            course_id = input("Enter your id_course: ")
            course = Course(course_name, course_id)
            self.add_course(course)

        while True:
            self.print_menu()
            choice = int(input("Enter your choice: "))
            if not self.handle_menu_choice(choice):
                break


school_system = SchoolSystem()
school_system.run()