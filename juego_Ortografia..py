import time
# Save the list of registered Users, it contains two sublists, the one that is in position 0 is for administrators
# and the one that is in position 1 for the players.
usersList = [[{"name": "Dayanna", "id": "dram", "password": "0210", "typeRol": "Administrator"},{"name": "selena", "id": "selenukis", "password": "987", "typeRol": "Administrator"}],
             [{"name":"Selena","nickname":"selena","id": "selena", "password":"1234","typeRol":"Player","gamesPlayed":10,"pointsEarned":9},
              {"name":"Dayana","nickname":"day","id": "day", "password":"123","typeRol":"Player","gamesPlayed":33,"pointsEarned":108},
              {"name": "Isabel", "nickname": "Isa", "id": "Isa99", "password": "1256", "typeRol": "Player","gamesPlayed": 0, "pointsEarned": 0},
              {"name": "Ryan", "nickname": "deadpool", "id": "Foxa", "password": "1233", "typeRol": "Player","gamesPlayed": 11, "pointsEarned": 45},
              {"name": "Chris", "nickname": "thor", "id": "trueno", "password": "5647", "typeRol": "Player","gamesPlayed": 15, "pointsEarned": 70},
              {"name": "Tony", "nickname": "stark", "id": "tony", "password": "1456", "typeRol": "Player","gamesPlayed": 0, "pointsEarned": 0},
              {"name": "Jeremy", "nickname": "Halcon", "id": "jeremy", "password": "564", "typeRol": "Player","gamesPlayed": 29, "pointsEarned": 500},
              {"name": "Dean", "nickname": "Winchester", "id": "Dean", "password": "978", "typeRol": "Player","gamesPlayed": 13, "pointsEarned": 26},
              {"name": "Andrew", "nickname": "Rick", "id": "Andrew", "password": "1237", "typeRol": "Player","gamesPlayed": 1, "pointsEarned": 49},
              {"name": "Jensen", "nickname": "Deanw", "id": "Jensen", "password": "1345", "typeRol": "Player","gamesPlayed": 7, "pointsEarned": 49},
              {"name": "Ana", "nickname": "jigoku", "id": "Ana", "password": "yolo", "typeRol": "Player","gamesPlayed": 0, "pointsEarned": 0},
              {"name": "Maria", "nickname": "sakura", "id": "Maria", "password": "vert", "typeRol": "Player","gamesPlayed": 9, "pointsEarned": 15},
              {"name": "Juan", "nickname": "LeeminHoo", "id": "Juan", "password": "yop", "typeRol": "Player","gamesPlayed": 0, "pointsEarned": 0},
              {"name": "rosa", "nickname": "ross", "id": "Rosa", "password": "5476", "typeRol": "Player","gamesPlayed": 4, "pointsEarned": 19},
              {"name": "jessie", "nickname": "misha", "id": "Jessie", "password": "657", "typeRol": "Player","gamesPlayed": 6, "pointsEarned": 20},
              {"name": "Carmen", "nickname": "karl", "id": "Carmen", "password": "7575", "typeRol": "Player","gamesPlayed": 8, "pointsEarned": 12},
              {"name": "Scarleth", "nickname": "ViudaNegra", "id": "Johanson", "password": "0776", "typeRol": "Player","gamesPlayed": 9, "pointsEarned": 17},
              {"name": "Logan", "nickname": "wolwerine", "id": "jackman", "password": "5678", "typeRol": "Player","gamesPlayed": 16, "pointsEarned": 56},
              {"name": "Goku", "nickname": "Kakaroto", "id": "goku12", "password": "1912", "typeRol": "Player","gamesPlayed": 6, "pointsEarned": 300},
              {"name": "Raúl", "nickname": "Auronplay", "id": "gato", "password": "10m", "typeRol": "Player","gamesPlayed": 8, "pointsEarned": 240},
              {"name": "Carlos", "nickname": "Carlos21", "id": "1989", "password": "120212", "typeRol": "Player","gamesPlayed": 17, "pointsEarned":62},]]

userLogged = [] #Save the id of the User that is currently logged in

# Save the word list with C, S, and Z.
wordsListCSZ = [["depre_ivo","s","depresivo"],["flore_er","c","florecer"],["santí_imo","s","santísimo"],["no_ivo","c","nocivo"],
                ["costarricen_e","s","costarricense"],["aboga_ía","c","abogacía"],["deli_iosos","c","deliciosos"],["finan_a","z","finanzas"],
                ["fluide_","z","fluidez"],["beode_","z","beodez"],["entere_a","z","entereza"],["pri_ión","s","prisi]ón"],
                ["belle_a","z","belleza"],["tre_illo","s","tresillo"],["llovi_na","z","llovizna"],["a_ertijo","c","acertijo"],
                ["ja_mín","z","jazmín"],["jere_","z","jerez"],["garban_o","z","garbanzo"],["abra_ivo","s","abrasivo"],
                ["ata_co","s","atasco"],["ingle_a","s","inglesa"],["cal_oncillos","z","calzoncillos"],["espe_ie","c","especie"],
                ["gentili_io","c","gentilicio"]]

# Save the word list with G and J.
wordsListGJ = [["aco_ían","g","acogían"],["vesti_io","g","vestigio"],["bu_ía","j","bujía"],["_imotear","g","gimotear"],
                ["_ordania","j","jordania"],["anal_ésico","g","analgésico"],["vi_ésimo","g","vigésimo"],["a_edrez","j","ajedrez"],
                ["an_ina","g","angina"],["_inebra","g","ginebra"],["octo_enario","g","octogenario"],["liti_io","g","litigio"],
                ["crucifi_o","j","crucifijo"],["pla_io","g","plagio"],["_enerico","g","generico"],["lo_ica","g","logica"],
                ["sacrile_io","g","sacrilegio"],["enca_ar","j","encajar"],["_iroscopio","g","giroscopio"],["venta_a","j","ventaja"],
                ["_eringa","j","jeringa"],["gin_ivitis","g","gingivitis"],["prote_er","g","proteger"],["_élido","g","gélido"],
                ["empare_o","j","emparejo"]]

# Save the word list with Y and LL.
wordsListYLL= [["ad_acente","y","ayacente"],["estribi_o","ll","estribillo"],["ra_o","y","rayo"],["cape_a","ll","capella"],
                ["con_eva","ll","conlleva"],["paragua_ismos","y","paraguayismos"],["ensa_ar","y","ensayar"],["onomatope_a","y","onomatopeya"],
                ["ho_o","y","hoyo"],["rodi_a","ll","rodilla"],["_acaré","y","Yacaré"],["novi_o","ll","novillo"],
                ["bo_o","y","boyo"],["ladri_o","ll","ladrillo"],["pro_ecto","y","proyecto"],["va_e","ll","valle"],
                ["ha_a","y","haya"],["vaji_a","ll","vajilla"],["ga_","y","gay"],["_avero","ll","llavero"],
                ["o_e","y","oye"],["a_anamiento","ll","allanamiento"],["a_er","y","ayer"],["ori_a","ll","orilla"],
                ["ave_ana","ll","avellana"]]

#Save the list of words with B, V and W.
wordsListBVW = [["bi_lioteca","b","biblioteca"],["reci_ir","b","recibir"],["nie_e","v","nieve"],["_elson","v","velson"],
                ["be_er","b","beber"],["bb_io","v","bbvio"],["ki_i","w","kiwi"],["mo_ilidad","v","movilidad"],
                ["tinie_la","b","tiniebla"],["solu_ilidad","b","solubilidad"],["longe_a","v","longeva"],["a_usivo","s","abusivo"],
                ["de_en","b","deben"],["pre_enir","v","prevenir"],["tai_án","w","taiwán"],["ci_ilidad","v","civilidad"],
                ["dar_in","w","darwin"],["ha_ai","w","hawai"],["subversi_a","v","subversiva"],["_endy","w","wendy"],
                ["con_iene","v","conviene"],["contra_enir","v","contravenir"],["_inchester","w","winchester"],["pro_abilidad","b","probabilidad"],
                ["_urro","b","burro"]]

# Save the list of words with tilde.
wordsLabeling = [["album","01234","0","álbum"],["abaco","01234","0","ábaco"],["cafe","0123","3","café"],["bebe","0123","3","bebé"],
                ["fantasia", "01234567", "6", "fantasía"], ["estatico", "01234567", "3", "estático"],["aromatico","012345678","4","aromático"],["violin","012345","4","violín"],
                ["cojin", "01234", "3", "cojin"], ["sociologia", "0123456789", "8", "sociología"],["frances","0123456","5","francés"],["manzana","0123456","-1","manzana"],
                ["heroes", "012345", "1", "héroes"], ["electrico", "012345678", "2", "eléctrico"],["tecla","01234","-1","tecla"],["espacio","0123456","-1","espacio"],
                ["pantalon", "01234567", "6", "pantalón"], ["galactico", "012345678", "3", "galáctico"],["espatula","01234567","3","espátula"],["memoria","0123456","-1","memoria"],
                ["lápiz", "01234", "1", "lápiz"], ["oceano", "012345", "2", "océano"],["penetracion","0123456789","8","penetración"],["talla","01234","-1","talla"],
                ["maria", "01234", "3", "maría"]]

# Requests the data of the administrator user as his: name, identifier and password.
def registerAdministrator():
    print("╔════════════════════════════════════════════════════════╗\n"
          "║         Enter the administrator's data:                ║\n"
          "╠════════════════════════════════════════════════════════╣")

    name = (input(" 1) Name: "))
    id = input(" 2) Identifier: ")
    password = (input(" 3) Password:"))
    typeRol = "Administrator "
    print("╚════════════════════════════════════════════════════════╝")
    print("\n")
    registerUserAdministrator(name, id, password, typeRol) # Call the function you add using a dictionary
                                                           # administrator users.
    userAdministrator()                                    # Call the function to manage users.

#Requests the data to the player user as his: name, alias, identifier and password.
def registerPlayers(): # Ask the player user for data to register
    print("╔════════════════════════════════════════════════════════╗\n"
          "║            Enter the Player's data:                    ║\n"
          "╠════════════════════════════════════════════════════════╣")

    name = (input(" 1) Name: "))
    nickname = (input(" 2) Nickname: "))
    id = input(" 3) Identifier: ")
    password = (input(" 4) Password:"))
    typeRol = "Player"
    print("╚════════════════════════════════════════════════════════╝")
    print("\n")

    registerUserPlayers(name, nickname, id, password, typeRol) # Call the function you add using a dictionary user players.

    userAdministrator()                                        # Call the function to manage users.

# Save the players' data in dictionaries.
def registerUserPlayers(name, nickname, id, password, typeRol): # Entries: name, id, nickname, password and role type.
    newUser = {}
    newUser["name"] = name
    newUser["nickname"] = nickname
    newUser["id"] = id
    newUser["password"] = password
    newUser["typeRol"] = typeRol
    newUser["gamesPlayed"] = 0
    newUser["pointsEarned"] = 0

    usersList[1].append(newUser)

# Save the data of the administrators in dictionaries.
def registerUserAdministrator(name, id, password, typeRol): # Entries: name, id, password and role type.
    newUser = {}
    newUser["name"] = name
    newUser["id"] = id
    newUser["password"] = password
    newUser["typeRol"] = typeRol

    usersList[0].append(newUser)

def loginID(): # Ask for the identifier and the password.
    print("******************** Login menu ********************\n"
          "┌--------------------------------------------------┐\n"
          " Please, enter your:                               \n")
    id = input(" »Identifier: ")
    password = input(" »Password: ")
    for i in range(len(usersList)):
        for user in usersList[i]:
            if user["id"] == id: # Validate that the identifier entered is the same one that is registered.
                if user["password"] == password: # Validate that the password entered is the same one that is registered.
                    print("├--------------------------------------------------┤")
                    userLogged.append(id)
                    verifyTypeRol(user)

                else: #If the password is incorrect, ask to be re-entered.
                    intentos = 2
                    while intentos > 0: # the cycle continues as long as the attempts are greater than 0
                        print(" -->Incorrect password, you have: " + str(intentos) + " attempts left.")
                        password = input(" »Password: ")
                        if user["id"] == id:
                            if user["password"] == password:
                                print("├--------------------------------------------------┤")
                                userLogged.append(id)
                                verifyTypeRol(user)

                            intentos -= 1
    print("\n")


# Verify the type of role that each user has to take it to its respective menu.
def verifyTypeRol(user):

    if user["typeRol"] == "Administrator": #Verify the administrator role.
        print(" " + user["name"] + ", you have the role of: " + user["typeRol"] + ".")
        print("└--------------------------------------------------┘")
        print("\n")
        administratorMenu()

    elif user["typeRol"] == "Player": # verify the role of player.
        print(" "+user["nickname"] + ", you have the role of: " + user["typeRol"] + ".")
        print("└--------------------------------------------------┘")
        print("\n")
        playerMenu()

#Main menu that continues as long as the option is not 2.
def mainMenu():

    runProgram = True

    while(runProgram):
        print("******** Welcome to the Spell Checker Game ********\n"
              "┌-------------------------------------------------┐\n"
              "¦ 1) Log in.                                      ¦\n"
              "¦ 2) Exit game.                                   ¦\n"
              "└-------------------------------------------------┘")

        option = input(str("→ Option: "))
        print("\n")

        if(option == "1"):
            loginID()         #Call the function to verify both the password and the identifier
        elif option == "2":
            runProgram = False #The exit of the program, the program is finished
#It is an administrator menu that redirects
def addTypeUser():
    print("╔════════════════════════════════════════════════════════╗\n"
          "║           Which user do you want to add?               ║\n"
          "╠════════════════════════════════════════════════════════╣\n"
          "║ 1) Administrator.                                      ║\n"
          "║ 2) Player.                                             ║\n"
          "║ 3) Return to the user manager menu.                    ║\n"
          "╚════════════════════════════════════════════════════════╝")
    option = input(str("→ User: "))
    print("\n")

    if option == "1":
        registerAdministrator()# Call the function to register an administrator user

    elif option == "2":
        registerPlayers() # Call the function to register a player user
    elif option == "3":
        userAdministrator()#Returns it to the administrator menu
    else:
        addTypeUser()# In the case that the user does not have an answer as a valid option, the user will be called again


#Function that is responsible for deleting an administrator user
def removeUsersAdministrators():
    print("╔════════════════════════════════════════════════════════╗\n"
          "║         Whom you want to eliminate?                    ║\n"
          "╠════════════════════════════════════════════════════════╣")
    count = 1     #Counter
    for users in usersList[0]: #Scroll the list in position 0
        print(" " + str(count) + ") Identifier: " + users["id"] + " (" + users["name"] + ").")#Print the players that are on the list, so that the user decides which one he wants to eliminate

        count += 1 # Increase the counter
    print("╠════════════════════════════════════════════════════════╣")
    delete = int(input(" → Enter the user number you want to delete: "))# It asks the user to type the user number that he wants to delete

    count2 = 1#A new counter
    for y in usersList[0]:# Scroll the list to find the number that was requested
        if delete == count2: #Condition
            usersList[0].pop(count2 -1)
        count2 +=1
    print("╠════════════════════════════════════════════════════════╣")
    print(" The user has been removed!")
    print("╚════════════════════════════════════════════════════════╝")
    print("\n")

    userAdministrator()

#Function to eliminate a player user
def removeUsersPlayers():
    print("╔════════════════════════════════════════════════════════╗\n"
          "║             Whom you want to eliminate?                ║\n"
          "╠════════════════════════════════════════════════════════╣")
    count = 1
    for users in usersList[1]:
        print(" "+str(count) + ") Identifier: " + users["id"] + "(" + users["name"] + ").")
        count += 1
    print("╠════════════════════════════════════════════════════════╣")
    delete = int(input(" → Enter the user number you want to delete: "))

    count2 = 1
    for y in usersList[1]:
        if delete == count2:
            usersList[1].pop(count2 -1)
        count2 += 1

    print("╠════════════════════════════════════════════════════════╣")
    print(" The user has been removed!")
    print("╚════════════════════════════════════════════════════════╝")

    print("\n")

    userAdministrator()

#Menu function to request the user to remove an administrator or player
def removeMenu():
    print("╔════════════════════════════════════════════════════════╗\n"
          "║           Which user do you want to remove?            ║\n"
          "╠════════════════════════════════════════════════════════╣\n"
          "║ 1) Administrator.                                      ║\n"
          "║ 2) Player.                                             ║\n"
          "║ 3) Return to the user manager menu.                    ║\n"
          "╚════════════════════════════════════════════════════════╝")

    option = (input(str("→ User: ")))
    print("\n")

    if option == "1":
        removeUsersAdministrators()#Call the function to remove administrator
    elif option == "2":
        removeUsersPlayers()# Call the function to eliminate player
    elif option == "3":
        userAdministrator()# Call the general user menu
    else:
        removeMenu()#

#Administrator menu function, it asks you what you want to do, create or delete a user or return the administrator general menu
def userAdministrator():
    print("╔════════════════════════════════════════════════════════╗\n"
          "║                User Manager Menu                       ║\n"
          "╠════════════════════════════════════════════════════════╣\n"
          "║ 1) Create user.                                        ║\n"
          "║ 2) Delete user.                                        ║\n"
          "║ 3) Return to the administrator menu.                   ║\n"
          "╚════════════════════════════════════════════════════════╝")

    option = (input(str("→ Option: ")))

    print("\n")

    if option == "1":
        addTypeUser()# Call the function to add a user
    elif option == "2":
        removeMenu()#Call the function to remove a user
    elif option == "3":
        administratorMenu()#Call the general menu of the administrator
    else:
        userAdministrator()#If no option is valid then the function menu will be called to administer ususrio, that is, the same, until there is a valid option

#Function to see the list of players by an administrator logged in
def seePlayerListAdministrator():
    playerCount = 1# Counter
    for player in usersList[1]: #Go through the list in position 1, where the players are
        print(str(playerCount) + ")" + " Identifier: " + player["id"] + " / " + "Player's name: " + player["name"]
                  + " / " + "Nickname: " + player["nickname"] + ".\n")#Print the players
        playerCount +=1#Increase the counter to scroll the position
    print("\n")
    consultsAdministratror()

#Function to see the list of players by a player logged in
def seePlayerListPlayers():
    playerCount = 1# Conatdor
    for player in usersList[1]:#Go through the list in position 1, where the players are
        print(str(playerCount) + ")" + " Identifier: " + player["id"] + " / " + "Player's name: " + player["name"]
                  + " / " + "Nickname: " + player["nickname"] + ".\n")#Print the players
        playerCount +=1#Increase the counter to scroll the position
    print("\n")

    consultsplayer()
#Feature that shows a record of the best 10 players
def bestPlayers():
    player = 1
    bestlist = []#Ready to add players
    for i in usersList[1]:# Scroll the list in the position in position 1, where the players are
        best = [i["pointsEarned"],i["nickname"],i["gamesPlayed"]]#Ready to add player data

        bestlist.append(best)#Add the best list to the bestList list

    bestlist.sort()#Sort the list ascendingly
    bestlist.reverse()#Change the order of the list downwards

    for x in bestlist:#Go through the list.
        if player <=10:#Condition to limit the number of players to 10
            print(str(player) + ") Nickname: "+ str(x[1]) + " / Games played: " + str(x[2]) + " / Points earned: " + str(x[0])+"\n")#It is printing each player from the list
            player+=1 # Increase to get to 10 to finally print the best players

    print("\n")
    consultsAdministratror()

# Function to know the average of games played
def avarageGames():
    print("╔════════════════════════════════════════════════════════╗\n"
          "║                         Avarage Games                  ║\n"
          "╠════════════════════════════════════════════════════════╣")


    games = 0 #Counter
    for i in usersList[1]:#Record the list at the position of 1, where the players are
        games += i["gamesPlayed"]#Increase the counter

    avarage = "{0:.2f}".format(games / len(usersList[1])) #Take the average and leave it 2 decimals
    print(" Total games played: " + str(games) + "\n" + " Total players: " + str(len(usersList[1]))+ "\n" + " Average of games played: " + str(avarage)+"\n")#Print the average
    print("╚════════════════════════════════════════════════════════╝")
    print("\n")

    consultsAdministratror()
#Function to know the players with fewer points
def badPlayers():
    print("╔════════════════════════════════════════════════════════╗\n"
          "║    Players with the least number of points             ║\n"
          "╠════════════════════════════════════════════════════════╣")
    player = 1#Counter
    bestlist = []#List where the players are
    for i in usersList[1]:#Scroll the list at the position of 1, where the players are
        best = [i["pointsEarned"],i["nickname"]]#Ready to add players with fewer points

        bestlist.append(best)#Add the best list to the bestlist list

    bestlist.sort()#Sort the list ascendingly

    for x in bestlist:#Go through the bestlist list
        if x[0] > 1:#Condition so that at least 2 players exist
            if player <=3:#Condition so that only 3 players are printed
                print(" " +str(player) + ") Nickname: "+ str(x[1]) + " / Points earned: " + str(x[0])+"\n")#It is printing the players

                player+=1#Increase the counter
    print("╚════════════════════════════════════════════════════════╝")
    print("\n")

    consultsAdministratror()#Call the administrator query function

# Function administrator query menu, you can consult the best players, player list, player average
def consultsAdministratror():
    print("╔════════════════════════════════════════════════════════╗\n"
          "║                   Consults Menu                        ║\n"
          "╠════════════════════════════════════════════════════════╣\n"
          "║ 1) See list of players.                                ║\n"
          "║ 2) See the best 10 players.                            ║\n"
          "║ 3) Average of games played.                            ║\n" 
          "║ 4) See players with the least number of points.        ║\n"                                        
          "║ 5) Return to the administrator menu.                   ║\n"
          "╚════════════════════════════════════════════════════════╝")



    option = input(str("→ Option: "))
    print("\n")

    if option == "1":
        seePlayerListAdministrator()#Call the function to see the list of players
    elif option == "2":
        bestPlayers()#Call the function to see the best 10 players
    elif option == "3":
        avarageGames()#Call the function to know the average of games
    elif option == "4":
        badPlayers()#Call the function to know the players with the least earned points
    elif option == "5":
        administratorMenu()#Call the general menu of the administrator
    else:
        consultsAdministratror()#The same menu is called again until the user some of the valid options

#Function of the general administrator menu
def administratorMenu():
    print("╔════════════════════════════════════════════════════════╗\n"
          "║                Administrator Menu                      ║\n"
          "╠════════════════════════════════════════════════════════╣\n"
          "║ 1) Manage users.                                       ║\n"
          "║ 2) Consutls.                                           ║\n"
          "║ 3) Sign off.                                           ║\n"
          "╚════════════════════════════════════════════════════════╝")

    opcion = input(str("→ Option: "))
    print("\n")

    if opcion == "1":
        userAdministrator()#Call the function to manage users, whether to delete or add user

    elif opcion == "2":
        consultsAdministratror()#Call the administration queries function, in which you can see the best and worst players and the list of them

    elif opcion == "3" :
        del (userLogged[:])#Remove the id all the information that is in the list
        mainMenu()#Call the main menu
    else:
        administratorMenu()#The same menu is called again until the user some of the valid options

#Menu to modify the nickname of the players
def modifyNickname():
    print("╔════════════════════════════════════════════════════════╗\n"
          "║                    Modify Nickname                     ║\n"
          "╠════════════════════════════════════════════════════════╣")

    for y in usersList[1]:#Go through position 1 on the list, where the players are
        if y["id"] == userLogged[0]:#Condition to see if the id is in the userLogged list
            newNick = input("→ Enter your new nickname(" + y["nickname"] + "): " )#Request the new nickname
            y["nickname"] = newNick#It gives a new value to the position of the nickname, to replace it with the entered one
    print("╠════════════════════════════════════════════════════════╣")
    print(" Your nickname was modified successfully!")
    print("╚════════════════════════════════════════════════════════╝")
    print("\n")
    playerMenu()#Call the player menu
#Function to see the data of the user that is logged in
def userDataLogin():
    print("╔════════════════════════════════════════════════════════╗\n"
          "║                  Account data                          ║\n"
          "╠════════════════════════════════════════════════════════╣")
    for i in usersList[1]:#Recall the list in position 1, where the players are
        if i["id"] == userLogged[0]:# Condition to see if the id is equal to the one found in the userLogged list
            print("Name: " + i["name"] + "." + "\n" + "Nickname: " + i["nickname"] + "." + "\n" + "Games played: "
                  + str(i["gamesPlayed"])+ "." + "\n" + "Puntos Ganados: " + str(i["pointsEarned"]) + ".")#Print the information of the logged in player
    print("╚════════════════════════════════════════════════════════╝")
    print("\n")

    consultsplayer()#Call the player's query menu
#Player query menu, you can see the list of players and your account information
def consultsplayer():
    print("╔════════════════════════════════════════════════════════╗\n"
          "║                  Consults Menu                         ║\n"
          "╠════════════════════════════════════════════════════════╣\n"
          "║ 1) See list of players.                                ║\n"
          "║ 2) View account data.                                  ║\n"
          "║ 3) Return to the player menu.                          ║\n"
          "╚════════════════════════════════════════════════════════╝")

    option = int(input("→ Option: "))
    print("\n")

    if option == 1:
        seePlayerListPlayers()#Call the function to see the list of players
    elif option == 2:
        userDataLogin()#Call the function to see the information of the logged in player
    elif option == 3:
        playerMenu()#Return to the general player menu
    else:
        consultsplayer()#Call the same player query menu if a valid option is entered

#Function for the category of completing in the area of the letters CSZ
def categoryCSZ():
    print("Completing, Category c, s y z.")
    print("Press the letter q, to exit the game")
    for x in wordsListCSZ:#Scroll the list of these categories of words
        start = time.time()#Variable for the beginning of time
        print("The word is: "+ str(x[0]))#Print the word to complete
        letter = input(str("Which letter is missing?: "))
        final = time.time()#Variable to end time
        timer = round(final - start,0)# subtract time and round it

        if letter == "q" or letter == "Q":# Condition to exit the game by completing
            print("He has left the game!")
            menuPlayComplete()#Call the game menu of the category completing

        elif timer > 15 and letter == (x[1]):# Condition if the user responds after the set time
            for i in usersList[1]:#Record the list of users in position 1, where the user users are
                if i["id"] == userLogged[0]:# Condition to verify that the id is equal to the one found in the userLogged list in position 0
                    i["pointsEarned"] = i["pointsEarned"] -2 #To subtract two points to answer from outside of the established time
                    print("Sorry, did not respond within the established time, lost 2 points."
                          "The correct letter was: " + str(x[1]) + ".\n"  )#Print the why of the subtraction of points, also print the correct word
        elif letter == (x[1]):#If the letter entered is correct
            for i in usersList[1]:#Go through the list of users in position 1, where the user users are
                if i["id"] == userLogged[0]:#Condition to verify that the id is equal to the one found in the userLogged list in position 0
                    i["pointsEarned"] = i["pointsEarned"] +2# 2 points are added to the position of points won by answering correctly
                    print("It's correct, you won 2 points."+ "\n")

        elif timer > 15 and letter != (x[1]):#If the entered letter is incorrect and outside the determined time
            for i in usersList[1]:#Go through the list of users in position 1, where the user users are
                if i["id"] == userLogged[0]:# Condition to verify that the id is equal to the one found in the userLogged list in position 0
                    i["pointsEarned"] = i["pointsEarned"] -2
                    print("Sorry, did not respond within the established time, lost 2 points."
                          "The correct letter was: " + str(x[1]) + ".\n")
        else:
            for i in usersList[1]:#Record the list of users in position 1, where the user users are
                if i["id"] == userLogged[0]:# Condition to verify that the id is equal to the one found in the userLogged list in position 0
                    i["pointsEarned"] -=1# 1 points are subtracted from the position of points awarded for answering incorrectly
            print("It's wrong, you lost 1 point, the correct letter was: " + str(x[1]) + "."+"\n")
    print("\n")

    menuPlayComplete()# Call the completing menu

#Function for the category of completing in the area of letters GJ
def categoryGJ():
    print("Completing, Category g y j.")
    print("Press the letter q, to exit the game")
    for x in wordsListGJ:#Recorre la lista de esta categorias de palabras
        start = time.time()  # Variable for the beginning of time
        print("The word is: " + str(x[0]))  # Print the word to complete
        letter = input(str("Which letter is missing?: "))
        final = time.time()  # Variable to end time
        timer = round(final - start, 0)  # subtract time and round it

        if letter == "q" or letter == "Q":  # Condition to exit the game by completing
            print("He has left the game!")
            menuPlayComplete()  # Call the game menu of the category completing

        elif timer > 15 and letter == (x[1]):  # Condition if the user responds after the set time
            for i in usersList[1]:  # Record the list of users in position 1, where the user users are
                if i["id"] == userLogged[0]:  # Condition to verify that the id is equal to the one found in the userLogged list in position 0
                    i["pointsEarned"] = i["pointsEarned"] - 2  # To subtract two points to answer from outside of the established time
                    print("Sorry, did not respond within the established time, lost 2 points."
                          "The correct letter was: " + str(x[1]) + ".\n")  # Print the why of the subtraction of points, also print the correct word
        elif letter == (x[1]):  # If the letter entered is correct
            for i in usersList[1]:  # Go through the list of users in position 1, where the user users are
                if i["id"] == userLogged[0]:  # Condition to verify that the id is equal to the one found in the userLogged list in position 0
                    i["pointsEarned"] = i["pointsEarned"] + 2  # 2 points are added to the position of points won by answering correctly
                    print("It's correct, you won 2 points." + "\n")

        elif timer > 15 and letter != (x[1]):  # If the entered letter is incorrect and outside the determined time
            for i in usersList[1]:  # Go through the list of users in position 1, where the user users are
                if i["id"] == userLogged[0]:  # Condition to verify that the id is equal to the one found in the userLogged list in position 0
                    i["pointsEarned"] = i["pointsEarned"] - 2
                    print("Sorry, did not respond within the established time, lost 2 points."
                          "The correct letter was: " + str(x[1]) + ".\n")
        else:
            for i in usersList[1]:  # Record the list of users in position 1, where the user users are
                if i["id"] == userLogged[0]:  # Condition to verify that the id is equal to the one found in the userLogged list in position 0
                    i["pointsEarned"] -= 1  # 1 points are subtracted from the position of points awarded for answering incorrectly
            print("It's wrong, you lost 1 point, the correct letter was: " + str(x[1]) + "." + "\n")
    print("\n")

    menuPlayComplete()  # Call the completing menu


#Function for the category of completing in the area of the letters YLL
def categoryYLL():
    print("Completing, Category y y ll.")
    print("Press the letter q, to exit the game")
    for x in wordsListYLL:#Recorre pointsEarnedla lista de esta categorias de palabras
        start = time.time()  # Variable for the beginning of time
        print("The word is: " + str(x[0]))  # Print the word to complete
        letter = input(str("Which letter is missing?: "))
        final = time.time()  # Variable to end time
        timer = round(final - start, 0)  # subtract time and round it

        if letter == "q" or letter == "Q":  # Condition to exit the game by completing
            print("He has left the game!")
            menuPlayComplete()  # Call the game menu of the category completing

        elif timer > 15 and letter == (x[1]):  # Condition if the user responds after the set time
            for i in usersList[1]:  # Record the list of users in position 1, where the user users are
                if i["id"] == userLogged[0]:  # Condition to verify that the id is equal to the one found in the userLogged list in position 0
                    i["pointsEarned"] = i["pointsEarned"] - 2  # To subtract two points to answer from outside of the established time
                    print("Sorry, did not respond within the established time, lost 2 points."
                          "The correct letter was: " + str(x[1]) + ".\n")  # Print the why of the subtraction of points, also print the correct word
        elif letter == (x[1]):  # If the letter entered is correct
            for i in usersList[1]:  # Go through the list of users in position 1, where the user users are
                if i["id"] == userLogged[0]:  # Condition to verify that the id is equal to the one found in the userLogged list in position 0
                    i["pointsEarned"] = i["pointsEarned"] + 2  # 2 points are added to the position of points won by answering correctly
                    print("It's correct, you won 2 points." + "\n")

        elif timer > 15 and letter != (x[1]):  # If the entered letter is incorrect and outside the determined time
            for i in usersList[1]:  # Go through the list of users in position 1, where the user users are
                if i["id"] == userLogged[0]:  # Condition to verify that the id is equal to the one found in the userLogged list in position 0
                    i["pointsEarned"] = i["pointsEarned"] - 2
                    print("Sorry, did not respond within the established time, lost 2 points."
                          "The correct letter was: " + str(x[1]) + ".\n")
        else:
            for i in usersList[1]:  # Record the list of users in position 1, where the user users are
                if i["id"] == userLogged[0]:  # Condition to verify that the id is equal to the one found in the userLogged list in position 0
                    i["pointsEarned"] -= 1  # 1 points are subtracted from the position of points awarded for answering incorrectly
            print("It's wrong, you lost 1 point, the correct letter was: " + str(x[1]) + "." + "\n")
    print("\n")

    menuPlayComplete()  #Call the completing menu

#Function for the completing category in the area of letters BWV
def categoryBVW():
    start = time.time()  # Variable for the beginning of time
    print("The word is: " + str(x[0]))  # Print the word to complete
    letter = input(str("Which letter is missing?: "))
    final = time.time()  # Variable to end time
    timer = round(final - start, 0)  # subtract time and round it

    if letter == "q" or letter == "Q":  # Condition to exit the game by completing
        print("He has left the game!")
        menuPlayComplete()  # Call the game menu of the category completing

    elif timer > 15 and letter == (x[1]):  # Condition if the user responds after the set time
        for i in usersList[1]:  # Record the list of users in position 1, where the user users are
            if i["id"] == userLogged[0]:  # Condition to verify that the id is equal to the one found in the userLogged list in position 0
                i["pointsEarned"] = i["pointsEarned"] - 2  # To subtract two points to answer from outside of the established time
                print("Sorry, did not respond within the established time, lost 2 points."
                      "The correct letter was: " + str(x[1]) + ".\n")  # Print the why of the subtraction of points, also print the correct word
    elif letter == (x[1]):  # If the letter entered is correct
        for i in usersList[1]:  # Go through the list of users in position 1, where the user users are
            if i["id"] == userLogged[0]:  # Condition to verify that the id is equal to the one found in the userLogged list in position 0
                i["pointsEarned"] = i["pointsEarned"] + 2  # 2 points are added to the position of points won by answering correctly
                print("It's correct, you won 2 points." + "\n")

    elif timer > 15 and letter != (x[1]):  # If the entered letter is incorrect and outside the determined time
        for i in usersList[1]:  # Go through the list of users in position 1, where the user users are
            if i["id"] == userLogged[0]:  # Condition to verify that the id is equal to the one found in the userLogged list in position 0
                i["pointsEarned"] = i["pointsEarned"] - 2
                print("Sorry, did not respond within the established time, lost 2 points."
                      "The correct letter was: " + str(x[1]) + ".\n")
    else:
        for i in usersList[1]:  # Record the list of users in position 1, where the user users are
            if i["id"] == userLogged[0]:  # Condition to verify that the id is equal to the one found in the userLogged list in position 0
                i["pointsEarned"] -= 1  # 1 points are subtracted from the position of points awarded for answering incorrectly
        print("It's wrong, you lost 1 point, the correct letter was: " + str(x[1]) + "." + "\n")
    print("\n")

    menuPlayComplete()  # Call the completing menu
#Function for the categories for the category of the game completing
def menuPlayComplete():
    print("╔════════════════════════════════════════════════════════╗\n"
          "║              Game menu Completing                      ║\n"
          "╠════════════════════════════════════════════════════════╣\n"
          "║      Which category do you want to play?:              ║\n"
          "╠════════════════════════════════════════════════════════╣\n"
          "║ 1) Category C,S,Z.                                     ║\n"
          "║ 2) Category G,J.                                       ║\n"
          "║ 3) Category Y,LL.                                      ║\n"
          "║ 4) Category B,V,W.                                     ║\n"
          "║ 5) Return to the game menu.                            ║\n"
          "╚════════════════════════════════════════════════════════╝")

    opcion = input(str("→ Option: "))
    print("\n")

    if opcion == "1":
        for i in usersList[1]:#Go through the list of users in position 1, where the user users are
            if i["id"] == userLogged[0]:#Condition to verify that the id is equal to the one found in the userLogged list in position 0
                i["gamesPlayed"] = i["gamesPlayed"] + 1 #Add a game to the games position
                categoryCSZ()

    elif opcion == "2":
        for i in usersList[1]:#Go through the list of users in position 1, where the user users are
            if i["id"] == userLogged[0]:#Condition to verify that the id is equal to the one found in the userLogged list in position 0
                i["gamesPlayed"] = i["gamesPlayed"] + 1#Add a game to the games position
                categoryGJ()

    elif opcion == "3":
        for i in usersList[1]:#Go through the list of users in position 1, where the user users are
            if i["id"] == userLogged[0]:#Condition to verify that the id is equal to the one found in the userLogged list in position 0
                i["gamesPlayed"] = i["gamesPlayed"] + 1#Add a game to the games position
                categoryYLL()
    elif opcion == "4":
        for i in usersList[1]:#Go through the list of users in position 1, where the user users are
            if i["id"] == userLogged[0]:#Condition to verify that the id is equal to the one found in the userLogged list in position 0
                i["gamesPlayed"] = i["gamesPlayed"] + 1#Add a game to the games position
                categoryBVW()
    elif opcion == "5":
        menuPlay()
    else:
        menuPlayComplete()
#Function for the rating category
def labelingWord():
    for x in wordsLabeling:
        print("Labeling")
        print("Press the letter q, to exit the game")
        start = time.time()#Variable to start the chronometer
        print("The word is: " + str(x[0]))#Print the word to check
        print("             "+ str(x[1]))#Print the positions of each letter
        letra = input(str("What position is tick?: "))
        final = time.time()#Variable to end the chronometer
        timer = round(final - start, 0)

        if letra == "q" or letra == "Q":
            labelingMenu()

        elif timer > 15 and letra == (x[2]):#Condition if the user responds after the set time
            for i in usersList[1]:#Go through the list of users in position 1, where the user users are
                if i["id"] == userLogged[0]:#Condition to verify that the id is equal to the one found in the userLogged list in position 0
                    i["pointsEarned"] = i["pointsEarned"] - 2#To subtract 2 points for answering incorrectly
                    print("Sorry, did not respond within the established time, lost 2 points."
                          "The correct position was: " + str(x[2]) + ".\n")  #Print the why of the subtraction of points, also print the correct word


        elif letra == (x[2]):#Condition if the user responds after the set time
            for i in usersList[1]:#Go through the list of users in position 1, where the user users are
                if i["id"] == userLogged[0]:#Condition to verify that the id is equal to the one found in the userLogged list in position 0
                    i["pointsEarned"] = i["pointsEarned"] + 2#To add 2 points to answer correctly
                    print("It's correct, you won 2 points.\n")

        elif timer > 15 and letra != (x[2]):#Condition if the user responds after the set time and incorrectly
            for i in usersList[1]:#Go through the list of users in position 1, where the user users are
                if i["id"] == userLogged[0]:#Condition to verify that the id is equal to the one found in the userLogged list in position 0
                    i["pointsEarned"] = i["pointsEarned"] - 2#Go through the list of users in position 1, where the user users are
                    print("Sorry, did not respond within the established time, lost 2 points."
                          "The correct position was: " + str(x[2]) + ".\n")  # Print the why of the subtraction of points, also print the correct word


        else:
            for i in usersList[1]:#Go through the list of users in position 1, where the user users are
                if i["id"] == userLogged[0]:#Condition to verify that the id is equal to the one found in the userLogged list in position 0
                    i["pointsEarned"] -= 1#To subtract 1 point for answering incorrectly
            print("It's wrong,you lost 1 point, the position was: " + str(x[2]) + ".\n")
    print("\n")

    menuPlay()


#Function of the game menu, either ticking or completing
def menuPlay():
    print("╔════════════════════════════════════════════════════════╗\n"
          "║                   Game Menu                            ║\n"
          "╠════════════════════════════════════════════════════════╣\n"
          "║            What do you want to do?:                    ║\n"
          "╠════════════════════════════════════════════════════════╣\n"
          "║ 1) Play completing.                                    ║\n"
          "║ 2) Play labeling.                                      ║\n"
          "║ 3) Read the instructions.                              ║\n"
          "║ 4) Return to the player menu.                          ║\n"                
          "╚════════════════════════════════════════════════════════╝")

    opcion = input(str("→ Option: "))
    print("\n")

    if opcion == "1":
        menuPlayComplete()#Call the completing menu

    elif opcion == "2":
        for i in usersList[1]:  # Go through the list of users in position 1, where the user users are
            if i["id"] == userLogged[0]:  #Condition to verify that the id is equal to the one found in the userLogged list in position 0
                i["gamesPlayed"] = i["gamesPlayed"] + 1  #Add a game to the games position
                labelingWord()  #Call the menu by branding words

    elif opcion == "3":
        print("Game instructions.\n\n" #print the instructions
              
              ">>>General instructions:\n"
              "1. It has 15 seconds to answer, it is already completing or calling.\n"
              "2. At any time you can press the letter q to exit the game.\n"
              "3. If you answer correctly, you will earn 2 points.\n"
              "4. If you answer incorrectly, you will lose 1 point.\n"
              "5. If you do not respond within the given time, you will lose 2 points.\n\n"
              
              ">>>Completing: \n"
              "1. It is divided into 4 categories c-s-z, g-j, y-ll, v-b-w.\n"
              "2. Each word must be completed with the correct letter of its respective category.\n\n"
              
              ">>>Labeling:\n"
              "1. Each word must be completed with the correct position where the tilde is located.\n"
              "2. The positions will appear below the word.\n"
              "3. If the word does not have a tilde, you should write -1.\n\n")
        menuPlay()

    elif opcion == "4":
        playerMenu()#Call the play menu, either by checking or completing words, in case the option is not valid

    else:
        menuPlay()#Call the player menu

#Player menu function, the, which allows you to either play, change nickaname or queries
def playerMenu():
    print("╔════════════════════════════════════════════════════════╗\n"
          "║                   Player Menu                          ║\n"
          "╠════════════════════════════════════════════════════════╣\n"
          "║            What do you want to do?:                    ║\n"
          "╠════════════════════════════════════════════════════════╣\n"
          "║ 1) Play.                                               ║\n"
          "║ 2) Change the nickname.                                ║\n"
          "║ 3) Consults.                                           ║\n"
          "║ 4) Sign off.                                           ║\n"
          "╚════════════════════════════════════════════════════════╝")

    opcion = input(str("→ Option: "))
    print("\n")

    if opcion == "1":
        menuPlay()#Call the player menu

    elif opcion == "2":
        modifyNickname()#Call the function to be able to modify the player's nickname (only the logged-in player can do that action)

    elif opcion == "3":
        consultsplayer()#Call the player's query menu

    elif opcion == "4":
        del (userLogged[:])#Remove the items from the logged in user list
        mainMenu()#Call the main menu

    else:
        playerMenu()#Call the player menu
mainMenu()#Call the main menu to start the program