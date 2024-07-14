def get_data(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            data = {}
            for line in lines:
                parts = line.split(':')
                student = parts[0].strip()
                courses = [course.strip() for course in parts[1].split(',')]
                data[student] = courses
        return data
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except IndexError as e:
        print(f"Data processing error: {e}")
        return None

def search(data, course_name):
    students_in_course = [student for student, courses in data.items() if course_name in courses]
    return students_in_course


data = get_data('input.txt')

if data is not None:
    while True:
        course_name = input("Enter the course title: ").strip()
        if not course_name:
            print("Course name cannot be empty. Please try again")
            continue

        students_in_course = search(data, course_name)

        if students_in_course:
            print(f"Students enrolled in the course {course_name}:")
            for student in students_in_course:
                print(student)
            break
        else:
            print(f"No one is registered for the {course_name} course or the course does not exist. Try again")