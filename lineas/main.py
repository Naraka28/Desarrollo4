import linea.linea as linea
import matplotlib.pyplot as mat

if __name__=="__main__":
    X=[x for x in range(10)]
    m=2
    b=3
    Y=linea.calcula_y(X,m,b)
    mat.plot(X,Y)
    mat.show()

