import time
# Guarda la lista de Usuarios registrados, contiene dos sublistas, la que se encuentra en la posición 0 es para los administradores
# y la que se encuentra en la posición 1 para los jugadores.
usersList = [[{"name": "Dayanna", "id": "dram", "password": "123", "typeRol": "Administrador"}],
             [{"name":"Selena","nickname":"selena","id": "selena", "password":"1234","typeRol":"Jugador","juegosJugados":0,"puntosGanados":0}]]

userLogged = [] # Guarda el id del Usuario que esta logueado en ese momento

# Guarda la lista de palabras con C, S y Z.
wordsListCSZ = [["depre_ivo","s","depresivo"],["Flore_er","c","florecer"]]

# Pide los datos del usuario administrador como su: nombre, identificador y contraseña.
def registerAdministrator():
    print("Datos del Administrador:")
    name = (input("1) Nombre del Administrador: "))
    id = input("2) Identificador: ")
    password = (input("3) Contraseña:"))
    typeRol = "Administrador"

    print("\n")

    registerUserAdministrator(name, id, password, typeRol) # Llama a la función que agrega mediante un diccionario
                                                           # ususarios administradores.
    userAdministrator()                                    # Llama a la función de administrar ususarios.


# Pide los datos al usuario jugador como su: nombre, alias, identificador y contraseña.
def registerPlayers(): # Pide datos al usuario jugador para registrarlo
    print("Datos del Jugador:")
    name = (input("1) Nombre del Jugador: "))
    nickname = (input("2) Nickname/Alias: "))
    id = input("3) Identificador: ")
    password = (input("4) Contraseña:"))
    typeRol = "Jugador"

    print("\n")

    registerUserPlayers(name, nickname, id, password, typeRol) # Llama a la función que agrega mediante un diccionario
                                                               # ususarios jugadores.
    userAdministrator()                                        # Llama a la función de administrar ususarios.


def registerUserPlayers(name, nickname, id, password, typeRol):
    newUser = {}
    newUser["name"] = name
    newUser["nickname"] = nickname
    newUser["id"] = id
    newUser["password"] = password
    newUser["typeRol"] = typeRol
    newUser["juegosJugados"] = 0
    newUser["puntosGanados"] = 0

    usersList[1].append(newUser)

def registerUserAdministrator(name, id, password, typeRol):
    newUser = {}
    newUser["name"] = name
    newUser["id"] = id
    newUser["password"] = password
    newUser["typeRol"] = typeRol

    usersList[0].append(newUser)




def mainLogin():
    print(">>> Menú de inicio de sesión <<<\n"
          "Por favor, ingrese su:")
    iD = input("1) Identificador: ")
    password = input("2) Contraseña: ")

    print("\n")

    loginUser(iD,password)

def loginUser(id,password):
    for i in range(len(usersList)):
        for user in usersList[i]:

                if user["id"]== id:
                    if  user["password"]== password:
                        userLogged.append(id)
                        verifyTyoeRol(user)
                    else:
                        pass


def verifyTyoeRol(user):

    if user["typeRol"] == "Administrador":
        print(user["name"] + ", usted tiene el rol de: " + user["typeRol"] + ".")
        print("\n")
        administratorMenu()
    elif user["typeRol"] == "Jugador":
        print(user["nickname"] + ", usted tiene el rol de: " + user["typeRol"] + ".")
        print("\n")
        playerMenu()


def mainMenu():

    run_program = True

    while(run_program):
        print("***** Bienvenido al Juego Corrector de Ortografía ***** \n"
                            "1) Iniciar Sesión.\n"
                            "2) Salir. ")

        option = input(str("→ Opción: "))

        print("\n")

        if(option == "1"):
            mainLogin()
        elif option == "2":
            run_program = False


def addTypeUser():
    print("¿Qué usuario desea agregar?\n"
          "1) Administrador.\n"
          "2) Jugador.\n"
          "3) Regresar.")
    option = int(input("→ Usuario: "))

    print("\n")

    if option == 1:
        registerAdministrator()

    elif option == 2:
        registerPlayers()
    elif option == 3:
        userAdministrator()
    else:
        addTypeUser()


def removeUsersAdministrators():

    count = 1

    for users in usersList[0]:
        print(str(count) + ") Identificador: " + users["id"] + " (" + users["name"] + ").")
        count += 1

    delete = int(input("→ Digite el número de usuario que desea eliminar: "))

    count2 = 1
    for y in usersList[0]:
        if delete == count2:
            usersList[0].pop(count2 -1)
        count2 +=1

        print("¡El usuario ha sido eliminado!")
        print("\n")

    userAdministrator()


def removeUsersPlayers():
    count = 1

    for users in usersList[1]:
        print(str(count) + ") Identificador: " + users["id"] + "(" + users["name"] + ").")
        count += 1

    delete = int(input("→ Digite el número de usuario que desea eliminar: "))

    count2 = 1
    for y in usersList[1]:
        if delete == count2:
            usersList[1].pop(count2 -1)
        count2 += 1

    print("¡El usuario ha sido eliminado!")
    print("\n")

    userAdministrator()


def removeMenu():
    print("¿Qué usuario desea eliminar?")
    print("1) Administrador.\n"
          "2) Jugador.\n"
          "3) Regresar.")

    option = int(input("→ Usuario: "))

    if option == 1:
        removeUsersAdministrators()
    elif option == 2:
        removeUsersPlayers()
    elif option == 3:
        userAdministrator()
    else:
        removeMenu()



def userAdministrator():
    print("----- Menú de Administrador de Usisarios ------")
    print("1) Crear usuario.\n"
          "2) Borrar usuario.\n"
          "3) Ver lista de usuarios.\n"
          "4) Regresar al menú del admistrador.")

    option = int(input("→ Opción: "))

    print("\n")

    if option == 1:
        addTypeUser()
    elif option == 2:
        removeMenu()
    elif option == 3:
        print(userLogged)
        administratorMenu()
    elif option == 4:
        administratorMenu()
    else:
        userAdministrator()


def seePlayerListAdministrator():
    jugador = 1
    for player in usersList[1]:
        print(str(jugador) + ")" + " Identificador: " + player["id"] + " / " + "Nombre del jugador: " + player["name"]
                  + " / " + "Nickname: " + player["nickname"] + ".")
        jugador +=1

    print("\n")

    consultsAdministratror()


def seePlayerListPlayers():
    jugador = 1
    for player in usersList[1]:
        print(str(jugador) + ")" + " Identificador: " + player["id"] + " / " + "Nombre del jugador: " + player["name"]
                  + " / " + "Nickname: " + player["nickname"] + ".")
        jugador +=1

    print("\n")

    consultsplayer()



def consultsAdministratror():
    print("----- Menú de Consultas ------")
    print("1) Ver lista de jugadores.\n"
          "2) Ver los mejores 10 jugadores.\n"
          "3) Promedio de juegos jugados.\n"
          "4) Ver jugadores con menor cantidad de puntos.\n"
          "5) Regresar al menú administrador.")

    option = int(input("→ Opción: "))

    print("\n")

    if option == 1:
        seePlayerListAdministrator()
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        pass
    elif option == 5:
        administratorMenu()
    else:
        consultsAdministratror()


def administratorMenu():
    print("----- Menú del Administrador -----")
    print("1) Administrar usuarios.\n" 
          "2) Consultas.\n"
          "3) Cerrar sesión.")

    opcion = input(str("→ Opción: "))

    print("\n")

    if opcion == "1":
        userAdministrator()

    elif opcion == "2":
        consultsAdministratror()

    elif opcion == "3" :
        del (userLogged[:])
        mainMenu()

    else:
        administratorMenu()


def modifyNickname():

    for y in usersList[1]:
        if y["id"] == userLogged[0]:
            newNick = input("Ingrese su nuevo nickname(" + y["nickname"] + "): " )
            y["nickname"] = newNick
    playerMenu()

def userDataLogin():
    for i in usersList[1]:
        if i["id"] == userLogged[0]:
            print("Nombre: " + i["name"] + "." + "\n" + "Alias: " + i["nickname"] + "." + "\n" + "Juegos jugados: "
                  + str(i["juegosJugados"])+ "." + "\n" + "Puntos Ganados: " + str(i["puntosGanados"]) + ".")
    consultsplayer()




def consultsplayer():
    print("----- Menú de Consultas ------")
    print("1) Ver lista de jugadores.\n"
          "2) Ver datos de la cuenta.\n"
          "3) Regresar al menú jugador.")

    option = int(input("→ Opción: "))

    print("\n")

    if option == 1:
        seePlayerListPlayers()
    elif option == 2:
        userDataLogin()
    elif option == 3:
        playerMenu()
    else:
        consultsplayer()
def categoryCSZ ():
    print("Instrucciones: Usted debera completar la palabra\n"
          "con la letra que considera es la correcta(C,S O Z)\n"
          "tendra un tiempo maximo de 15 segundos para responder\n"
          "cada palabra, si sobrepasa el tiempo maximo, la palabra\n"
          "no contara y se le restaran puntos")
    print("Para salir, presione la letra Q")
    time.sleep(10)
    print("--------------------------------------------------")
    time.sleep(1.5)

    for x in wordsListCSZ:
        start = time.time()
        print("La palabra es: "+ str(x[0]))
        letra = input(str("Cuál letra falta?: "))
        final = time.time()
        timer = round(final - start,0)



        if letra == "q" or letra == "Q":
            menuPlayComplete()

        elif timer > 15 and letra == (x[1]):
            for i in usersList[1]:
                if i["id"] == userLogged[0]:
                    i["puntosGanados"] = i["puntosGanados"] -2
                    print("Lo sentimos, no respondió en el tiempo establecido. La palabra era: " + str(x[2]) + "." )
                    print(timer)
                    print("\n")

        elif letra == (x[1]):
            for i in usersList[1]:
                if i["id"] == userLogged[0]:
                    i["puntosGanados"] = i["puntosGanados"] +2
                    print("Es correcto, ganó 2 puntos.")
                    print("\n")

        elif timer > 15 and letra != (x[1]):
            for i in usersList[1]:
                if i["id"] == userLogged[0]:
                    i["puntosGanados"] = i["puntosGanados"] -2
                    print("Lo sentimos, no respondió en el tiempo establecido. La palabra era: " + str(x[2]) + "." )
                    print(timer)
                    print("\n")


        else:
            for i in usersList[1]:
                if i["id"] == userLogged[0]:
                    i["puntosGanados"] -=1
            print("Es incorrecto, perdió 1 punto, la palabra era: " + str(x[2]) + ".")
            print("\n")



    menuPlayComplete()

def menuPlayComplete():
    print("----- Menú del juego -----")
    print("¿Qué categoria desea jugar?:\n"
          "1) Categoria C,S,Z.\n"
          "2) Categoria G,J.\n"
          "3) Categoria Y,LL.\n"
          "4) Categoria B,V,W.\n"
          "5) Regresar al menú de juego.")

    opcion = input(str("→ Opción: "))

    print("\n")

    if opcion == "1":
        for i in usersList[1]:
            if i["id"] == userLogged[0]:
                i["juegosJugados"] = i["juegosJugados"] + 1
                categoryCSZ()

    elif opcion == "2":
        pass

    elif opcion == "3":
        playerMenu()
    elif opcion == "4":
        pass
    elif opcion == "5":
        menuPlay()
    else:
        menuPlayComplete()


def menuPlay():
    print("----- Menú de Juego -----")
    print("¿Qué desea realizar?:\n"
          "1) Jugar completando.\n"
          "2) Jugar tildando.\n"
          "3) Regresar al menú del jugador.\n")

    opcion = input(str("→ Opción: "))

    print("\n")

    if opcion == "1":
        menuPlayComplete()

    elif opcion == "2":
        pass

    elif opcion == "3":
        playerMenu()

    else:
        menuPlay()

def playerMenu():
    print("----- Menú del Jugador -----")
    print("¿Qué desea realizar?:\n"
          "1) Jugar.\n"
          "2) Cambiar el nickname.\n"
          "3) Consultas.\n"
          "4) Cerrar sesión.")


    opcion = input(str("→ Opción: "))

    print("\n")

    if opcion == "1":
        menuPlay()

    elif opcion == "2":
        modifyNickname()

    elif opcion == "3":
        consultsplayer()

    elif opcion == "4":
        del (userLogged[:])
        mainMenu()

    else:
        playerMenu()


mainMenu()