from Revista import Revista, lee_archivo
from bs4 import BeautifulSoup
import argparse
import requests

b_url = 'https://www.scimagojr.com/'
base_url = 'https://www.scimagojr.com/journalrank.php?category=1902'
def scrap(URL:str):
    page=requests.get(URL)
    source = BeautifulSoup(page.content,'html.parser')
    return source

def get_urls(dom,url_list:list)->list:
    i = 0
    url = dom.find('div',class_='pagination_buttons')
    for anchor in url.find_all('a'):
        if i == 1:
            next = anchor['href']
            print(next)
        i+=1
    if next != '#':
        next = f"{b_url}{next}"
        url_list.append(next)
        soup = scrap(next)
        return get_urls(soup, url_list)
    return url_list

def main():
    url = 'https://www.scimagojr.com/journalrank.php?category=1706'
    urls = lee_archivo('urls.txt')
    page = scrap(urls[0])
    soup = BeautifulSoup(page.content,"html.parser")
    result = soup.find('tbody')
    lista_revistas = []
    for row in result.find_all('tr'):
        i = 0
        for col in row.find_all('td'):
            if i == 1:
                titulo = col.text
            if i == 2:
                catalogo = col.text

            if i == 3:
                sjr = col.text.split(" ")[0]
                q = col.text.split(" ")[1]

            if i == 4:
                h_index = col.text

            if i == 8:
                total_citas = col.text
            i += 1
        r= Revista(titulo,catalogo,sjr,q,h_index,total_citas)
        lista_revistas.append(r)
    parser = argparse.ArgumentParser(
        description='Procesa archivos  y genera catálogo'
    )
    parser.add_argument('h_index',
                        type=int,
                        help=''
                        )
    parser.add_argument('nombre_archivo',
                        type=str,
                        help='Ruta de la carpeta areas con JSON'
                        )

    args = parser.parse_args()
    index = args.h_index
    archivo= args.nombre_archivo
    lista_menores = hindex_menor(lista_revistas,index)
    for revista in lista_menores:
        print(revista.__str__())
    guardar_JSON(lista_revistas,archivo)


def main2():
    urls = lee_archivo('urls.txt')
    lista_total = []
    for url in urls:
        page = scrap(url)
        soup = BeautifulSoup(page.content,"html.parser")
        result = soup.find('tbody')
        lista_revistas = []
        for row in result.find_all('tr'):
            i = 0
            for col in row.find_all('td'):
                if i == 1:
                    titulo = col.text
                if i == 2:
                    catalogo = col.text
                if i == 3:
                    sjr = col.text.split(" ")[0]
                    q = col.text.split(" ")[1]
                if i == 4:
                    h_index = col.text

                if i == 8:
                    total_citas = col.text
                i += 1
            r= Revista(titulo,catalogo,sjr,q,h_index,total_citas)
            lista_revistas.append(r)
        lista_total.extend(lista_revistas)
        parser = argparse.ArgumentParser(
            description='Procesa archivos  y genera catálogo'
        )
        parser.add_argument('h_index',
                            type=int,
                            help=''
                            )
        parser.add_argument('nombre_archivo',
                            type=str,
                            help='Ruta de la carpeta areas con JSON'
                            )

        args = parser.parse_args()
        index = args.h_index
        archivo= args.nombre_archivo
        lista_menores = hindex_menor(lista_total,index)
        for revista in lista_menores:
            print(revista.__str__())
        guardar_JSON(lista_total,archivo)

def hindex_menor(lista: list, index: int):
    return [revista for revista in lista if revista.h_index < index]

def guardar_JSON(lista: list, nombre_archivo: str):
    with open(nombre_archivo, 'w') as file:
        for revista in lista:
            file.write(revista.__str__() + '\n')


if __name__ == '__main__':
    #main2()
    url_listas = []
    pag = scrap(base_url)
    urls = get_urls(pag,url_listas)
    print(urls)