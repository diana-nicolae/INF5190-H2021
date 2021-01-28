class Client(object):
    def __init__(self, numero):
        self.numero = numero  # type VARCHAR
        self.liste_article_client = {}  # Initialisation d'un dictionnaire

    def ajouter_article(self, numero_article, quantite):
        self.liste_article_client[numero_article] = quantite


# Fin de la fonction ajouter_article
# Fin de la classe Client

def creer_client(numero_client, nom_article, quantite, liste_clients):
    existant_client = False
    for client in liste_clients:
        if client.numero == numero_client:  # Alors on va mettre à jour notre client
            existant_client = True
            client.ajouter_article(nom_article, quantite)  # On ajout notre nouvelle article avec sa quantite
            # Je dois trouver le moyen d'écrire dans mon client
            break
    # Si la variable demeure à false, ça veut dire que nous n'avosn pas trouver notre client
    if not existant_client:
        nouveau_client = Client(numero_client)
        nouveau_client.ajouter_article(nom_article, quantite)
        liste_clients.append(nouveau_client)
# Fin de la fonction creer_client
