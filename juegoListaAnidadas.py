# Guarda la lista de Usuarios registrados, contiene dos sublistas, la que se encuentra en la posición 0 es para los administradores
# y la que se encuentra en la posición 1 para los jugadores.
usersList = [[{"name": "Dayanna", "id": "dram", "password": "123", "typeRol": "Administrador"}],
             [{"name":"Selena","nickname":"selena","id": "selena", "password":"1234","typeRol":"Jugador","juegosJugados":0,"puntosGanados":0}]]

# Guarda la lista de palabras.
wordsList = []

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
def registerPlayers():
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
            if user["id"] == id:
                if user["password"] == password:
                    verifyTyoeRol(user)

                else:
                    print("No le quedan intentos")
                    print("\n")
                    mainMenu()

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


def removeUsers():

    count = 1

    for i in range(len(usersList)):

        for users in usersList[i]:
            print(str(count) + ") " + users["name"] + " (" + users["typeRol"] + ").")
            count += 1

        delete = int(input("→ Digite el número de usuario que desea eliminar: "))

        count2 = 1
        if delete == count2:
            usersList.remove(count2)
            count2 +=1

            print("¡El usuario ha sido eliminado!")
            print("\n")

    userAdministrator()


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
        removeUsers()
    elif option == 3:
        print(usersList)
        administratorMenu()
    elif option == 4:
        administratorMenu()
    else:
        userAdministrator()


def seePlayerList():
    jugador = 1
    for player in usersList:
        if player["typeRol"] == "Jugador":
            print(str(jugador) + ")" + "  Identificador: " + player["id"] + " / " + "Nombre del jugador: " + player["name"]
                  + " / " + "Nickname: " + player["nickname"] + ".")
        jugador +=1

    print("\n")

    consultsAdministratror()

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
        seePlayerList()
    elif option == 2:
        pass
    elif option == 3:
        print(usersList)
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
        mainMenu()

    else:
        administratorMenu()


def modifyNickname():
   pass


def userDataLogin():
    user = mainLogin()
    for i in usersList:
        if i["id"] == user:
            print("Nombre: " + i["name"] + "." +"\n" + "Alias: " + i["nickname"] + "." + "\n" + "Juegos jugados: " + i["juegosJugados"] + "." + "\n" + "Puntos Ganados: " + i["puntosGanados"] + ".")

    consultsplayer()


def consultsplayer():
    print("----- Menú de Consultas ------")
    print("1) Ver lista de jugadores.\n"
          "2) Ver datos de la cuenta.\n"
          "3) Regresar al menú jugador.")

    option = int(input("→ Opción: "))

    print("\n")

    if option == 1:
        seePlayerList()
    elif option == 2:
        userDataLogin()
    elif option == 3:
        playerMenu()
    else:
        consultsplayer()


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
        pass

    elif opcion == "2":
        pass

    elif opcion == "3":
        consultsplayer()

    elif opcion == "4":
        mainMenu()

    else:
        playerMenu()






mainMenu()