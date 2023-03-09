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

class computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
        # print("in init")

    def config(self):
        # print("i5,8GB,512GB")
        print("Config is",self.cpu,self.ram)

# com1 = computer()
# com2 = computer()
com1 = computer("5",16)
com2 = computer("Ryzen 3",8)

com1.config()
com2.config()