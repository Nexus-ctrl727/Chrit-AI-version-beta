api = "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"

import requests
from bs4 import BeautifulSoup
from googlesearch import search
import random

def get_web_content(url):
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        return ' '.join([p.get_text() for p in paragraphs][:3])  # Retourne les 3 premiers paragraphes
    except:
        return None

def search_online(query, num_results=3):
    try:
        search_results = list(search(query, num_results=num_results, lang='fr'))
        return search_results
    except:
        return []

def chatbot_response(user_input):
    # Si l'utilisateur demande quelque chose de factuel, on cherche sur Internet
    if '?' in user_input or any(keyword in user_input.lower() for keyword in ['qui est', 'quelle est', 'comment', 'pourquoi']):
        print("🔍 Je cherche des informations en ligne...")
        search_results = search_online(user_input)
        
        if search_results:
            for url in search_results[:2]:  # On prend les 2 premiers résultats
                content = get_web_content(url)
                if content:
                    return f"ℹ️ D'après {url} :\n{content[:500]}..."  # Limité à 500 caractères
        return "Je n'ai pas trouvé de réponse précise. Peux-tu reformuler ?"
    else:
        # Réponses génériques si ce n'est pas une question factuelle
        generic_responses = [
            "C'est intéressant ! Peux-tu en dire plus ?",
            "Je vois. Comment te sens-tu par rapport à ça ?",
            "Je n'ai pas trouvé d'infos en ligne. Pose-moi une question plus précise !"
        ]
        return random.choice(generic_responses)

# Boucle de discussion
print("🤖 Salut ! Je suis un bot connecté à Internet. Pose-moi une question ou dis-moi quelque chose.")
while True:
    user_input = input("\nToi : ")
    if user_input.lower() in ['exit', 'quitter', 'bye']:
        print("🤖 À bientôt !")
        break
    response = chatbot_response(user_input)
    print(f"🤖 {response}")
