def kannan():
    try:
        a = 10000
        a= str(a)
        print(a[1])
        print("helloe")
    except Exception as err:
        print(err)
    else:
        print("no error found")
    finally:
        print("i'm going to execute on all time")

try:
    kannan("name")
except Exception as err:
    print(err)
    kannan()