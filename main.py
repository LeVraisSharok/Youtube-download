import os
from pytube import YouTube
from colorama import init, Fore
import time

# Initialisation de colorama
init(autoreset=True)

# Fonction pour afficher le texte en multicolore arc-en-ciel
def afficher_texte_arc_en_ciel(texte):
    couleurs = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    texte_arc_en_ciel = ""
    for i, caractere in enumerate(texte):
        couleur = couleurs[i % len(couleurs)]
        texte_arc_en_ciel += couleur + caractere
    print(texte_arc_en_ciel)

# Fonction pour télécharger la vidéo
def telecharger_video(lien, format):
    try:
        yt = YouTube(lien)
        if format == "mp3":
            stream = yt.streams.filter(only_audio=True).first()
        else:
            stream = yt.streams.get_highest_resolution()
        print(f"Téléchargement de la vidéo: {yt.title}")
        stream.download()
        print("Téléchargement terminé.")
    except Exception as e:
        print(f"Une erreur s'est produite: {str(e)}")

# Texte en arc-en-ciel
texte = """
░██████╗██╗░░██╗░█████╗░██████╗░░█████╗░██╗░░██╗
██╔════╝██║░░██║██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
╚█████╗░███████║███████║██████╔╝██║░░██║█████═╝░
░╚═══██╗██╔══██║██╔══██║██╔══██╗██║░░██║██╔═██╗░
██████╔╝██║░░██║██║░░██║██║░░██║╚█████╔╝██║░╚██╗
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
"""

# Affichage du texte en multicolore arc-en-ciel
afficher_texte_arc_en_ciel(texte)

# Texte "Dev by Sharok_" en arc-en-ciel
texte_dev = "Dev by Sharok_"
afficher_texte_arc_en_ciel(texte_dev)

# Texte "Dm me discord -> Sharok_" en arc-en-ciel
texte_discord = "Dm me discord -> Sharok_"
afficher_texte_arc_en_ciel(texte_discord)


# Demande de lien YouTube à l'utilisateur
lien = input("Veuillez entrer le lien de la vidéo YouTube que vous souhaitez télécharger : ")

# Demande de format à l'utilisateur
format = input("Veuillez choisir le format de téléchargement (mp3/mp4) : ").lower()

# Vérification du format
if format not in ["mp3", "mp4"]:
    print("Format invalide. Veuillez choisir entre 'mp3' et 'mp4'.")
else:
    # Téléchargement de la vidéo dans le format choisi
    telecharger_video(lien, format)
