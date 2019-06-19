list=[1,2,3,4,5,6,7,8,9]
sum=0
for x in list:
    if x%2==0:
        sum=sum+x
print sum
for x in list:
    if x%2!=0:
        continue
    else:
        print x



