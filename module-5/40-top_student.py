#/usr/bin/python3
"""Write a function that takes a dictionary of student names and scores and returns the name of the student with the highest score.
"""
def top_student(scores):
    
    if not scores:
        return None
    return max(scores, key=scores.get)
students = {'Alice': 88, 'Bob': 95, 'Charlie': 90}
print(top_student(students))  # Output: Bob