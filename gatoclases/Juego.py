from Jugador import Jugador
from tablero import Tablero
class Juego:
    def __init__(self,tablero:Tablero,jugador1:Jugador,jugador2:Jugador):
        self.tablero=tablero
        self.jugador1=jugador1
        self.jugador2=jugador2
        self.turno=0

    def inicia_juego(self):
        self.tablero.reset_tablero()
        while self.turno<9:
            self.tablero.display_tablero()
            ganador=self.jugar(moviendo=self.jugador1,esperando=self.jugador2)
        if ganador!=True:
            ganador=self.jugar(moviendo=self.jugador2,esperando=self.jugador1)
            if ganador:
                self.turno+=1
        else:
            self.turno+=1



    def jugar(self, moviendo:Jugador, esperando:Jugador):
        ganador=False
        mov=False
        while mov==False:
            print(f"Juega: {moviendo.nombre}")
            mov=self.tablero.juega_usuario(moviendo)
        self.tablero.display_tablero()
        if self.tablero.check_winner():
            moviendo.juegos["ganados"]+=1
            esperando.juegos["perdidos"]+=1
            ganador=True
            print(f"Ganador: {moviendo.nombre}")
        self.turno+=1
        return ganador

if __name__=="__main__":
    simbolos=["X","O"]
    j1=Jugador("Juan","X",simbolos)
    j2=Jugador("Pedro","O",simbolos)
    t=Tablero()
    j=Juego(t,j1,j2)
    j.inicia_juego()
