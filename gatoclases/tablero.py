from colorama import Fore, Back, Style, Cursor
from Jugador import Jugador
class Tablero:
    def __init__(self,color_fondo=Back.WHITE,color_rayas=Fore.LIGHTCYAN_EX, color_numeros=Fore.BLUE, color_x=Fore.RED, color_y=Fore.GREEN):
        self.lista_numero=[x for x in range(0,9)]
        self.dicc_posiciones={x:str(x) for x in self.lista_numero}
        self.combosganadores=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        self.color= {"fondo":color_fondo,"rayas":color_rayas,"X":color_x,"numeros":color_numeros,"O":color_y}


    def display_tablero(self):
        reset=Style.RESET_ALL
        bg=self.color["fondo"]
        blue=self.color["numeros"]
        board_color=self.color["rayas"]
        x_color=self.color["X"]
        o_color=self.color["O"]
        X=x_color+"X"
        O=o_color+"O"
        BD=board_color+"------------"
        BS= board_color+" | "
        d={}
        for k,v in self.dicc_posiciones.items():
            if v=="X":
                d[k]=X+BS
            elif v=="O":
                d[k]=O + BS
            else:
                d[k]=blue + str(k)+BS
        print(Cursor.POS(20,5)+f"{bg}{d[0]}{d[1]}{d[2]}{reset}")
        print(Cursor.POS(20,6)+f"{bg}{BD}{reset}")
        print(Cursor.POS(20,7)+f"{bg}{d[3]}{d[4]}{d[5]}{reset}")
        print(Cursor.POS(20,8)+f"{bg}{BD}{reset}")
        print(Cursor.POS(20,9)+f"{bg}{d[6]}{d[7]}{d[8]}{reset}")
        print(Cursor.POS(20,10)+f"{bg}{BD}{reset}")
        print(Style.RESET_ALL)

    def reset_tablero(self):
        self.dicc_posiciones={x:str(x) for x in self.lista_numero}

    def check_winner(self):
        tab=self.dicc_posiciones
        lista_lineas=self.combosganadores
        for cmb in lista_lineas:
            if (tab[cmb[0]]==tab[cmb[1]]==tab[cmb[2]]):
                return True
        return False

    def juega_usuario(self,jugador:Jugador):
        tab=self.dicc_posiciones
        turno_correcto=False
        usuario= input(Cursor.POS(1,15)+"Escoja celda:\n")
        usuario=int(usuario)
        if usuario in tab:
            if tab[usuario]== str(usuario):
                tab[usuario]=jugador.simbolo
                turno_correcto=True
            else:
                print(Cursor.POS(1,12)+f"Casilla {usuario} Ocupada \nElija otra opción\n")
        return turno_correcto

if __name__=="__main__":
    t=Tablero()
    t.display_tablero()
    t.dicc_posiciones[0]="X"
    t.dicc_posiciones[1]="X"
    t.dicc_posiciones[2]="X"
    print(t.check_winner())
    t.reset_tablero()
    t.display_tablero()
    lista_simbolos=["X","O"]
    A=Jugador("Juan","X",lista_simbolos)
    B=Jugador("Pedro","O",lista_simbolos)
    t.juega_usuario(A)
    t.display_tablero()
