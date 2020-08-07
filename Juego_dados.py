from os import system, path, sys
import pickle
import random

jugadores = []
puntaje_para_ganar = 100
jugador_player = 0
puntaje1 = 0
puntaje2 = 0
# puntajes_maximos = ["", 0]

def buscar_jugador(nom):
    pos = 0
    jugador = None
    while pos < len(jugadores) and jugador == None:
        jds = jugadores[pos]
        if jds["nombre"] == nom:
            jugador = jds
        pos += 1
    return jugador

def buscar_jugador2(nom2):
    pos = 0
    jugador2 = None
    while pos < len(jugadores) and jugador2 == None:
        jds = jugadores[pos]
        if jds["nombre"] == nom2:
            jugador2 = jds
        pos += 1
    return jugador2

def nuevo_jugador():
    global jugador_player
    system("cls")
    nom = input("Ingrese el nombre del jugador 1: ")
    jugador = buscar_jugador(nom)
    if jugador != None:
        print("Jugador:", jugador["nombre"])
    print()
    nom2 = input("Ingrese el nombre del jugador 2: ")
    jugador2 = buscar_jugador2(nom2)
    if jugador2 != None:
        print("Jugador:", jugador2["nombre"])
    print()

    while jugador == None:
        print()
        print("El jugador", nom, "no existe")
        input("Presione ENTER para crear nuevo jugador")
        nombre = input("Ingrese el nombre del nuevo jugador_1: ")
        jugador = {"nombre":nombre, "partidas":0, "puntos":0}
        jugadores.append(jugador)
        print("Jugador Creado! Presione ENTER para continuar")
        print()
        print("Hola! ",nombre)
        print()
        input("Presione ENTER para continuar")

    while jugador2 == None:
        print()
        print("El jugador",nom2, "no existe")
        input("Presione ENTER para crear nuevo jugador")
        nombre2 = input("Ingrese el nombre del nuevo jugador_2: ")
        jugador2 = {"nombre":nombre2, "partidas":0, "puntos":0}
        jugadores.append(jugador2)
        print("Jugador Creado! Presione ENTER para continuar")
        print()
        print("Hola! ",nombre2)
        print()
        input("Presione ENTER para continuar")

    return jugador, jugador2

def nueva_partida():
    system("cls")
    print("BIENVENIDOS!")
    print()
    input("Presione ENTER para comenzar")
    jugador = nuevo_jugador()
    print()
    print("EL PUNTAJE PARA GANAR ES: " , str(puntaje_para_ganar))
    print()
    jugar = input("Presione Enter Para Tirar Dados")
    jugador == jugar
    print("Comenzó la partida:")
    turno_jugador_1 = True
    puntos_turno = turno(turno_jugador_1)
    return puntos_turno
# jugador.partidas += partidas
# guardar_jugadores()
# # guardar_puntajes_maximos()

def turno(turno_jugador_1):
    resp = "S"
    total_tiro = 0
    continuar = True
    tirada = 1
    puntaje1 =0
    puntaje2 = 0
    while (continuar):
        if (turno_jugador_1):
            print("Turno jugador 1")
            tirada = obtener_puntaje()
            if(tirada==0):
                total_tiro=0
                puntajes1 =total_tiro
            else:
                total_tiro += tirada
                puntajes1 = total_tiro
            print ("Puntaje de jugador 1:", puntajes1)
            print()

        else:
            print("Turno jugador 2")
            tirada = obtener_puntaje()
            if(tirada==0):
                total_tiro =0
                puntajes2=total_tiro
            else:
                total_tiro += tirada
                puntajes2 = total_tiro
            print ("Puntaje de jugador 2:", puntajes2)
            print ()

        if  puntaje1 + total_tiro >= puntaje_para_ganar or puntaje2 + total_tiro >= puntaje_para_ganar:
            continuar = False
            if(turno_jugador_1):
                print("HA GANADO EL JUGADOR 1")
                input("Presione ENTER para salir")
            else:
                print("HA GANADO EL JUGADOR 2")
                input("Presione ENTER para salir")
        elif total_tiro ==0:
            turno_jugador_1 = not(turno_jugador_1)

        else:
            resp = str.upper(input("Desea seguir tirando? (S/N)"))
            if(resp=="N"):
                print ()
                resp2 = str.upper(input("Desea salir del juego? (S/N)"))
                if (resp2=="N"):
                    turno_jugador_1 = not(turno_jugador_1)
                else:
                    print ()
                    print ()
                    print ("LA PARTIDA FINALIZO")
                    continuar=False
                    input("Presione ENTER para continuar")
    return puntaje1, puntaje2

def obtener_puntaje():
    dados = tirar_dados()
    if dados[0]:
        return obtener_puntaje
    else:
        return 0

    '''
    elif dados[0]==dados[1] or dados[1]==dados[2] or dados[0]==dados[2]:
        return 500
    elif dados[0]==1 and dados[1]==6 or dados[0]==6 and dados[1]==1 or dados[1]==1 and dados[2]==6 or dados[1]==6 and dados[2]==1 or dados[0]==1 and dados[2]==6 or dados[1]==6 and dados[2]==1:
        return 100
    elif dados[0]==1 or dados[1]==1 or dados[2]==1 or dados[0]==6 or dados[1]==6 or dados[2]==6:
        return 50
    '''

def tirar_dados():
    dados  = [random.randint(1,12),]
    print("dado 1:",dados[0])
    return dados

#def maximo_puntaje():
    #system("cls")
    #print("El Maximo Puntaje de Todos Los Tiempos es:")
    #for jugador in jugadores:
    #    pts =
    #    print(jugador["nombre"], "puntos", pts)
    #print()
    #input("Presione ENTER para continuar")
    #return pts

def listar_jugadores(jugadores):
    system("cls")
    print("Nombre  Partidas")
    for jugador in jugadores:
        print(jugador["nombre"], jugador["partidas"])
    print()
    input("Presione ENTER para continuar")

def cambiar_puntaje():
    system ("cls")
    global puntaje_para_ganar
    print()
    puntaje_nuevo = int(input("Escriba puntaje maximo del juego: "))
    puntaje_para_ganar == int(puntaje_nuevo)
    return int(puntaje_nuevo)

def guardar_jugadores():
    ruta_archivo = path.join(sys.path[0], "kamikaze.bin")
    archivo = open(ruta_archivo, "wb+")
    pickle.dump(jugadores,archivo)
    archivo.close()

def cargar_jugadores():
    global jugadores
    ruta_archivo = path.join(sys.path[0], "kamikaze.bin")
    if path.isfile(ruta_archivo):
        archivo = open(ruta_archivo, "rb+")
        jugadores = pickle.load(archivo)
        archivo.close()
    else:
        jugadores = []

# def guardar_puntajes_maximos ():
#     ruta_archivo = path.join (sys.path[0], "maximos.bin")
#     archivo = open(ruta_archivo, "wb")
#     pickle.dump (puntajes_maximos,archivo)
#     archivo.close()
# def cargar_puntajes_maximos ():
#     global puntajes_maximos
#     ruta_archivo = path.join (sys.path[0], "maximos.bin")
#     if path.isfile(ruta_archivo):
#         archivo = open(ruta_archivo, "rb")
#         puntajes_maximos = pickle.load (archivo)
#         archivo.close ()
#     else :
#         puntajes_maximos = {}

def mostrar_menu():
    system("cls")
    print("1. Nueva Partida")
    print("2. Lista de jugadores")
    print("3. Maximo puntaje de todos los tiempos")
    print("4. Cambiar puntaje para ganar partidas")
    print("5. Guardar y Salir")
    print()

def pedir_opcion():
    opcion = input("Ingrese una opción: ")
    while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5":
        mostrar_menu()
        print("Opción inválida")
        opcion = input("Ingrese una opción: ")
    return opcion

#dados = tirar_dados()
cargar_jugadores()
# cargar_puntajes_maximos()
mostrar_menu()
opcion = pedir_opcion()
while opcion != "5":
    if opcion == "1":
        nueva_partida()
        print("opcion 1")
    elif opcion == "2":
        listar_jugadores(jugadores) # FALTA ARREGLAR ESO
        print("opcion 2")
    elif opcion == "3":
        maximo_puntaje() #FALTA HACER ESTO
        print("opcion 3")
    elif opcion == "4":
        puntaje_para_ganar = cambiar_puntaje()
        print("opcion 4")
    elif opcion == "5":
        guardar_jugadores()
        print("opcion 5")
    mostrar_menu()
    opcion = pedir_opcion()

guardar_jugadores()

print("Adiós!")
