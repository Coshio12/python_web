import math as m
class Figura:
    def __init__(self, nombre):
         self.nombre = nombre
        
    def area(self):
        pass
    def __str__(self):
        return f'Nombre: {self.nombre}'
    
    def perimetro(self):
        pass
    
    def __str__(self):
        return f'{self.nombre}'

class Rectangulo(Figura):
    
    def __init__(self, base, altura):
        self.nombre = __class__.__name__
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)

    def __str__(self):
        return f'{self.nombre}[base:{self.base}, altura:{self.altura}]'

class Circulo(Figura):
    def __init__(self,radio):
        self.nombre = __class__.__name__
        self.radio = radio
        
    def area(self):
        return m.pi * (self.radio**2)
    
    def perimetro(self):
        return 2 * m.pi * self.radio
    
    def __str__(self):
        return f'{self.nombre}[radio:{self.radio}]'
    
def probar_figura(Figura):
    print('Estado del objeto: ',Figura)
    print('Area: ', Figura.area())
    print('Perimetro: ',Figura.perimetro())
