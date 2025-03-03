import numpy as np
import pandas as pd

def calculate_gpa(grade_counts):
    # Define grade points for each letter grade
    grade_points = {
        'A+': 4.0, 'A': 4.0, 'A-': 3.67,
        'B+': 3.33, 'B': 3.0, 'B-': 2.67,
        'C+': 2.33, 'C': 2.0, 'C-': 1.67,
        'D+': 1.33, 'D': 1.0, 'D-': 0.67,
        'F': 0.0
    }
    
    total_points = 0
    total_count = 0
    
    # Calculate total grade points and count
    for grade, count in grade_counts.items():
        if grade in grade_points:  # Exclude W grades
            total_points += grade_points[grade] * count
            total_count += count
    
    # Calculate GPA
    if total_count > 0:
        return total_points / total_count
    return 0.0

def calculate_grade_disparity(professor_name: str):
    # Read the UIUC GPA dataset
    df = pd.read_csv('data/uiuc-gpa-dataset.csv')
    
    # Initialize grade disparity dictionary to store counts for each grade
    grade_counts = {
        'A+': 0, 'A': 0, 'A-': 0,
        'B+': 0, 'B': 0, 'B-': 0,
        'C+': 0, 'C': 0, 'C-': 0,
        'D+': 0, 'D': 0, 'D-': 0,
        'F': 0, 'W': 0
    }
    
    # Filter courses for the given professor, handling null values
    professor_courses = df[df['Primary Instructor'].notna() & df['Primary Instructor'].str.startswith(professor_name)]
    
    if len(professor_courses) == 0:
        print(f"No courses found for professor {professor_name}")
        return
    
    # Print each course row and accumulate grade counts
    for _, course in professor_courses.iterrows():
        course_grade_counts = {
            'A+': 0, 'A': 0, 'A-': 0,
            'B+': 0, 'B': 0, 'B-': 0,
            'C+': 0, 'C': 0, 'C-': 0,
            'D+': 0, 'D': 0, 'D-': 0,
            'F': 0, 'W': 0
        }
        
        # Add grade counts for this course
        for grade in grade_counts.keys():
            if f'{grade}' in course:
                count = course[f'{grade}']
                grade_counts[grade] += count
                course_grade_counts[grade] = count
        
        course_gpa = calculate_gpa(course_grade_counts)
    
    overall_gpa = calculate_gpa(grade_counts)
    return overall_gpa

# print(calculate_grade_disparity("Tsokaros, A"))