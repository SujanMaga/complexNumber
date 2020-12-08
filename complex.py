# (a+bi)(c+di) = (ac-bd) + (bc+ad)i
# (a+bi)+(c+di) = (a+c) + (b+d)i

# deducing the formaula into a program.
class Complex:
    def __init__(self, r , i):
        self.real = r
        self.imaginary = i

    def __add__(self, other):
        return f"{self.real + other.real} + {self.imaginary + other.imaginary}i"

    def __mul__(self, other):
        real = (self.real * other.real) - (self.imaginary * other.imaginary)
        imaginary = (self.imaginary * other.real) + (self.real * other.imaginary)
        return f"{real} + {imaginary}i" 

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

# taking example
c1 = Complex(2, 5)
c2 = Complex(4, -3)
print (c2 * c1 )
print (c2 + c1 )
