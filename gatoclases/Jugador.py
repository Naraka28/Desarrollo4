class Jugador:
    def __init__(self, nombre, simbolo,lista_simbolo):
        self.nombre = nombre
        simbolo = str(simbolo.upper())
        if len(lista_simbolo)==1:
            self.simbolo = lista_simbolo.pop()
        elif simbolo not in lista_simbolo:
            self.simbolo=lista_simbolo.pop()
        else:
            idx=lista_simbolo.index(simbolo)
            self.simbolo=lista_simbolo.pop(idx)
        self.juegos={"ganados":0,"perdidos":0,"empatados":0}

    def __str__(self) -> str:
        g=self.juegos["ganados"]
        p=self.juegos["perdidos"]
        e=self.juegos["empatados"]
        return f"Jugador: {self.nombre} Simbolo: {self.simbolo} Juegos: G:{g} P:{p} E:{e}"

if __name__=="__main__":
    simbolos=["X","Y"]
    j1=Jugador("Juan","X",simbolos)
    j2=Jugador("Pedro","P",simbolos)
    print(j1)
    print(j2)