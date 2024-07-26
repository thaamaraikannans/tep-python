# if we have square braces -> [] -> is known as List
# eg -> [10, 20, 30 ] -> collection of data types

data = [10, "10", ["20", "30", "40"]]
# data = [10, "10", ["20", "30", "40", "50"]]
# print(data[2][2][1])
print(data[2])
data[2].append("60")
print(data[2])
print(data[2][0])
print(data[2][1])
print(data[2][2])
()