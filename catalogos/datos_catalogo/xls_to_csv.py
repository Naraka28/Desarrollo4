import pandas as pd
import os
f="/Users/danielestrada/Desarrollo de sistemas IV/catalogos/datos_catalogo"
f2="/Users/danielestrada/Desarrollo de sistemas IV/catalogos/datos_catalogo/areas"

def read_folder(folder_path:str) -> list:
    return os.listdir(folder_path)

def enter_dirs(file_list:list):
    for archivo in file_list:
        if os.path.isdir(archivo):
            lista_2=read_folder("./"+archivo)
        return lista_2

def xls_to_csv(file_list:list,path:str):
    for archivo in file_list:
        df = pd.read_excel(f'/{path}/{archivo}')
        archivo=archivo.split(".")
        archivo_csv_nombre = f'/{path}/{archivo[0]}.csv'
        df.to_csv(archivo_csv_nombre, index=False)


def main(f:str):
    lista = read_folder(f)
    dir_files = enter_dirs(lista)
    xls=[file for file in dir_files if file.endswith(".xls")]
    xls_file=[file for file in lista if file.endswith(".xls")]
    xls_to_csv(xls,f2)
    xls_to_csv(xls_file,f)

if __name__=="__main__":
    main(f)

