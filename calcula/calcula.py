def suma(lista:list) ->  float:
    return sum(lista)

def promedio(lista:list) ->  float:
    return suma(lista)/len(lista)

def main(lista:list):
    print(f"Suma: {suma(lista)}")
    print(f"Promedio: {promedio(lista)}")
def moda(lista:list) ->  int:
    dic={x:0 for x in lista}
    for x in lista:
        dic[x]+=1
    return max(dic,key=lambda key:dic[key])

if __name__ == "__main__":
    listado=[x for x in range(1,11)]
    dict={x:0 for x in listado}
    print(dict[2])
