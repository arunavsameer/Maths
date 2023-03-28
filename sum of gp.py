'''
def func(a,r,n):
    if n==0:
        return a
    return a*(r**n)

def fn2(a,r,n):
    d=0
    for i in range(0,n,1):
        e = func(a,r,i)
        d = d + e
    return d

fn2(1,0.5,10000000000)
'''
'''
def fn1(a, b, c):
    d = 0
    for x in range(c):
        d = d + a
        a = a * b
    return d

fn1(23,32,10000)
'''

def sum(a,r,n):
    if a >= 0 and n >=0:
        return (a*((r**n)-1))/(r-1)
    else:
        print("invalid entry")
print(sum(1,0.5,1000000000))       
