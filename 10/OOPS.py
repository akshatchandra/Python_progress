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


class student:
    school='xyz'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    # def get_m1(self):
    #     return self.m1
    # def set_m1(self,value):
    #     self.m1=value
    @classmethod
    def getschool(cls):
        return cls.school

    @staticmethod
    def info():
        print("abjnjcavovihohv")

s1 = student(32,23,12)
s2 = student(23,11,21)

print(s1.avg())
print(s2.avg())
print(student.info())














