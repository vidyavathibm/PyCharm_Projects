class Parent:
     var1=1
     def func1(self):
         print "parent method"
class Child(Parent):
    var2=2
    def func1(self):
        print "parent method in child"
    def func2(self):
        print "child method"


p = Parent()
c=Child()
c.func2()
c.func1()
p.func1()

