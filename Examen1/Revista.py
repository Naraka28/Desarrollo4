#Daniel Iván Estrada Neri 20/02/24
class Revista:
    def __init__(self,titulo:str,catalogo:str):
        self.titulo = titulo
        self.catalogos = set()
        self.catalogos.add(catalogo)

    def __str__(self):
        return f"{self.titulo} - {self.catalogos}"

    def leer_csv(self,archivo:str):
        with open(archivo, "r",encoding="utf8") as file_csv:
            lista_titulos = []
            for linea in file_csv:
                titulo=linea.strip().lower()
                lista_titulos.append(titulo)
        return lista_titulos

    def crear_revistas(self,lista_revistas:list,catalogo:str)->list:
        lista = []
        for revista in lista_revistas:
            lista.append(Revista(revista,catalogo))
        return lista

    def crea_diccionario_revistas(self,lista_revistas: list) -> dict:
        diccionario = {}
        for revista in lista_revistas:
            palabras_titulo = revista.titulo.split()
            for palabra in palabras_titulo:
                if palabra in diccionario:
                    diccionario[palabra].append(revista)
                else:
                    diccionario[palabra] = [revista]
        return diccionario


if (__name__=="__main__"):
    Revista1 = Revista("Revista1","Catalogo1")
    lista=Revista1.leer_csv("CONACYT_RadGridExport.csv")
    Revista1.crear_revistas(lista,"Conacyt")
