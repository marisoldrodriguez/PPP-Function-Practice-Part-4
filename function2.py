# Python function called mult_list() to multiply all the numbers in a list
def mult_list(list):
    if len(list) == 0:
        return 0
    prod = list[0]
    if len(list) > 1:
        for i in list[1:]:
            prod = prod * i 
    return prod
print(mult_list([10]))
print(mult_list([2,4,6]))
print(mult_list([]))
print(mult_list([1,2,3]))
    