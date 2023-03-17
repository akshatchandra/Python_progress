# class Computer:
#
#     def config (self):
#         print("i5 , 8Gb, 512 Gb")
#
# com1 = Computer()
# com2 = Computer()
#
# # Computer.config(com1)
# # Computer.config((com2))
#
# com1.config()
# com2.config()


# __init__ method
#
# class computer:
#     def __init__(self,cpu,ram):
#         self.cpu = cpu
#         self.ram = ram
#         # print("in init")
#
#     def config(self):
#         # print("i5,8GB,512GB")
#         print("Config is",self.cpu,self.ram)

# com1 = computer()
# com2 = computer()
# com1 = computer("5",16)
# com2 = computer("Ryzen 3",8)
#
# com1.config()
# com2.config()


# Constructor , self and comparing objects
# class Computer:
#     # pass
#     def __init__(self):
#         self.name = "aks"
#         self.age = 23
#
#     def update(self):
#         self.age = 32
#
#     def compare(self,other):
#         if self.age == other.age:
#             return True
#         else:
#             return False
#
# c1 = Computer()
# c2 = Computer()
# # print(id(c1))
# # print(id(c2))
# c1.name = "xyz"
# c1.age = 12
#
# if c1.compare(c2):
#     print("They are same")
# else:
#     print("They are not same")
# # c1.update()
# print(c1.name)
# # print(c2.name)
#
# print(c1.age)
# # print(c2.age)


# Types of Variable
# class Car:
#     wheels = 4
#
#     def __init__(self):
#         self.mil = 10
#         self.com = "AUDI"
#
# c1 = Car()
# c2 = Car()
# c1.mil = 8
# # Car.wheels=5
#
# print(c1.com,c1.mil,c1.wheels)
# print(c2.com,c2.mil,c2.wheels)

# Types of Method :
# 1> Instance method
# 2> Class methods
# 3> Static method


# class student:
#     school='xyz'
#     def __init__(self,m1,m2,m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
#
#     def avg(self):
#         return (self.m1+self.m2+self.m3)/3
#
#     # def get_m1(self):
#     #     return self.m1
#     # def set_m1(self,value):
#     #     self.m1=value
#     @classmethod
#     def getschool(cls):
#         return cls.school
#
#     @staticmethod
#     def info():
#         print("abjnjcavovihohv")
#
# s1 = student(32,23,12)
# s2 = student(23,11,21)
#
# print(s1.avg())
# print(s2.avg())
# print(student.info())

# Inner Class

# class Student:
#     def __init__(self,name,rollno):
#         self.name = name
#         self.rollno = rollno
#         self.lap = self.Laptop()
#
#     def show(self):
#         print(self.name , self.rollno)
#         self.lap.show()
#
#     class Laptop:
#         def __init__(self):
#             self.model = 'HP'
#             self.ram = 8
#         def show(self):
#             print(self.model,self.ram)
#
#
# s1 = Student('Aks',2)
# s2 = Student('zxc',3)
#
# # s1.show()
# s2.show()




# Inheritance
#
# class A:
#     def feature1(self):
#         print("F1 working")
#     def feature2(self):
#         print("F2 working")
#
# class B(A):
#     def feature3(self):
#         print("F3 working")
#
#     def feature4(self):
#         print("F4 working")
#
# class D:
#     def feature6(self):
#         print("F6 working")
#
# class C(B,D):
#     def feature5(self):
#         print("F5 working")
#
#
# a1 = A()
# a1.feature2()
# a1.feature1()
#
# b1 = B()
#
# c1 = C()
# c1.feature6()



# # Constructor in inheritance
# class A:
#     def __init__(self):
#         print("in A init")
#
#     def feature1(self):
#         print("Feature 1-A working")
#
#     def feature2(self):
#         print("Feature 2 working")
# # class B(A):
# class B:
#     def __init__(self):
#         super().__init__()
#         print("in B init")
#
#     def feature(self):
#         print("Feature 1-B working")
#
#     def feature(self):
#         print("Feature 4 working")
#
# class C(A,B):
# # class C(B,A):
#     def __init__(self):
#         super().__init__()  # Mro: method resolution order (left to right)
#         print("in C init")
#
#     def feat(self):
#         super().feature2()
# # a1 = A()
# # a1 = B()
# a1=C()
# a1.feature1()
# a1.feat()

# Polymorphism
# Duck typing
# operator Overloading
# method Overloading
# method Overriding

# Duck typing
# class Pycharm:
#     def execute(self):
#         print("compiling")
#         print("Running")
# class MyEditor:
#     def execute(self):
#         print("Spell check")
#         print("compiling")
#         print("Running")
# class Laptop:
#     def code(self,ide):
#         ide.execute()
# # ide = Pycharm()
# ide = MyEditor()
# lap1=Laptop()
# lap1.code(ide)

# Operator Overloading
# class Student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#     def __add__(self,other):
#         m1 = self.m1 + other.m1
#         m2 = self.m2 + other.m2
#         s3 = Student(m1,m2)
#
#         return s3
#
#     def __gt__(self, other):
#         r1 = self.m1 + self.m2
#         r2 = other.m1 + other.m2
#         if r1 > r2:
#             return True
#         else:
#             return False
#
# # s1 = Student(23,32)
# # s2 = Student(12,21)
# s1 = Student(23,32)
# s2 = Student(12,21)
# s3 = s1 + s2
# print(s3.m2)
# print(s3.m1)
#
# if s1 > s2:
#     print("s1 wins")g
# else:
#     print("s2 wins")


# Method Overloading and method overriding

# class Student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#
#     def sum(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#             s = a + b + c
#         elif a!= None and b!=None:
#             s = a + b
#         else:
#             s = a
#         return s
#
# s1 = Student(12,21)
# # print(s1.sum(22,44,21))
# # print(s1.sum(22,21))
# print(s1.sum(22))


# method overriding:
# class A:
#     def show(self):
#         print("show a")
#
# class B(A):
#     # pass
#     def show(self):
#         print("show b")
# # a1=A()
# a1=B()
# a1.show()

# Abstract Class and abstract method ABC = abstract base classes
# from abc import ABC, abstractmethod
# class Computer(ABC):
#     @abstractmethod
#     def process(self):
#
#         # print("A")
#         pass
#
# class Laptop(Computer):
#     # pass
#     def process(self):
#         print("its running")
# # a1=Computer()
# a1 = Laptop()
# # a1.process()
# a1.process()


# Iterator
# num = [1,2,3,4]
# # for i in num:
# #      print(i)
#
# it =  iter(num)
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(next(it))
# for i in num:
#     print(i)
# class top:
#     def __init__(self):
#         self.num = 1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if se
#         val = self.num
#         self.num += 1
#         return val
#
# valus = top()

# Generators:
# def topten():
#     # yield 4
#     # yield 3
#     # yield 2
#     # yield 1
#     # yield 0
#     n = 1
#     while n <= 10:
#         sq = n*n
#         yield sq
#         n+=1
#
# value = topten()
# # print(value)
# # print(value.__next__())
# print(value.__next__())
#
# for i in value :
#     print(i)


# Exception Handling:

a = 5
# b = 2
b=2
try:
    print("Resource open")
    print(a/b)
    # print("Resource closed")
    k = int(input("Enter a number"))
    print(k)
# except Exception as a:
except ZeroDivisionError as a:
    print("Hey, you cannot divide a number by zero",a)
    # print("Resource closed")
# print("bye")
except ValueError:
    print("Invalid input")
except Exception:
    print("something went wrong")
finally:
    print("Resource closed")
