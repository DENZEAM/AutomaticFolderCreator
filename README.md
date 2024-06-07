
# Créateur Automatique de Dossiers

## Aperçu du Projet

Ce projet est un devoir scolaire conçu pour créer une structure de dossiers automatique pour organiser des fichiers. Le script automatise le processus de création de dossiers et sous-dossiers prédéfinis en fonction d'un fichier de configuration.

## Fonctionnalités

- Crée automatiquement une structure de dossiers basée sur la configuration fournie.
- Assure que les répertoires nécessaires existent pour organiser les fichiers.
- Facile à configurer et à utiliser.

## Installation

1. **Cloner le dépôt :**

   ```bash
   git clone https://github.com/DENZEAM/AutomaticFolderCreator
   ```

2. **Naviguer dans le répertoire du projet :**

   ```bash
   cd AutomaticFolderCreator
   ```

3. **Installer les dépendances requises :**

   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

1. **Exécuter le script :**

   Pour exécuter le script, utilisez la commande suivante :

   ```bash
   python gui.py
   ```

2. **Configuration :**

   La structure des dossiers et autres paramètres sont définis dans le répertoire `Config`. Modifiez les fichiers de configuration selon vos besoins.

## Dépendances

Ce projet nécessite les bibliothèques Python suivantes :

- `click`
- `colorama`

Vous pouvez installer toutes les dépendances en utilisant la commande suivante :

```bash
pip install click colorama
```

## Structure du Projet

- `.git` - Répertoire Git pour le contrôle de version.
- `build` - Répertoire pour les fichiers liés à la construction.
- `Config` - Répertoire contenant les fichiers de configuration pour la structure des dossiers.
- `Dependencies` - Répertoire contenant les dépendances requises par le projet.
- `LICENSE` - Fichier de licence du projet.
- `test.py` - Script principal pour exécuter le processus de création de dossiers automatique.

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## Contribution

Les contributions sont les bienvenues ! Si vous souhaitez contribuer à ce projet, veuillez forker le dépôt et soumettre une pull request.
