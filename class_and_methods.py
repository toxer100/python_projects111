class Person:
    def __init__(self, name):
        self.name = name
        
    def introduce(self):
        print("Hi, my name is", self.name)
        
# Instantiate an instance of the class
p = Person("John")

# Call the method on the instance
p.introduce()  # Output: Hi, my name is John



class Shape:
    def area(self):
        pass
    
class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return self.side ** 2
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14159 * self.radius ** 2
    
# Instantiate an instance of the classes
s = Square(5)
c = Circle(2)

# Call the overridden method on each instance
print(s.area())  # Output: 25
print(c.area())  # Output: 12.56636


class Car:
    # Class variable
    num_wheels = 4
    
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    # Instance method
    def drive(self):
        print("Driving a", self.make, self.model)
        
    @classmethod
    def about(cls):
        print("A car has", cls.num_wheels, "wheels.")
        
# Instantiate an instance of the class
c = Car("Ford", "Mustang")

# Call the instance method on the instance
c.drive()  # Output: Driving a Ford Mustang

# Call the class method on the class
Car.about()  # Output: A car has 4 wheels.