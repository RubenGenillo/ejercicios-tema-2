class punto():
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return("({},{})".format(self.x, self.y))
    
    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return("El punto esta sobre el origen")
        elif self.x == 0:
            return("El punto esta sobre el eje Y")
        elif self.y == 0:
            return("El punto esta sobre el eje X")
        elif self.x > 0 and self.y > 0:
            return("El punto esta en el primer cuadrante")
        elif self.x < 0 and self.y > 0:
            return("El punto esta en el segundo cuadrante")
        elif self.x < 0 and self.y < 0:
            return("El punto esta en el tercer cuadrante")
        else:
            return("El punto esta en el cuarto cuadrante")

    def vector(self, otro):
        return punto(self.x - otro.x, self.y - otro.y)

    def distancia(self, otro):
        return pow(pow((self.x - otro.x), 2) + pow((self.y - otro.y), 2) , 1/2)   



class rectangulo():

    def __init__(self, punto1 = punto(), punto2 = punto()):
        self.punto1 = punto1
        self.punto2 = punto2

    def base(self):
        return abs(self.punto1.x - self.punto2.x)
    
    def altura(self):
        return abs(self.punto1.y - self.punto2.y)
    
    def area(self):
        return self.base() * self.altura()
    


if __name__ == "__main__":
    A = punto(2,3)
    B = punto(5,5)
    C = punto(-3,-1)
    D = punto(0,0)
    print(A)
    print(B)
    print(C)
    print(D)
    print(A.cuadrante())
    print(C.cuadrante())
    print(D.cuadrante())
    print(A.vector(B))
    print(B.vector(A))
    print(A.distancia(B))
    print(B.distancia(A))
    print("La distancia de A del origen es: {}, la distancia de B del origen es: {} y la distancia de C del origen es: {}, por lo que B es el punto más alejado del origen".format(A.distancia(D), B.distancia(D), C.distancia(D)))
    rectangulo1 = rectangulo(A, B)
    print("La base del rectangulo es: {}, la altura es: {} y el area es: {}".format(rectangulo1.base(), rectangulo1.altura(), rectangulo1.area()))
