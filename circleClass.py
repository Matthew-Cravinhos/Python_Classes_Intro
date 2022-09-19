
# Print the circumference for circles with a radius of a given value

# Circle class.
# When a Circle object is instantiated,
# a data element is created and is a member of that object.
# Methods:
# __init()__
# circumference()
# printCircumference()


class Circle:

    def __init__(self, radius):
        self.radius = radius #This is where the object is created

    def circumference(self):
        pi = 3.14
        circumferenceValue = pi * self.radius * 2 #notice the use of self here, this means use this instance of the object
        return circumferenceValue

    def printCircumference(self):
        myCircumference = self.circumference()
        print ("Circumference of a circle with a radius of " + str(self.radius) + " is " + str(myCircumference))


circle1 = Circle(2) #you only need to pass the radius because when you call it on the next line, it starts the instance (self) then takes the int as the radius parameter
circle1.printCircumference()

circle2 = Circle(5)
circle2.printCircumference()

circle3 = Circle(7)
circle3.printCircumference()