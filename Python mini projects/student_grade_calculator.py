def get_marks():
    english = int(input("Enter your english mark: "))
    maths = int(input("Enter your maths mark: "))
    science = int(input("Enter your science mark: "))
    social = int(input("Enter your social mark: "))
    computer = int(input("Enter your computer mark: "))

    return english,maths,science,social,computer

def get_total(english,maths,science,social,computer):
    total= english + maths + science + social + computer
    return total

def get_average(total):
    average= total/5
    return average

def get_grade(average):
    if average >= 90:
        grade = 'A+'
    elif average >= 80:
        grade = 'A'
    elif average >= 70:
        grade = 'B'
    elif average >= 60:
        grade = 'C'
    elif average >= 50:
        grade = 'D'
    else:
        grade = 'E'

    return grade

def display_result(total,average,grade):
    print("Total mark= ",total)
    print("average= ", average)
    print("grade= ",grade)
    if average >= 50:
        result = "PASS"
    else:
        result = "FAIL"
    print("result= ",result)


english,maths,science,social,computer = get_marks()
total = get_total(english,maths,science,social,computer)
average = get_average(total)
grade = get_grade(average)

display_result(total,average,grade)
