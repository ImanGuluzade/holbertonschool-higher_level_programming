#!/usr/bin/python3
"""Main script to test Student class with JSON save/load"""

from 11-student import Student
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file
from 0-read_file import read_file
import os

filename = "student.json"

# Remove file if it already exists
if os.path.exists(filename):
    os.remove(filename)

# Create a student
student_1 = Student("John", "Doe", 23)
print("Initial student:")
print(student_1)
print("Attributes:", student_1.first_name, student_1.last_name, student_1.age)

# Convert to JSON and save to file
json_student = student_1.to_json()
save_to_json_file(json_student, filename)
print("\nSaved JSON to file:")
read_file(filename)

# Create a fake student
new_student = Student("Fake", "Fake", 89)
print("\nFake student before reload:")
print(new_student)
print("Attributes:", new_student.first_name, new_student.last_name, new_student.age)

# Load JSON from file and reload fake student
json_data = load_from_json_file(filename)
new_student.reload_from_json(json_data)
print("\nFake student after reload:")
print(new_student)
print("Attributes:", new_student.first_name, new_student.last_name, new_student.age)
