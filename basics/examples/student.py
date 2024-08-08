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

subjects = ["social", "maths", "science", "tamil", "english"]
total_rank = [] # stu name and the total mark
total_order = [] # total mark
for student in students_grades:
    user = []
    name = student["name"]
    user.append(name)
    soc_m = student["marks"][0]["social"]
    mat_m = student["marks"][0]["maths"]
    sci_m = student["marks"][0]["science"]
    tam_m = student["marks"][0]["tamil"]
    eng_m = student["marks"][0]["english"]
    stu_mark = [ soc_m, mat_m, sci_m, tam_m, eng_m]
    total = sum(stu_mark)
    user.append(total)
    total_order.append(total)
    print(total)
    total_rank.append(user)
    print(user)
    for i in range(len(stu_mark)):
        if stu_mark[i] >= 35:
            pass
            # print(subjects[i] + " is " + "Pass")
        else:
            pass
            # print(subjects[i] + " is " + "Fail")
print(total_rank)
total_order.sort() # ascesding -> lower ----- higher
total_order.reverse() # descending -> higher ---- lower
print(total_order)

rank_holder = [] # rank wise name
for rank in total_order:
    for j in range(len(total_rank)):
        if total_rank[j][1] == rank:
            rank_holder.append(total_rank[j][0])

print(rank_holder)

for r_name in range(len(rank_holder)):
    print(r_name + 1, "is ", rank_holder[r_name])