name=raw_input("enter your full name: ")
age=input("Enter your age: ")
f_name=name.split()
print "First Name "+f_name[0]
print "Last Name "+f_name[1]
if age>=18:
    print name+" is elgible to vote"
else:
    print name+" is not eligible to vote"