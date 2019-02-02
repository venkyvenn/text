n=int(input("enter a range :"))
for i in range(n):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)