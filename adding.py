from re import S


def adder(*args):
    s=0
    for i in args:
       s+=i
    return s 

result = adder(3,4,5)
print(result)