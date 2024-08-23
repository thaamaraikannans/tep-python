# other languages -> JSON -> DICT 

# for API requests -> JSON STRING payload......

# DICT (JSON) -> STR (JSON STRING)   ,----->>>>>> json.dumps
# STR(JSON STRING) -> DICT           ,----->>>>>> json.loads


# API REQ -> JSON.dumps
# API RES -> JSON.loads


import json

student_1 = {"name": "Alice", "marks": [{"social": 80, "maths": 60, "science": 20, "tamil": 99, "english": 66}]}

print(type(student_1))

converted = json.dumps(student_1)

print(converted)
print(type(converted),"\n")

original = json.loads(converted)
print(original)
print(type(original))