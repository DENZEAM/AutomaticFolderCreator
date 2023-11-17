
import json

with open('Config/config.json', 'r') as fichier:
    # Charger les données JSON depuis le fichier
    donnees = json.load(fichier)
    
print(donnees["folder"]["path"])