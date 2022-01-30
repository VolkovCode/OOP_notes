import re

def calculate(expression):
    int_list = re.split("[^\d]", expression)
    op_list = list(filter(None, re.split("[0-9]", expression)))
    res = 0
    for i in sorted(op_list):
        op_index = op_list(i)
        if i == '$' and res==0:
            res = int_list[op_index-1]/int_list[op_index+1]
        elif res !=0 and i == '$':
            res /= int_list[op_index+1]
        elif i == '+':
            res     


    return int_list, sorted(op_list)

print(calculate("5+8-8*2$4"))