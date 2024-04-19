def funcion(x,m,b):
    #Funcon que calcula la pendiente de una recta
    resultado=m*x+b
    return resultado

def main():
#Funcion principal
    x=float(input("Ingrese el valor de x: "))
    m=float(input("Ingrese el valor de m: "))
    b=float(input("Ingrese el valor de b: "))
    print("el resultado es:", funcion(x,m,b))
    X=[x for x in range(0,10)]
    Y=[funcion(x,m,b) for x in X]
    print(X)
    print(Y)
    print(list(zip(X,Y)))
    #función zip para unir dos listas, como un zipper jajaja
lista="241 220 249 209 258 194 251 212 237 245 238 185 210 209 210 187 194 201 198 218 225 195 199 190 248 255 183 175 203 245 213 178 195 235 236 175 249 220 245 190"
arreglo=list(lista.split(" "))
print(arreglo)
print(arreglo[0:5])

