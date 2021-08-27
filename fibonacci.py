n=int(input("Enter number: "))
#[0,1,1,2,3,5,8] for n=7
a=[]
for i in range(n):
    if i==0:
        a.append(0)
    elif i==1:
        a.append(1)
    else:
        fibn=a[i-1]+a[i-2]
        a.append(fibn)
    print(a[i])