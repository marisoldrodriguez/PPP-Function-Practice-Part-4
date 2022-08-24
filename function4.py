# Python function called num_within() to check whether a number falls in a given range
# The function accepts the number "x", beginning of range "a", and end of range "b"(inclusive) as arguments.
def num_within(x,a,b):
    return x in range(a,b+1)
print(num_within(3,2,4))
print(num_within(3,1,3))
print(num_within(10,2,5))
print(num_within(12,3,13))