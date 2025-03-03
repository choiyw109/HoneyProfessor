from course_explorer import get_professors
from grade_disparity import calculate_grade_disparity
def main():
    print("Welcome to UIUC Auto-RateMyProfessor Course Picker!")

    # Get user input
    year = input("Enter the academic year (e.g., 2025): ")
    term = input("Enter the semester (e.g., spring, fall): ").lower()
    course = input("Enter the course (e.g., CS 374): ").strip()

    try:
        subject, course_number = course.split(" ")
    except ValueError:
        print("Invalid format! Use format: SUBJECT COURSE_NUMBER (e.g., CS 374)")
        return

    # Fetch professor data
    professors = get_professors(year, term, subject.upper(), course_number)

    if not professors:
        print(f"No professors found for {course} in {term} {year}.")
    else:
        print(f"Professors teaching {course} in {term} {year}:")
        for prof in professors:
            print(f"- {prof}: {calculate_grade_disparity(prof)}")
    
    print(calculate_grade_disparity("Golecki, Thomas F"))

if __name__ == "__main__":
    main()
