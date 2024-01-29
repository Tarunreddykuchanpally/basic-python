a=[8,1,3,2,6]
sum=0
for i in a:
    sum=sum+i
print(sum)

a=[4,2,3,1,6,7,9]
b=[]
c=[]
for i in a:
    if i%2==0:
        b.append(i)
    else:
        c.append(i)
print(b)
print(c)