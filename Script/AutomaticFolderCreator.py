import os
import click 
import json


text = r"""                _                        _   _        ______    _     _              _____                _             
     /\        | |                      | | (_)      |  ____|  | |   | |            / ____|              | |            
    /  \  _   _| |_ ___  _ __ ___   __ _| |_ _  ___  | |__ ___ | | __| | ___ _ __  | |     _ __ ___  __ _| |_ ___  _ __ 
   / /\ \| | | | __/ _ \| '_ ` _ \ / _` | __| |/ __| |  __/ _ \| |/ _` |/ _ \ '__| | |    | '__/ _ \/ _` | __/ _ \| '__|
  / ____ \ |_| | || (_) | | | | | | (_| | |_| | (__  | | | (_) | | (_| |  __/ |    | |____| | |  __/ (_| | || (_) | |   
 /_/    \_\__,_|\__\___/|_| |_| |_|\__,_|\__|_|\___| |_|  \___/|_|\__,_|\___|_|     \_____|_|  \___|\__,_|\__\___/|_|   
                                                                                                                        
"""


ConfigFiles = os.path.join(os.path.dirname(__file__), '../Config/config.json')

with open(ConfigFiles, 'r') as file: ## Import Config
    config = json.load(file)


## Hub 
def Hub():
    click.echo("© 2023 AFC-Teams. All rights reserved")
    click.echo(click.style(text, fg='green'))
    click.echo(
    """
        Choisiez votre mode
        
        1. Mode createur
        2. exit
        3. AFC Teams Information
    """
    )
    choix = click.prompt("Entre votre choix ")
    click.option('--choix', prompt='Entrez votre choix', help='Votre nom.')
    
    if choix == "1":
        print("Mode createur")
    elif choix == "2" :
        print("exit")
    elif choix == "3" : 
        print("AFC Teams Information")
    else : 
        print()
    


## Script
def createDay(nbr,path):
    
    for i in range(nbr+1):
        os.chdir(path)
        if i > 0:
            days = f"Jour {i}"
            newpath = os.path.join(path,days)
            os.mkdir(days)
            if os.path.exists(newpath):
                os.chdir(newpath)
                # os.mkdir("TP")
                # os.mkdir("Theorie")
                for i in range(len(config["folder"]["underFolder"])):
                    os.mkdir(config["folder"]["underFolder"][i])
            


def CreateDoss():
    
    NameDoss = input("Inserez le nom de votre de la matiere: ")
    NbrDays = input("Inserez le nombre de jour: ")
    NameAdress = config["folder"]["path"]
    while not os.path.exists(NameAdress) :
        print("Le chemin indiqué n'exsite pas , veuillez reverifié le chemin dans votre fichier de configuration")
        # NameAdress = input("Inserez le chemin du repertoir: ")
   
    while not NbrDays.isdigit() :
        NbrDays = input("Inserez le nombre de jour: ")
        
    os.chdir(NameAdress) #Changement de directory
    os.mkdir(NameDoss) #Creation de dossier
    NewPath = os.path.join(NameAdress,NameDoss)
    os.chdir(NewPath) #Changement de directory
    
    if os.path.exists(NewPath):
        createDay(int(NbrDays),NewPath)
    else:
        print("Il n'y a rien")

Hub()


# A venir 
# Systeme de preset 
# Exportation en .exe
