# from errorHandling import demo
from app import *

try:
    name = "kannan"
    print_func(name)
    find_avg_for = []
    response = avg(find_avg_for)
    print_func(response)
    # print_func(avg([1,2,3,4,5]))
except Exception as err:
    print(err)