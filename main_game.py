userList = [{"name":"Dayanna","nickname":"dram","id": "dram", "password":"123","typeRol":"Administrador"},
            {"name":"Selena","nickname":"selena","id": "selanamm", "password":"semm","typeRol":"Administrador"}]




def registerUser(name,nickname,id,password,typeRol):
    newUser = {}
    newUser["name"] = name
    newUser["nickname"] = nickname
    newUser["id"] = id
    newUser["password"] = password
    newUser["typeRol"] = typeRol

    userList.append(newUser)


def register():
    name = (input("1) Nombre: "))
    nickname = (input("2) Nickname: "))
    id = input("3) ID: ")
    password = (input("4) Password:"))
    print("Rol= Administrador o Jugador")
    typeRol = input(str("Tipo de rol: "))

    registerUser(name,nickname,id,password,typeRol)
    adminstratorOpcions()



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
        adminstratorOpcions()

def adminstratorOpcions():
    print("1) Administrar usuarios\n"
          "2) Menu de inicio de secion")

    opcion = int(input("opcion: "))

    if opcion == 1:
        userAdministrator()
    elif opcion == 2:
        mainLogin()


def loginUser(id,password):

    for user in userList:
        if user["id"] == id:
            if user["password"] == password:
                verifyTyoeRol(user)
            elif user["id"] != id and user["password"] != password:
                print("Intente de nuevo")
                intentos = 1
                while intentos < 4:
                    print("Lleva " + str(intentos)+ " intentos de 3")
                    intentos+=1
                    mainLogin()
            else:
                print("No le quedan intentos")
                mainLogin()

        else:
            mainLogin()
def verifyTyoeRol(user):
    print(user["name"] + ", usted tiene el rol de: " + user["typeRol"] )
    if user["typeRol"] == "Administrador" or "administrador":
        adminstratorOpcions()
    elif user["typeRol"] == "Jugador" or "jugador":
        pass


def mainLogin():
    print("Bienvenido al menu de inicio de secion")
    iD = input("Identificador: ")
    password = input("Contraseña: ")
    loginUser(iD,password)

mainLogin()