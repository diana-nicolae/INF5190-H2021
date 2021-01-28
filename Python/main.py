from decimal import *

from facture.article import *
from facture.client import *

RABAIS = 0.15
NEW_LINE = "\n"
FICHIER_ENTREE = "entree.txt"


# lire_fichier du fichier + Création des objets de type Client et Article
def lire_fichier(liste_clients, liste_articles):
    with open(FICHIER_ENTREE) as les_lignes:
        for une_ligne in les_lignes:
            taxe_possible = ""
            if len(une_ligne.split()) == 5:
                numero_client, nom_article, quantite, prix, taxe_possible = une_ligne.split(' ')
            else:
                numero_client, nom_article, quantite, prix = une_ligne.split(' ')

            quantite = int(quantite)  # Conversion string to int
            prix = float(prix)  # Conversion string to float
            creer_client(numero_client, nom_article, quantite, liste_clients)
            creer_liste_articles(nom_article, prix, taxe_possible, liste_articles)
    les_lignes.close()


# Fin de la fonction lire_fichier


def creer_facture(liste_clients, liste_articles):
    for client in liste_clients:
        facture_client = open(client.numero + ".txt", "w")
        facture_client.write("Client numéro %s" % client.numero + NEW_LINE)
        facture_client.write(NEW_LINE)
        facture_client.write(
            "".rjust(15) + "No de produit".ljust(15) + "Qte".rjust(15) + "Prix".rjust(15) + "Total (tx)".rjust(
                15) + NEW_LINE)

        nb_article = 1
        total_facture = 0.0
        total_articles = 0

        # la liste des articles du client X dans la commande
        for cle, valeur in client.liste_article_client.items():
            total_articles += valeur
            # liste_prix va contenir le prix unitaire et le total en fct des taxes + quantite
            liste_prix = chercher_article(cle, valeur,
                                                     liste_articles)
            prix_unitaire = liste_prix[0]
            total_avec_taxe = liste_prix[1]
            total_facture += total_avec_taxe
            enumeration_produit = "Produit #" + str(nb_article)
            facture_client.write(
                enumeration_produit.ljust(15) + cle.ljust(15) + "{:15d}".format(valeur) + "{:15f}".format(
                    Decimal(prix_unitaire).quantize(Decimal('.01'))) + "{:15f}".format(
                    Decimal(total_avec_taxe).quantize(Decimal('.01'))) + NEW_LINE)
            ++nb_article

        # A partir d'ici : verifier si le rabais est applicable
        facture_client.write(NEW_LINE)
        if total_articles >= 100:
            facture_client.write("Total avant rabais :".ljust(20) + "{:10f}".format(
                Decimal(total_facture).quantize(Decimal('.01'))) + NEW_LINE)
            montant_rabais = total_facture * RABAIS
            facture_client.write(
                "Rabais : ".ljust(20) + "{:10f}".format(Decimal(montant_rabais).quantize(Decimal('.01'))) + NEW_LINE)
            facture_client.write("Total : ".ljust(20) + "{:10f}".format(
                Decimal(total_facture - montant_rabais).quantize(Decimal('.01'))) + NEW_LINE)
            facture_client.write(NEW_LINE)
        else:
            facture_client.write("Aucun rabais est applicable sur cette commande !" + NEW_LINE)
            facture_client.write(
                "Total : " + format(Decimal(total_facture).quantize(Decimal('.01'))) + NEW_LINE)

        facture_client.close()

# Fin de la fonction creer_facture


def main():
    liste_clients = []  # création d'une liste vide
    liste_articles = []  # création d'une liste vide
    lire_fichier(liste_clients, liste_articles)  # On commence par lire le fichier de commande
    creer_facture(liste_clients, liste_articles)


# Fin de la fonction main


main()  # Fonction principale du programme
