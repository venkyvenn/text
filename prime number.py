n=int(input("enter a range :"))
for i in range(n):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)

f=0
s=1
for k in range(n):
    print(f)
    a=f
    f=s
    s=a+f
    