N = int(input("type a number"))
a = 0
b = 0
for n in range(1,abs(N)+1):
    if int(n)%2==1:
        a += n
print(a)
for n in range(1, abs(N)+1):
    if int(n)%2==0:
        b += n
        c = b//(n//2)
print(c)


