
#Program to dettermine angle between the hands of a12 hours clock
#input is given as hh:mm


time=raw_input("Enter time")
li=time.split(':')
print li[0]
print li[1]
print 30 * float(li[0]) - 5.5 * float(li[1])
print 360 - (30 * float(li[0]) - 5.5 * float(li[1]))
angle = min((30 * float(li[0]) - 5.5 * float(li[1]), 360 - (30 * float(li[0]) - 5.5 * float(li[1]))))
print angle
