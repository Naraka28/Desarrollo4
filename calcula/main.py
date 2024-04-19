"""
Calcula datos estadísticos de una lista, usando argumentos
"""
import argparse
import calcula

def main(listado:list, operacion:str,operaciones):
    dicc_operaciones={k:0 for k in operaciones}
    for k in operaciones:
        if k=="todas":
            dicc_operaciones[k]="print('no implementado')"
        else:
            dicc_operaciones[k]="print(f'{k}: {calcula.{k}(listado)}')"

    # dicc={"suma":"print(f'Suma: {calcula.suma(listado)}')",
    #       "promedio":"print(f'Promedio: {calcula.promedio(listado)}')",
    #       "moda":"print(f'Moda: {calcula.moda(listado)}')",
    #       "todas":f"suma: {'sin implementar'}"}
    # eval(dicc[operacion])
    # operacion=operacion.lower()

if __name__ == "__main__":
    #Declaramos nuestro parse o procesador de argumentos
    opciones=["suma","promedio","moda", "todas"]
    parser=argparse.ArgumentParser(description="Calcula el promedio de una lista y su sumatoria")
    parser.add_argument("entero",metavar="n",type=int,nargs="+",help="Hola tontin owo")
    parser.add_argument("--operacion","-o",dest="o",type=str,choices=opciones)
    args=parser.parse_args()
    print(args.entero)
    main(args.entero,args.o)
