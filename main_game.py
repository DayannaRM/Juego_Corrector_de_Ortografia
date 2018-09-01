userList = [{"name":"Dayanna","nickname":"dram","id": "dram", "password":"123","typeRol":"Administrador"},
            {"name":"Selena","nickname":"selena","id": "selanamm", "password":"semm","typeRol":"Administrador"}]




def typeRolUI():
    print("Que usuario quiere agregar?:\n"
          "1) Administrador\n"
          "2) Jugador\n"
          "3) Regresar\n")
    option = int(input("Rol: "))

    if (option == 1):
        return "Administrador"
        adminstratorOpcions()
    elif option == 2:
        return "Jugador"
        adminstratorOpcions()
    elif option == 3:
        adminstratorOpcions()

    else:
        return "Unknow"


def register():
    name = (input("1) Nombre: "))
    nickname = (input("2) Nickname: "))
    id = int(input("3) ID: "))
    password = (input("4) Password:"))
    typeRol = typeRolUI()

    registerUser(name,nickname,id,password,typeRol)



def registerUser(name,nickname,id,password,typeRol):
    newUser = {}
    newUser["name"] = name
    newUser["nickname"] = nickname
    newUser["id"] = id
    newUser["password"] = password
    newUser["typeRol"] = typeRol

    userList.append(newUser)




def userAdministrator():
    print("1) Crear usuario\n"
          "2) Borrar usuario\n"
          "3) Ver lista de usuarios\n"
          "4) Regresar")

    opcion = int(input("opcion"))

    if opcion == 1:
        register()
    elif opcion == 3:
        print(userList)


def adminstratorOpcions():
    print("1) Administrar usuarios\n"
          "2) Regresar")

    opcion = int(input("opcion: "))

    if opcion == 1:
        userAdministrator()


def loginUser(id,password):

    for user in userList:
        if user["id"] == id:
            if user["password"] == password:
                verifyTyoeRol(user)
            else:
                print("Intente de nuevo")

                #intentos = 0
                #while intentos < 4:
                #    if intentos <= 3:
                #        print("Lleva " + str(intentos)+ " intentos de 3")
                #        mainLogin()
                #        intentos+=1
                #    else:
                #        print("No le quedan intentos")'''

def verifyTyoeRol(user):
    print(user["name"] + ", usted tiene el rol de: " + user["typeRol"] )
    if user["typeRol"] == "Administrador":
        adminstratorOpcions()
    elif user["typeRol"] == "Jugador":
        pass


def mainLogin():
    print("Bienvenido al menu de inicio de secion")
    iD = input("Identificador: ")
    password = input("Contraseña: ")
    loginUser(iD,password)

mainLogin()