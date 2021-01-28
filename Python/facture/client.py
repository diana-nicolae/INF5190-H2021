class Client(object):
    def __init__(self, numero):
        self.numero = numero
        self.liste_article_client = {}
    
    def ajouter_article(self, numero_article, quantite):
        self.liste_article_client[numero_article] = quantite

def creer_client(numero_client, nom_article, quantite, liste_client):
    client_existant = False
    for client in liste_client:
        if client.numero == numero_client: # On met a jour la liste d'articles du client
            client_existant = True
            client.ajouter_article(nom_article, quantite)
            break
    if not client_existant:
        nouveau_client = Client(numero_client) # On crée un nouveau client
        nouveau_client.ajouter_article(nom_article, quantite) # On ajoute l'article
        liste_client.append(nouveau_client) # On ajoute le client à la liste des clients