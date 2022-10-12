# From 50 days of Python Challenge book


def student_marks():
    grades = {}
    while True:
        marks = str(input("Enter student name followed by the student's grade (ex. John:94); press enter to break: "))
        if marks == '':
            break
        grades[(marks.split(':'))[0]] = (marks.split(':'))[1]
    return grades


# print(student_marks())
