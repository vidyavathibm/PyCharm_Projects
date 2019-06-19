year=input("Enter the year: ")
print type(year)
if year%400==0 and year%100==0:
    print year," is Leap Year"
else:
    print year," is not Leap Year"