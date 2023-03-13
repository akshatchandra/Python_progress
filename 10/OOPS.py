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

class A:
    def feature1(self):
        print("F1 working")
    def feature2(self):
        print("F2 working")

class B(A):
    def feature3(self):
        print("F3 working")

    def feature4(self):
        print("F4 working")

class D:
    def feature6(self):
        print("F6 working")

class C(B,D):
    def feature5(self):
        print("F5 working")


a1 = A()
a1.feature2()
a1.feature1()

b1 = B()

c1 = C()
c1.feature6()









