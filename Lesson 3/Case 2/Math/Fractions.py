class Fraction:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __add__(self, other):
        return Fraction(self.numerador * other.denominador + other.numerador * self.denominador, self.denominador * other.denominador)

    def __sub__(self, other):
        return Fraction(self.numerador * other.denominador - other.numerador * self.denominador, self.denominador * other.denominador)

    def __mul__(self, other):
        return Fraction(self.numerador * other.numerador, self.denominador * other.denominador)

    def __truediv__(self, other):
        return Fraction(self.numerador * other.denominador, self.denominador * other.numerador)

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"
