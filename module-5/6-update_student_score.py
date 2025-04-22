#/usr/bin/python3
def update_score(students, name, new_score):
    
    # Update the score of the student if the name exists; otherwise, add the student
    students[name] = new_score
    
    return students

students = {"Ali": 80, "Tobi": 90}
print(update_score(students, "Ali", 95))  # Output: {'Ali': 95, 'Tobi': 90}
print(update_score(students, "Sarah", 88))  # Output: {'Ali': 95, 'Tobi': 90, 'Sarah': 88}
