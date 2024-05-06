# MRO (Method Resolution Order)
class Primera:
    def clase(self):
        print(" soy la primer clase")


class Segunda:
    def clase(self):
        print(" soy la segunda clase")


class Tercera:
    def clase(self):
        print(" soy la tercera clase")


class Cuarta:
    def clase(self):
        print(" soy la cuarta clase")


class Quinta(Tercera, Cuarta):
    def clase(self):
        print(" soy la quinta clase")


clase = Quinta()
print(Quinta.mro())
