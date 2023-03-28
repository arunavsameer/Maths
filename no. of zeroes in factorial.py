def fac(n):
    if n == 1 or n == 0:
        return 1
    return n * fac(n-1)
a = fac(int(input()))
#print(a)

'''
z = 0
while a%10 == 0:
    a = a/10
    z = z + 1
print(z)
'''

b = list(str(a))
c = len(b)
#print(b)

d = 0
for i in range(1,c+1):
    l = c - i
    if b[l] == '0' :
        d = d + 1
    else:
        break
print(d)        