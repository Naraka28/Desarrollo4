import random

def lee_archivo(archivo:str):
    palabras = []
    with open(archivo,"r",encoding="utf-8") as a:
        data = a.readlines()
    for palabra in data:
        palabra = palabra.strip("\n")
        palabras.append(palabra)
    return palabras

def palabra_a_diccionario(palabra:str)->list:
    ''' convierte palabra en un diccionario de letras'''
    lista = [ {letra:"_"} for letra in palabra ]
    return lista

def checa_si_gano(lista_letras:list):
    existe_underscore=False
    for dic in lista_letras:
        for k,v in dic.items():
            if v == "_":
                existe_underscore = True
    if existe_underscore == True:
        gana = False
    else:
        gana = True
    return gana

if __name__ == "__main__":
    palabras = lee_archivo("palabras.txt")
    print(palabras)
    palabra = random.choice(palabras)
    dp = palabra_a_diccionario(palabra)
    print(dp)
    gato_ = [{"g":"_"},{"a":"_"},{"t":"_"},{"o":"_"}]
    print(checa_si_gano(gato_))
    gato = [{"g":"g"},{"a":"a"},{"t":"t"},{"o":"o"}]
    print(checa_si_gano(gato))