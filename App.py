def LlenarPosiciones():
    posiciones={}
    columnas=["A","B","C"]
    for i in range(3):
        for j in range(3):
            valor=f"{i+1}{columnas[j]}"
            posiciones[valor]="-"
    return posiciones

posiciones=LlenarPosiciones()

def DibujarTablero():
    columnas=["A","B","C"]
    print("    A    B    C")
    for i in range(3):
        print(f"{i+1} ",end="")
        for j in range(3):
            valor=f"{i+1}{columnas[j]}"
            print(f"| {posiciones[valor]} |",end="")
        print()
        if i<2:
            print("  ---------------")

def ComprobarEntrada(jugador,modo):
    import random
    ok=False
    while not ok:
        print(f"\nTurno jugador {jugador}")
        if modo==True and jugador=="O":
            libres=[k for k,v in posiciones.items() if v=="-"]
            posicion=random.choice(libres)
        else:
            posicion=input("Introduce la posción : ")

        ok=ComprobarPosicion(posicion,jugador)

def ComprobarPosicion(posicion,jugador):
    if posicion in posiciones.keys():
        if posiciones[posicion]=="-":
            posiciones[posicion]=jugador
            print("Ficha colocada")
            return True
        else:
            print("Posición ocupada")
            return False
    else:
        print("Posición no valida")
        return False

def ComprobarGanador(jugador):
    Filas=[0,0,0]
    Columnas=[0,0,0]
    Diagonales=[0,0]
    Letras=["A","B","C"]

    for i,j in posiciones.items():
        if j==jugador:
            aux1=int(i[0:1])-1
            aux2=Letras.index(i[1:2])
            Filas[aux1]+=1
            Columnas[aux2]+=1
            if aux1==aux2:
                Diagonales[0]+=1
            if aux1+aux2==2:
                Diagonales[1]+=1


    if 3 in Filas or 3 in Columnas or 3 in Diagonales:
        DibujarTablero()
        print(f"\n!El jugador {jugador} ha ganado¡")
        return True
    return False
            
def ElegirModo():
    while True:
        print("1. Modo individual")
        print("2. Modo 2 Jugadores")
        modo=input("Opcion : ")     
        match modo:
            case "1":
                return True
            case "2":
                return False
            case _:
                print("Elige una de las opciones")

def Jugar():
    print("-- Tres en raya --")
    Modo=ElegirModo()
    Jugador="X"
    FichasX=3
    FichasO=3
    ok=False

    while not ok and (FichasO>0 or FichasX>0):
        DibujarTablero()
        ComprobarEntrada(Jugador,Modo)
        ok=ComprobarGanador(Jugador)
        if Jugador=="X":
            FichasX-=1
            Jugador="O"
        else:
            FichasO-=1
            Jugador="X"
    if not ok:
        DibujarTablero()
        print("!Ha ocurrido un empate!")

Jugar()


