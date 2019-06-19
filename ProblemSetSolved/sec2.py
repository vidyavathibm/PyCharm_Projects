class Circle:
    radius=12
    def getArea(self):
        area=3.14*self.radius*self.radius
        print "Area of a circle",area
    def getCircumference(self):
        circum=2*3.14*self.radius
        print "Circumfernce of a circle",circum

c=Circle()
c.getArea()
c.getCircumference()