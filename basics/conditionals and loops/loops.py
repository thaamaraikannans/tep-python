languages = [ "swift", "python", "go"]

for data in languages:
    print(data)
    data = data.capitalize()
    print(data)
    if data == "Swift":
        print("\n",data, "is valid name")
    else:
        print("\n",data, "not valid name")
        