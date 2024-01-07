def number_of_stundents(students):
    #create a list for students 
    student_list = []
    for i in range (students):
        #student informations 
        student_name = input("Enter your name: ")
        student_id = input("Enter your id: ")
        age = int(input("Enter your age: "))
    #create a tuple with student info
        a_student = (student_name,student_id,age)
        student_list.append(a_student)
    return student_list

def number_of_courses(courses):
    #create a list of courses
    course_list = []
    for i in range(courses):
        #course information
        course_name = input("Enter your course: ")
        course_id = input("Enter your id_course: ")
        a_course = (course_name,course_id)
        course_list.append(a_course)

    return course_list

def print_student_list(students):
    #print student list
    print("Student list: ")
    for a_student in students:
        student_name,student_id,age = a_student
        print(f"Name: {student_name}, Id: {student_id},Age: {age}")

def print_course_list(courses):
    #print course list
    print("Course list: ")
    for a_course in courses:
        course_name,course_id = a_course
        print(f"Name of the course: {course_name}  Name of the id course: {course_id}")

def input_student_marks(student_list, course_list):
    #make an input for the marks 
    course_name = input("Enter the course name to input marks for students: ")
    for student in student_list:
        student_name, student_id, age, *marks = student
        student_marks = float(input(f"Enter marks for student {student_name} in course {course_name}: "))
        marks.append((course_name, student_marks))

def display_student_marks(student_list):
    #make a display
    course_name = input("Enter the course name to display student marks: ")
    print(f"Student marks for course {course_name}:")
    found = False # create a flag to check 
    for student_name, student_id, age, *marks in student_list:
        for course, marks_value in marks:
            if course == course_name:
                found = True
                print(f"Student: {student_name}, ID: {student_id}, Marks: {marks_value}")
    if not found:
        print("We don't have any marks yet!")


def print_menu():
    #create choices
    print("\n--- MENU ---")
    print("1. Input marks for a course")
    print("2. List courses")
    print("3. List students")
    print("4. Show student marks for a course")
    print("5. Exit")

def handle_menu_choice(choice, student_list, course_list):
    if choice == 1:
        input_student_marks(student_list, course_list)
    elif choice == 2:
        print_course_list(course_list)
    elif choice == 3:
        print_student_list(student_list)
    elif choice == 4:
        display_student_marks(student_list)
    elif choice == 5:
        print("Exiting...")
        return False
    else:
        print("Invalid choice. Please try again.")
    return True


def main():
    num_students = int(input("Enter the number of students: "))
    student_list = number_of_stundents(num_students)

    num_courses = int(input("Enter the number of courses: "))
    course_list = number_of_courses(num_courses)

    while True:
        print_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            input_student_marks(student_list, course_list)
        elif choice == 2:
            print_course_list(course_list)
        elif choice == 3:
            print_student_list(student_list)
        elif choice == 4:
            display_student_marks(student_list)
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()