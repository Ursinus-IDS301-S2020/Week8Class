"""
@author: ctralie / IDS 301 Class
Purpose: To show how to dynamically fill in a dictionary
         using loops, and also to make sure students
         are comfortable with nested dictionaries
         (dictionaries that have keys whose values are 
         themselves dictionaries)
"""

# The main dictionary has the student name as a key,
# and a dictionary of student info as its value
students = {}
names = ['chris', 'celia']
# Each student is itself a dictionary with three keys
keys = ['year', 'major', 'grades']
# For the grades key, we have yet another dictionary that
# stores the grades by assignment
assignments = ['audio', 'image', 'nbody']

# Outer loop loops through the students
for name in names:
    print("Fill in info for ", name)
    # Setup a blank dictionary for this person
    students[name] = {} # Add empty dictionary as value for student
    for key in keys:
        # Fill the value for each key
        if key == 'grades':
            # If it's the grades key, we need to loop
            # through all of the assignments and create
            # a dictionary to hold the grades by assignment
            grades = {}
            for a in assignments:
                print("What is ", name, "'s grade on ", a)
                grade = int(input())
                grades[a] = grade
            students[name][key] = grades
        else:
            # For all other keys, we're simply storing
            # a string as their value
            print("What is ", key, " for ", name, "?")
            value = input()
            students[name][key] = value
    print(students[name])

print(students)