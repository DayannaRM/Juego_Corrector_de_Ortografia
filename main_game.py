userList = []

def loginUser(id,password):

    for user in userList:
        if user["iD"] == id:
            if user["password"] == password:
                pass
            else:
                print("Intente de nuevo")
                intentos = 0
                while intentos <= 3:
                        mainLogin()
                    intentos+=1


def mainLogin():
    print("Bienvenido al menu de inicio de secion")
    iD = input("Identificador: ")
    password = input("Contraseña: ")
    loginUser(iD,password)

mainLogin()