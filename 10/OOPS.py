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
class Computer:
    # pass
    def __init__(self):
        self.name = "aks"
        self.age = 23

    def update(self):
        self.age = 32

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = Computer()
c2 = Computer()
# print(id(c1))
# print(id(c2))
c1.name = "xyz"
c1.age = 12

if c1.compare(c2):
    print("They are same")
else:
    print("They are not same")
# c1.update()
print(c1.name)
# print(c2.name)

print(c1.age)
# print(c2.age)


