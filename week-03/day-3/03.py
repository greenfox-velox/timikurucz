# create a pirate class
# it should have 2 methods
# drink_rum()
# hows_goin_mate()
# if the drink_rum was called at least 5 times:
# hows_goin_mate should return "Arrrr!"
# "Nothin'" otherwise

class Pirate ():
    def __init__(self):
        self.rum_num = 0
    def drink_rum(self):
        self.rum_num += 1
        return self.rum_num
    def hows_goin_mate(self):
        if self.rum_num >= 5:
            print("Arrrr!")
        else:
            print("Nothin'")

pirate1 = Pirate()
pirate1.drink_rum()
pirate1.drink_rum()
pirate1.drink_rum()
pirate1.drink_rum()
pirate1.drink_rum()
pirate1.hows_goin_mate()
