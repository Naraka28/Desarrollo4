'''
Logica del programa del gato
'''
import random


tablero=[x for x in range(0,9)]
tab_dict={x:str(x) for x in tablero}
def display_tablero(tab:dict):
    print(f" {tab[0]} | {tab[1]} | {tab[2]} ")
    print("---+---+---")
    print(f" {tab[3]} | {tab[4]} | {tab[5]} ")
    print("---+---+---")
    print(f" {tab[6]} | {tab[7]} | {tab[8]} ")

def ia(board:dict):
    occupied = True
    while occupied==True:
        r=random.choice(list(board.keys()))
        if board[r]==str(r):
            occupied=False
            board[r]="O"

def juega_usuario(tab):
    turno_correcto=False
    usuario = input("Escoja celda: ")
    usuario = int(usuario)
    if usuario in tab:
        if tab[usuario]== str(usuario):
            tab[usuario]="X"
            turno_correcto=True
        else:
            print(f"Posicion {usuario} ya esta ocupada")
            print("Eliga otra opción")
    return turno_correcto

def check_winner(tab,lista_lineas):
    for comb in lista_lineas:
        if tab[comb[0]]==tab[comb[1]]==tab[comb[2]]:
            return True
        return False

def game(tab:dict):
    diccionario = {'ganador':''}
    lista_combinaciones = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    turnos=0
    while turnos<=9:
        display_tablero(tab)
        correcto = juega_usuario(tab)
        if correcto:
            turnos+=1
            gana = check_winner(tab,lista_combinaciones)
            if gana == True:
                diccionario['ganador']='X'
                print("Gano el usuario!")
                break
            ia(tab)
            gana = check_winner(tab,lista_combinaciones)
            if gana==True:
                diccionario['ganador']='O'
                print("Gano la maquina!")
                break
            turnos+=1
        display_tablero(tab)
    return diccionario

#print(f"tablero:{tablero}")
#print(f"tab_dict:{tab_dict}")
#display_tablero(tab_dict)

if __name__=="__main__":
    d = game(tab_dict)
    if d ['ganador'] != '':
        print(f"Ganador: {d['ganador']}")
    else:
        print("Empate")