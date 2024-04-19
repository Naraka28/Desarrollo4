#Daniel Iván Estrada Neri 20/02/24
from Revista import Revista

def main_funcion():
    archivo="CONACYT_RadGridExport.csv"
    r = Revista("Revista1","Catalogo1")
    lista_titulo=r.leer_csv(archivo)
    catalogo="Conacyt"
    lista_de_revistas=r.crear_revistas(lista_titulo,catalogo)
    diccionario=r.crea_diccionario_revistas(lista_de_revistas)
    buscador=diccionario["acta"]
    for revista in buscador:
        print(f"{revista}")

if __name__=="__main__":
    main_funcion()
