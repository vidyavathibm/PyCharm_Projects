a,b,c=raw_input("Enter three numbers: ").split()
print a
print b
print c

if (a==b or a==c or b==c):
    print 0
else:
    print int(a)+int(b)+int(c)
