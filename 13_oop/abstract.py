from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    # abstract method
    def sides(self):
        pass


class Triangle(Shape):

    # overriding abstract method
    def sides(self):
        print("I have 3 sides")


class Circle(Shape):

    # overriding abstract method
    def sides(self):
        print("I have 0 sides")


class Square(Shape):

    # overriding abstract method
    def sides(self):
        print("I have 4 sides")


T = Triangle()
T.sides()

C = Circle()
C.sides()

S = Square()
S.sides()

print('************')

A = Shape()
A.sides()
