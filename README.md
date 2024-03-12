# ![Hitster Logo](hitster_logo.png)

**Hitster** vise à offrir une expérience ludique de quiz musical, où les joueurs doivent identifier les titres et les artistes de chansons populaires à travers différentes époques. Le concept central réside dans la capacité à ordonner ces titres retrouvés dans l'ordre chronologique, similaire à un jeu de timeline. Pour cela, le jeu repose sur des cartes contenant un QR code lié à un extrait audio sur Spotify, ainsi que les informations de l'artiste, du titre et de l'année correspondante. Constatant les limitations de la version de base du jeu en termes de cartes disponibles, l'implémentation de notre propre jeu Hitster se basera sur l'API de Spotify. Pour constituer la playlist nécessaire, nous utiliserons les données extraites de Wikipedia, en particulier la liste des singles numéro un en France, pour obtenir les titres ainsi que leurs dates. Ensuite, chaque titre sera recherché sur Spotify pour récupérer son extrait audio. Enfin, l'application générera un fichier PDF pour chaque extrait, contenant le QR code menant à l'extrait audio, ainsi que les informations essentielles telles que l'artiste, le titre et la date de l'œuvre. Grâce à un jeton d'API Spotify, l'application pourra ainsi produire un ensemble de fichiers prêts à être imprimés pour une expérience de jeu complète.

## 📚 Table des matières

- [Prérequis](#prérequis)
- [Fonctionnalités](#fonctionnalités)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Profiter du Jeu](#profiter-du-jeu)
- [Imprimer et Jouer](#imprimer-et-jouer)

## 🛠️ Prérequis

- Avoir un compte Spotify.
- Générer CLIENT_ID et CLIENT_SECRET à l'aide de l'API Spotify.
- Installer Python 3.x sur votre système.

## ⚙️ Fonctionnalités

1. Récupération des informations des utilisateurs : l'utilisateur doit d'abord créer un compte sur l'API Spotify.
2. Génération d'un token d'accès stocké dans le fichier .cach, en utilisant la bibliothèque Spotipy.
3. Création de la playlist et récupération de ses informations.
4. Parcours d'un fichier CSV contenant des chansons."Vous pouvez choisir les chansons que vous voulez et les mettre dans le fichier chansons.csv sans toucher à la 1er ligne (Titre, Artiste)"
5. Pour chaque chanson, recherche des informations via son titre.
6. Récupération des URI nécessaires.
7. Ajout des URI à la playlist.
8. Parcours de la playlist pour récupérer les URL, dates et QR codes.

### 📊 Diagramme de Classe

![Hitster Image](hitster_diagramme_de_classe.png)

## 💻 Installation

Pour exécuter Hitster, suivez ces étapes :

1. Clonez ou téléchargez ce dépôt sur votre machine locale.
2. Installez les packages Python requis à l'aide de pip :

```bash
pip install -r requirements.txt

```

3. Configurez vos identifiants d'API Spotify en créant un fichier .env dans le répertoire du projet avec le format suivant :


```bash
CLIENT_ID=<Votre identifiant client Spotify>
CLIENT_SECRET=<Votre secret client Spotify>
REDIRECT_URI=<Votre URI de redirection Spotify>
```

## 🚀 Utilisation

Pour utiliser Hitster, exécutez la commande suivante:
```bash
python main.py <votre_nom_de_playlist> <votre_description_de_playlist>
```
Remplacez <votre_nom_de_playlist> et <votre_description_de_playlist> par le nom et la description de votre playlist désirée.

## 🎵 Profiter du Jeu : 
Hitster recherchera des chansons populaires, générera des cartes liées à des codes QR et les compilera dans une playlist prête à être imprimée.
## 🎮 Imprimer et Jouer :
Une fois le processus terminé, vous disposerez de fichiers PDF prêts à être imprimés. Amusez-vous à jouer au quiz musical avec vos amis et votre famille !
