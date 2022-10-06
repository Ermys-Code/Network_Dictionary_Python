# region Libraries

import socket
import random
import pymysql

# endregion



# region Basic Server Functions

def SelectLanguage():
    global selectLanguageQuestion, selectLanguageError, language
    
    SendMenssage(selectLanguageError + selectLanguageQuestion)
    language = ReceiveMessage().lower()
    if language == "en" or language == "es":
        selectLanguageError = ""
        ConnectDatabase()
    else:
        selectLanguageError = "This is not a valid option / Esa no es una opcion valida\n"
        SelectLanguage()


def ConnectDatabase():
    global acronyms, descriptionsList, language
    
    connection = pymysql.connect(host="localhost", user="root", password="", database="Acronyms", cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    request = "SELECT * FROM acronyms_{}".format(language)
    cursor.execute(request)
    result = cursor.fetchall()
    for dic in result:
        acronyms[dic["acronym"]] = dic["description"]
    descriptionsList = list(acronyms.values())

def InitializeConnection():
    global serverSocket, serverAdress
    
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverAdress = ("localhost", 5002)
    serverSocket.bind(serverAdress)
    serverSocket.listen()
    print("Server {} connected on port {}.".format(*serverAdress))

def AcceptClient():
    global serverSocket, connection, clientAdress, connectionOpen
    
    print("\nWaiting for client.")
    while not connection or not clientAdress:
        connection, clientAdress = serverSocket.accept()
    connectionOpen = True
    print("\nClient {} has connected.".format(clientAdress[0]))

def SendMenssage(message_):
    global connection
    
    connection.sendall(message_.encode())

def ReceiveMessage():
    global connection
    
    messageReceived = None
    while not messageReceived:
        messageReceived = connection.recv(1024)
    return messageReceived.decode()

# endregion



# region App Functions

# region Main Menu

def SelectOption(option):
    global mainMenuOptions, incorrectOption, language
    
    if option in mainMenuOptions.keys():
        mainMenuOptions[option]()
    else:
        if language == "en":
            incorrectOption = "This is not a valid option\n"
        else:
            incorrectOption = "Esa no es una opcion valida\n"

def MainMenu():
    global menu, incorrectOption, language
    
    SendMenssage(incorrectOption + menu[language])
    incorrectOption = ""
    response = ReceiveMessage()
    SelectOption(response)

# endregion 



# region Acronym Description

def GetDescription(acronym):
    global acronyms, language
    
    if acronym in acronyms.keys():
        return acronyms[acronym]
    else:
        if language == "en":
            return "There is no description matching to this acronym in the database"
        else:
            return "No hay ninguna descripcion asociada a ese acronimo en la base de datos"

def AcronymDescription():
    global acronymDescriptionQuestion, acronymDescriptionConfirmation, language
    
    SendMenssage(acronymDescriptionQuestion[language])
    response = ReceiveMessage().upper()
    description = GetDescription(response)
    description += acronymDescriptionConfirmation[language]
    SendMenssage(description)
    decision = ReceiveMessage().lower()
    if language == "en" and decision == "yes" or language == "es" and decision == "si":
        AcronymDescription()

# endregion



# region Guess The Acronym

def GetRandomDescription():
    global descriptionsList
    
    randomIndex = random.randint(0, len(descriptionsList) - 1)
    return descriptionsList[randomIndex]

def CheckAnswer(acronym, description):
    global acronyms
    
    if acronym in acronyms.keys():
        print(acronyms[acronym] == description)
        return acronyms[acronym] == description
    else:
        return False

def GuessTheAcronym():
    global guessTheAcronymQuestion, playAgainQuestion, guessFailMessage, language
    
    description = GetRandomDescription()
    question = guessFailMessage + description + guessTheAcronymQuestion[language]
    SendMenssage(question)
    guessFailMessage = ""
    response = ReceiveMessage().upper()
    if CheckAnswer(response, description):
        SendMenssage(playAgainQuestion[language])
        playAgain = ReceiveMessage()
        if language == "en" and playAgain == "yes" or language == "es" and playAgain == "si":
            GuessTheAcronym()
    else:
        if language == "en": 
            guessFailMessage = "Fail\n\n"
        else:
            guessFailMessage = "Error\n\n"
        GuessTheAcronym()

# endregion



# region Close Conection

def CloseConnection():
    global closeConectionMessage, connection, clientAdress, connectionOpen
    
    SendMenssage(closeConectionMessage)
    connection.close()
    print("\nConnection with the client {} closed.".format(clientAdress[0]))
    connectionOpen = False
    connection = None
    clientAdress = None

# endregion

# endregion



# region Global Variables

serverSocket = None
serverAdress = None
connection = None
clientAdress = None

selectLanguageQuestion = "\nSelect the languaje / Selecciona el idioma: (en / es) "

menu = {
    "en" : """
ACRONYM DICTIONARY

1 - Acronym description
2 - Guess the acronym
3 - Close connection

Select an option: """,
    "es" : """
DICCIONARIO DE ACRONIMOS

1 - Descripcion de acronimos
2 - Adivina el acronimo
3 - Cerrar conexion

Selecciona una opcion: """
}

acronymDescriptionQuestion = {"en": "\nWrite the acronym you want to know about: ", "es" : "\nEscribe el acronimo del que busques informacion: "}
guessTheAcronymQuestion = {"en": "\n\nWhat protocol is this? ", "es" : "\n\nCual es este protocolo? "}
playAgainQuestion = {"en" : "Correct!\n\nDo you want to play again? (yes / no) ", "es" : "Correcto!\n\nQuieres jugar otra vez? (si / no) "}
acronymDescriptionConfirmation = {"en" : "\n\nDo you want to know about another acronym? (yes / no) ", "es" : "\n\nQuieres buscar informacion de otro acronimo? (si / no) "}
closeConectionMessage = "!close"
guessFailMessage = ""
incorrectOption = ""
selectLanguageError = ""
language = ""

mainMenuOptions = {
    "1" : AcronymDescription,
    "2" : GuessTheAcronym,
    "3" : CloseConnection
}
acronyms = {}

descriptionsList = []

connectionOpen = False

# endregion



# region Code

InitializeConnection()
while True:
    AcceptClient()
    SelectLanguage()
    while connectionOpen:
        MainMenu()

serverSocket.close()

# endregion