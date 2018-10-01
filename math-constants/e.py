import math 

pi = math.pi 

e = ( pi**4 + pi**5 )**(1/6)

memo = {}
memo[1] = 1
memo[0] = 1 

def fact(x):
    if memo.get(x)!=None:
        return memo[x]
    memo[x] = x * fact(x-1)
    return memo[x]

def ex(x):
    sum = 0
    count = 10**4
    for i in range(count):
        sum = sum + (x**i/fact(i))
    return sum

print(ex(1)==math.exp(1))
print(e,'\n',math.exp(1))
print(ex(1)) 