#Daniel Iván Estrada Neri 05/04/2024
import os
class Revista:
    def __init__(self,titulo:str,catalogo:str,sjr:str,
                 q:str,h_index:str,total_citas:str):
        self.titulo = titulo
        self.catalogos = set()
        self.catalogos.add(catalogo)
        self.sjr = float(sjr)
        self.q = q
        self.h_index = int(h_index)
        self.total_citas = int(total_citas)
    
    def __str__(self):
        return f'{self.titulo}|{self.catalogos}|{self.sjr}|{self.q}|{self.total_citas}'

def lee_archivo(archivo:str):
    palabras = []
    with open(archivo,"r",encoding="utf-8") as a:
        data = a.readlines()
    for palabra in data:
        palabra = palabra.strip("\n")
        palabras.append(palabra)
    return palabras

def main():
    urls = lee_archivo('urls.txt')
    print(urls)

if __name__ == '__main__':
    main()

