import math
import os
import random
import re
import sys

def gradingStudents(grades):
    for grade in grades:
        if (grade >= 38) and (grade % 5 >= 3):
            grade = (grade + 5) // 5 * 5
        print(grade)

if __name__ == '__main__':
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)