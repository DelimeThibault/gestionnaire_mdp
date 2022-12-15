from tkinter import *
#from tkinter.ttk import *
from functools import partial
from test import *
#from interface import gui


flag = True
def firstTime():
    if flag == True:
        regis.mainloop()
        
    else:
        print("pas")
def checkLogin(password):
    if str(password.get()) == "ok":
        mainWin()
        
    else:
        print("pas ok")
        
def logWin():
    logwin = Tk()  
    logwin.geometry('500x150')  
    logwin.title('Connexion au gestionnaire de mots de passes')
    Intro = Label(logwin, text = "Bienvenue sur votre gestionnaire de mots de passe Mr.Dory", font = "Castellar")

    #password label and password entry box
    passwordLabel = Label( logwin,text="Password", font = "Castellar")
    password = StringVar()
    passwordEntry = Entry(logwin, textvariable=password, show='*')
    checkLogin = partial(checkLogin, password)

    #login button
    loginButton = Button(logwin, text= "Se connecter", font = "Castellar", command=checkLogin)


    #Quit button
    Quit_button = Button(logwin, text="Quitter", font = "Castellar", command=logwin.quit)

    #command to displak in window
    Intro.pack()
    passwordLabel.pack()
    passwordEntry.pack()
    loginButton.pack()
    Quit_button.pack()  

def mainWin():
    main = Tk()  
    main.geometry('500x150')  
    main.title('Gestionnaire de mots de passes')
    
    siteLabel = Label( main,text="Site", font = "Castellar").grid(row=0, column=0)
    URLLabel = Label( main,text="URL", font = "Castellar").grid(row=0, column=1)
    usernameLabel = Label( main,text="Username", font = "Castellar").grid(row=0, column=2)
    passwdLabel = Label( main,text="Password", font = "Castellar").grid(row=0, column=3)
    
    Add = Button(main, text="Ajouter", font = "Castellar", command=main.quit).grid(row=7, column=0)
    Modify = Button(main, text="Modifier", font = "Castellar", command=main.quit).grid(row=7, column=1)
    Delete = Button(main, text="Supprimer", font = "Castellar", command=main.quit).grid(row=7, column=2)
    Quit = Button(main, text="Quitter", font = "Castellar", command=main.quit).grid(row=7, column=3)
    
#window

regis = Tk()  
regis.geometry('500x150')  
regis.title('Inscription au gestionnaire de mots de passes')
Introreg = Label(regis, text = "Bonjour M.Dory, créer votre mot de passe s'il vous plait", font = "Castellar")

#password label and password entry box
passwordRegLab = Label( regis,text="Password", font = "Castellar")
passwordReg = StringVar()
passwordRegEntry = Entry(regis, textvariable=passwordReg, show='*')
checkLogin = partial(checkLogin, passwordReg)

#login button
loginButton = Button(regis, text= "Se connecter", font = "Castellar", command=checkLogin)


#Quit button
Quit_button = Button(regis, text="Quitter", font = "Castellar", command=regis.quit)

#command to displak in window
Intro.pack()
passwordLabel.pack()
passwordEntry.pack()
loginButton.pack()
Quit_button.pack()  

firstTime()




