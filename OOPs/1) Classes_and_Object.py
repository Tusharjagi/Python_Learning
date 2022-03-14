class Computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is", self.cpu,self.ram)


com1 = Computer('i5', 32)
com2 = Computer('AMD 5' , 8)

com1.config()
com2.config()


