# import os
# import click 
# import json


# text = r"""                _                        _   _        ______    _     _              _____                _             
#      /\        | |                      | | (_)      |  ____|  | |   | |            / ____|              | |            
#     /  \  _   _| |_ ___  _ __ ___   __ _| |_ _  ___  | |__ ___ | | __| | ___ _ __  | |     _ __ ___  __ _| |_ ___  _ __ 
#    / /\ \| | | | __/ _ \| '_ ` _ \ / _` | __| |/ __| |  __/ _ \| |/ _` |/ _ \ '__| | |    | '__/ _ \/ _` | __/ _ \| '__|
#   / ____ \ |_| | || (_) | | | | | | (_| | |_| | (__  | | | (_) | | (_| |  __/ |    | |____| | |  __/ (_| | || (_) | |   
#  /_/    \_\__,_|\__\___/|_| |_| |_|\__,_|\__|_|\___| |_|  \___/|_|\__,_|\___|_|     \_____|_|  \___|\__,_|\__\___/|_|   
                                                                                                                        
# """


# ConfigFiles = os.path.join(os.path.dirname(__file__), '../Config/config.json')

# with open(ConfigFiles, 'r') as file: ## Import Config
#     config = json.load(file)


# ## Hub 
# def Hub():
#     click.echo("© 2023 AFC-Teams. All rights reserved")
#     click.echo(click.style(text, fg='green'))
#     click.echo(
#     """
#         Choisiez votre mode
        
#         1. Mode createur
#         2. Mes Configuration
#         3. exit
#         4. AFC Teams Information
#     """
#     )
#     choix = click.prompt("Entre votre choix ")
#     click.option('--choix', prompt='Entrez votre choix', help='Votre nom.')
    
#     if choix == "1":
#         print("Mode createur")
#     elif choix == "2" :
#         print("Mes Configuration")
#     elif choix == "3" : 
#         print("exit")
#     elif choix == "4":
#         print("AFC Teams Information")
    


# ## Script

import os
import json
from tkinter import messagebox

def create_structure(json_file, base_path):
    print(json_file)
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)

        for folder, content in data['folder']['Preset'].items():
            if folder == 'underFolder':
                for subfolder in content:
                    os.makedirs(os.path.join(base_path, subfolder), exist_ok=True)
            elif folder == 'underUnderFolder':
                for subfolder, subsubfolders in content.items():
                    for subsubfolder in subsubfolders:
                        os.makedirs(os.path.join(base_path, subfolder, subsubfolder), exist_ok=True)
            elif folder == 'underFilesFolder':
                for subfolder, files in content.items():
                    for file in files:
                        open(os.path.join(base_path, subfolder, file), 'a').close()

        messagebox.showinfo("Succès", "La structure a été créée avec succès.")
    except Exception as e:
        messagebox.showerror("Erreur", str(e))