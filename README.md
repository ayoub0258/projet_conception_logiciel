# Hitster - Documentation

##### Hitster est un jeu de quiz musical dans lequel les participants doivent retrouver le titre et l'artiste de différents titres populaires de différentes époques. Pour fonctionner, le jeu est constitué de cartes contenant un QR code qui renvoie vers un extrait audio disponible sur Spotify, ainsi que la réponse au dos de la carte, comprenant une année, un artiste et le nom du titre.


## Table of Contents
<<<<<<< HEAD
 
=======

>>>>>>> hister
- [Fonctionnalités](#Fonctionnalités)
- [Installation](#installation)
- [Utilisation](#Utilisation)

## Fonctionnalités
    -Récupérer les titres et artistes des chansons populaires de différentes époques.
    -Générer des cartes liées à des codes QR pour chaque chanson, contenant :
      -> Un lien vers un extrait audio de Spotify.
      -> Le nom de l'artiste, le titre de la chanson et la date de sortie.
    -Compiler une playlist des chansons identifiées à partir de la liste des singles numéro un en France de Wikipedia.
    -Utiliser l'API Spotify pour rechercher chaque chanson et récupérer son extrait audio.
    -Générer des fichiers PDF pour chaque chanson contenant le code QR et les informations sur la chanson.


## Installation

Pour exécuter Hitster, suivez ces étapes :

    1/ Installez Python 3.x sur votre système.
    2/ Clonez ou téléchargez ce dépôt sur votre machine locale.
    3/ Installez les packages Python requis à l'aide de pip :

```bash
pip install -r requirements.txt
```

- Configurez vos identifiants d'API Spotify en créant un fichier .env dans le répertoire du projet avec le format suivant :

```bash
CLIENT_ID=<Votre identifiant client Spotify>
CLIENT_SECRET=<Votre secret client Spotify>
REDIRECT_URI=<Votre URI de redirection Spotify>
```

## Utilisation

Pour utiliser Hitster, exécutez la commande suivante:
```bash
python hitster.py <votre_nom_de_playlist> <votre_description_de_playlist>
```
Remplacez <votre_nom_de_playlist> et <votre_description_de_playlist> par le nom et la description de votre playlist désirée.

## Profiter du Jeu : 
Hitster recherchera des chansons populaires, générera des cartes liées à des codes QR et les compilera dans une playlist prête à être imprimée.
## Imprimer et Jouer :
Une fois le processus terminé, vous disposerez de fichiers PDF prêts à être imprimés. Amusez-vous à jouer au quiz musical avec vos amis et votre famille !
