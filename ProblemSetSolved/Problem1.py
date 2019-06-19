N = int(raw_input("Enter the no. of students: "))
results = {}

for i in range(N):
     print "Enter name and marks"
     a = raw_input("").split(' ')
     results[a[0]] = [float(x) for x in a[1:]]
student = raw_input("Enter the student whose average needs to be calculated: ")
print "%.2f" %(sum(results[student])/len(results[student]))
