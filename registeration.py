class Course:
    def __init__(self, course_id, name, prerequisite=None):
        # Initialize Course object with course ID, name, and optional prerequisite
        self.course_id = course_id
        self.name = name
        self.prerequisite = prerequisite
        self.enrolled_students = []  # List to store enrolled students

    def add_student(self, student):
        # Method to enroll student in the course
        # Check student prerequisite
        if self.prerequisite and not student.has_passed_prerequisite(self.prerequisite):
            print(f"Cannot enroll {student.name} in {self.name}: Prerequisite not met.")
            return
        # Check if the student has paid fees
        if student.is_fee_defaulter():
            print(f"Cannot enroll {student.name} in {self.name}: Fee not paid.")
            return
        # Add student to enrolled_students list
        self.enrolled_students.append(student)
        # Add the course to the student's enrolled courses
        student.enrolled_courses.append(self)

    def display_enrolled_students(self):
        # Method to display enrolled students for the course
        print(f"Enrolled students for course {self.name}:")
        for student in self.enrolled_students:
            print(student.name)


class Student:
    def __init__(self, student_id, name, has_paid_fees=True):
        # Initialize Student object with student ID, name, and fee payment status
        self.student_id = student_id
        self.name = name
        self.has_paid_fees = has_paid_fees
        self.courses_passed = []  # List to store passed courses
        self.enrolled_courses = []  # List to store enrolled courses

    def is_fee_defaulter(self):
        # Method to check if the student has paid fees
        return not self.has_paid_fees

    def has_passed_prerequisite(self, prerequisite_course):
        # Method to check if the student has passed a prerequisite course
        return prerequisite_course in self.courses_passed

    def display_enrolled_courses(self):
        # Method to display enrolled courses for the student
        print(f"Enrolled courses for student {self.name}:")
        for course in self.enrolled_courses:
            print(course.name)


def display_available_courses(courses):
    # Function to display available courses
    print("Available courses:")
    for idx, course in enumerate(courses, 1):
        print(f"{idx}. {course.name}")


# Main program
courses = []  # List to store created courses

while True:
    print("\nOptions:")
    print("1. Create new course")
    print("2. Enroll student")
    print("3. Display enrolled students for a course")
    print("4. Display enrolled courses for a student")
    print("5. Display available courses")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Option to create a new course
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        prerequisite_id = input("Enter prerequisite course ID (leave blank if none): ")
        prerequisite = None
        # Check if prerequisite course ID is provided
        if prerequisite_id:
            prerequisite = next((course for course in courses if course.course_id == prerequisite_id), None)
            if prerequisite is None:
                print("Error: Prerequisite course not found.")
                continue
        # Create a new Course object and add it to the courses list
        course = Course(course_id, name, prerequisite)
        courses.append(course)
        print("Course created successfully.")

    elif choice == "2":
        # Option to enroll a student
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        has_paid_fees = input("Has the student paid the fees? (yes/no): ").lower() == "yes"
        student = Student(student_id, name, has_paid_fees)
        # Check if the student is a fee defaulter
        if student.is_fee_defaulter():
            print(f"Cannot enroll {student.name}: Fee not paid.")
        else:
            # Display available courses and enroll the student in the selected course
            display_available_courses(courses)
            course_idx = input("Enter the index of the course to enroll the student: ")
            try:
                course_idx = int(course_idx)
                if 1 <= course_idx <= len(courses):
                    course = courses[course_idx - 1]
                    course.add_student(student)
                else:
                    print("Error: Invalid course index.")
            except ValueError:
                print("Error: Invalid input for course index.")

    elif choice == "3":
        # Option to display enrolled students for a course
        if not courses:
            print("No courses available.")
            continue
        print("Available courses:")
        for idx, course in enumerate(courses, 1):
            print(f"{idx}. {course.name}")
        course_idx = input("Enter the index of the course: ")
        try:
            course_idx = int(course_idx)
            if 1 <= course_idx <= len(courses):
                course = courses[course_idx - 1]
                course.display_enrolled_students()
            else:
                print("Error: Invalid course index.")
        except ValueError:
            print("Error: Invalid input for course index.")

    elif choice == "4":
        # Option to display enrolled courses for a student
        if not courses:
            print("No courses available.")
            continue
        student_id = input("Enter student ID: ")
        # Find the student and display their enrolled courses
        student = next((student for course in courses for student in course.enrolled_students if student.student_id == student_id), None)
        if student:
            student.display_enrolled_courses()
        else:
            print("Student not found.")

    elif choice == "5":
        # Option to display available courses
        display_available_courses(courses)

    elif choice == "6":
        # Exit the program
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
