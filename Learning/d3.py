'''class A:
    def func1(self):
        print "class A"

class B:
    def func2(self):
        print "class B"

class C(A,B):
    def func3(self):
        print "Class A and B"

a=A()
b=B()
c=C()
a.func1()
b.func2()
c.func1()
c.func2()
c.func3()'''
class A:
    def func1(self):
        print "class A"

class B(A):
    def func2(self):
        print "class B"

class C(B):
    def func3(self):
        print "Class A and B"

a=A()
b=B()
c=C()
a.func1()
b.func2()
b.func1()
c.func2()
c.func1()
c.func3()