dob=raw_input("Enter your birth date : (dd/mm/yyyy)")
num=dob.split("/")
print num
sum=0
for x in num:
    y =int(x)
    while y!=0:
        n = y % 10
        y = y / 10
        sum = sum + n
print sum
