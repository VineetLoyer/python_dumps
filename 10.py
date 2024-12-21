# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# records = [["chi",20.0],["beta",50.0],["alpha",50.0]]
# beta and alpha have second lowest score

# ouput is sorted alphabetically

# alpha
# beta
if __name__ == '__main__':
    stu = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        stu.append([name, score])  # Appending name, score to the student list

    # Sorting the student list based on score
    stu.sort(key=lambda x: x[1])

    # Extract unique grades and sort them
    unique_grades = sorted(set(student[1] for student in stu))  # Fix: student[1], not stu[1]
    second_lowest_grade = unique_grades[1]

    # Get names of students with the second lowest grade
    names = [student[0] for student in stu if student[1] == second_lowest_grade]

    # Print names alphabetically
    for name in sorted(names):
        print(name)