# def print_something(name):
#     print(name)

# # print_something("krishna")
# # print_something("naveen")
# print_something("sathya")
# print_something("kannan")
students_grades = [
    {"name": "Alice", "marks": [{"social": 80, "maths": 60, "science": 20, "tamil": 99, "english": 66}]},
    {"name": "Bob", "marks": [{"social": 70, "maths": 65, "science": 75, "tamil": 85, "english": 78}]},
    {"name": "Charlie", "marks": [{"social": 90, "maths": 85, "science": 95, "tamil": 88, "english": 92}]},
    {"name": "Diana", "marks": [{"social": 82, "maths": 79, "science": 85, "tamil": 90, "english": 87}]},
    {"name": "Eve", "marks": [{"social": 88, "maths": 90, "science": 2, "tamil": 94, "english": 89}]},
    {"name": "Frank", "marks": [{"social": 75, "maths": 80, "science": 70, "tamil": 60, "english": 65}]},
    {"name": "Grace", "marks": [{"social": 95, "maths": 90, "science": 85, "tamil": 80, "english": 88}]},
    {"name": "Hank", "marks": [{"social": 60, "maths": 70, "science": 65, "tamil": 75, "english": 70}]},
    {"name": "Ivy", "marks": [{"social": 85, "maths": 75, "science": 80, "tamil": 85, "english": 82}]},
    {"name": "Jack", "marks": [{"social": 78, "maths": 85, "science": 88, "tamil": 90, "english": 84}]}
]

def print_students(values):
    for data in values:
        print(data["name"])

def total_marks(student):
    soc_m = student["marks"][0]["social"]
    mat_m = student["marks"][0]["maths"]
    sci_m = student["marks"][0]["science"]
    tam_m = student["marks"][0]["tamil"]
    eng_m = student["marks"][0]["english"]
    stu_mark = [ soc_m, mat_m, sci_m, tam_m, eng_m]
    total = sum(stu_mark)
    print(total)
    
print_students(students_grades)

for marks in students_grades:
    print(marks)
    total_marks(marks)