def linea(x,m,b):
    return x*m+b
    

def calcula_y(X,m,b):
    Y=[linea(x,m,b)for x in X]
    return Y

if __name__=="__main__":
    X=[x for x in range(0,10)]
    m=2
    b=3
    Y=calcula_y(X,m,b)
    print(X,Y)


