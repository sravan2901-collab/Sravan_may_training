def analyze_result(name, roll, marks):
    total = sum(marks)
    average = total / len(marks)
 
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"
 
    print(f"Student: {name} (Roll: {roll})")
    print(f"Total: {total}, Average: {average}")
    print(f"Grade: {grade}")
 
    failed_subjects = []
    for i, mark in enumerate(marks):
        if mark < 40:
            failed_subjects.append(f"Subject {i + 1}")
 
    if failed_subjects:
        print(f"Subjects below 40: {', '.join(failed_subjects)}")
    else:
        print("No subjects below 40")
 
 

name = input("name = ")
roll = int(input("roll = "))
marks = list(map(float,input("marks = ").split()))
 
analyze_result(name, roll, marks)
