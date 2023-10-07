import json
import requests
import random
from pystyle import Colors, Colorate, Center
from time import sleep
from pymongo import MongoClient
import sys

# Connexion à la base de données MongoDB
client = MongoClient("database-ici")
db = client.test


def keysystem():
    key = input(Colorate.Diagonal(Colors.yellow_to_red, ('Enter the key: ')))
    #data = {"key": "gAygqssvw9Q#b7fh7#vY"}
    #db.key.insert_one(data)
    user = db.key.find_one({"key": key})
    if user:
        print("Key Found")
    else:
        print("The key not found")
        sys.exit()


keysystem()

# Effacer la console
def clear_console():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

# Fonction pour envoyer un message via un webhook Discord
def send_message(webhook_url, message):
    username = ".gg/RR9qwcbHdG"  # Remplacez par le nom d'utilisateur souhaité
    avatar = "https://picsum.photos/id/{}/200".format(random.randint(1, 500))
    
    data = {
        "content": message,
        "username": username,
        "avatar_url": avatar,
        "tts": False
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    response = requests.post(webhook_url, json=data, headers=headers)
    
    if response.status_code == 429:
        clear_console()
        print("[!] Trop de requêtes - Attente avant nouvelle tentative...")
        sleep(2)
        return False
    elif not response.ok:
        clear_console()
        print("[!] Échec de l'envoi du message !")
        print(response.text)  # Affichez la réponse JSON de Discord pour obtenir des informations sur l'erreur
        sleep(15)
        return False

    clear_console()
    print(Colorate.Diagonal(Colors.yellow_to_red, Center.XCenter(header_final)))
    print(Colorate.Diagonal(Colors.blue_to_cyan, (f"Message envoyé ! {sent_count} ")))
    return True

# En-tête du programme
header_final = """
  ▄ ▄   ▄███▄   ███    ▄  █ ████▄ ████▄ █  █▀        ▄▄▄▄▄   █ ▄▄  ██   █▀▄▀█ 
 █   █  █▀   ▀  █  █  █   █ █   █ █   █ █▄█         █     ▀▄ █   █ █ █  █ █ █ 
█ ▄   █ ██▄▄    █ ▀ ▄ ██▀▀█ █   █ █   █ █▀▄       ▄  ▀▀▀▀▄   █▀▀▀  █▄▄█ █ ▄ █ 
█  █  █ █▄   ▄▀ █  ▄▀ █   █ ▀████ ▀████ █  █       ▀▄▄▄▄▀    █     █  █ █   █ 
 █ █ █  ▀███▀   ███      █                █                   █       █    █  
  ▀ ▀                   ▀                ▀                     ▀     █    ▀   
                                                                    ▀         
By Awa                                                                                                                   
"""

clear_console()
print(Colorate.Diagonal(Colors.yellow_to_red, Center.XCenter(header_final)))

# Demander l'URL du webhook
webhook_url = input("[?] Webhook URL ↓ ")
if not webhook_url.startswith("https://discord.com/api/webhooks/"):
    clear_console()
    print("[!] Veuillez insérer un lien valide !")
    sleep(2)
else:
    # Demander le message à envoyer
    message1 = input("[?] Message à envoyer ↓ ")
    
    sent_count = 0
    while True:  # Boucle infinie pour envoyer continuellement des messages
        if send_message(webhook_url, message1):
            sent_count += 1
