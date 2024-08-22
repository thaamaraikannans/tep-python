def print_func(value):
    try:
        print(value)
        return
    except Exception as err:
        print(err)
        return

def avg(input):
    try:
        total = sum(input)
        length = len(input)
        return total/length
    except Exception as err:
        return err