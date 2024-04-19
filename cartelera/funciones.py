import csv
from datetime import datetime
import unicodedata

def carga_csv(nombre_archivo:str)->list:
    '''
    Carga archivo csv y regresa una lista 
    '''
    lista = []
    with open(nombre_archivo,'r',encoding="utf-8") as archivo:
        lista = list(csv.DictReader(archivo))
    return lista

def peliculas_mas_recientes(lista_peliculas:list)->list:
    '''Regresa las películas de más reciente estreno'''
    listap = []
    hoy = datetime.now()
    for pelicula in lista_peliculas:
        #print(pelicula['titulo']," - ",pelicula['fecha_estreno'])
        estreno = pelicula['fecha_estreno']
        estreno = datetime.strptime(estreno,"%Y/%m/%d")
        diferencia = hoy - estreno
        pelicula['dias_desde_estreno'] = diferencia.days
    lista_sorted = sorted(lista_peliculas, key=lambda x: x['dias_desde_estreno'],reverse=False)
    listap = lista_sorted[:5]
    return listap

def crea_diccionario_años(lista_peliculas:list)->dict:
    dic_años = {}
    for pelicula in lista_peliculas:
        year = pelicula['fecha_estreno']
        year = year.split("/")[0]
        if year in dic_años:
            dic_años[year].append(pelicula)
        else:
            dic_años[year] = [pelicula]
    dic_años = {k: v for k, v in reversed(sorted(dic_años.items(), key=lambda item: item[0]))}
    return dic_años
def crea_diccionario_letra(lista_peliculas:list)->dict:
    dic_letter = {}
    for pelicula in lista_peliculas:
        letra = pelicula['titulo']
        letra = letra[0]
        if letra in dic_letter:
            dic_letter[letra].append(pelicula)
        else:
            dic_letter[letra] = [pelicula]
    dic_letter = {k: v for k, v in sorted(dic_letter.items(), key=lambda item: item[0])}
    return dic_letter




def crea_diccionario_peliculas(lista_peliculas:list)->dict:
    ''' Crea diccionario de peliculas a partir de
        la lista de peliculas
        {"id_pelicula" ={diccionario_pelicula}}
    '''
    d = {}
    for pelicula in lista_peliculas:
        key = pelicula["id"]
        d[key] = pelicula # key,value
    return d

def crea_diccionario_genero(lista_peliculas:list)->dict:
    ''' Crea diccionario de generos a partir de
        la lista de peliculas
        {"genero" =[lista_peliculas]}
    '''
    d = {}
    for pelicula in lista_peliculas:
        keys = pelicula["genero"]
        keys = unicodedata.normalize('NFD', keys).encode('ascii', 'ignore').decode('utf-8')
        keys = keys.upper()
        keys = keys.split(",")
        for key in keys:
            key = key.strip()
            if key in d:
                d[key].append(pelicula)
            else:
                d[key] = [pelicula]
    d = {k: v for k, v in sorted(d.items(), key=lambda item: item[0])}
    return d

if __name__ == "__main__":
    lista =carga_csv("cartelera_2024.csv")
    #lista =carga_csv("cartelera_estrenos.csv")
    #print(lista)
    print("..........")
    lista5 = peliculas_mas_recientes(lista)
    # for pelicula in lista5:
    #     print(f"{pelicula['titulo']} - {pelicula['fecha_estreno']} {pelicula['dias_desde_estreno']}")
    # d = crea_diccionario_peliculas(lista)
    # print(f"Dune 2: {d['Dune2']}")

    d = crea_diccionario_genero(lista)
    # for genero,lista in d.items():
    #     print(f"Genero:{genero} | Peliculas:{len(lista)}")
    dic = crea_diccionario_letra(lista)
    for k,v in dic.items():
        print(f"Letra: {k} Peliculas: {v}")
