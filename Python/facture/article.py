TAXE_FED = 0.05
TAXE_PROV = 0.09975


class Article(object):
    def __init__(self, nom_article, prix_unitaire, taxe_fed, taxe_prov):
        self.nom_article = nom_article
        self.prix_unitaire = prix_unitaire
        self.taxe_fed = taxe_fed
        self.taxe_prov = taxe_prov


def creer_liste_articles (nom_article, prix, taxe_possible, liste_articles):
    for article in liste_articles:
        if article.nom_article ==  nom_article:
            return
    indicateur_taxe_fed = False
    indicateur_taxe_prov = False
    taxe_possible = taxe_possible.rstrip('\n')

    if taxe_possible == "FP":
        indicateur_taxe_fed = True
        indicateur_taxe_prov = True
    elif taxe_possible == "P":
        indicateur_taxe_prov = True
    elif taxe_possible == "F":
        indicateur_taxe_fed = True

    nouvel_article = Article(nom_article, prix, indicateur_taxe_fed, indicateur_taxe_prov)
    liste_articles.append(nouvel_article)


def chercher_article(nom_article, quantite, liste_articles):
    liste_prix= []
    for article in liste_articles:
        if article.nom_article == nom_article:
            liste_prix.append(article.prix_unitaire)
            prix_quantite = article.prix_unitaire * quantite
            montant_taxe_fed = 0.0
            montant_taxe_prov = 0.0
            if article.taxe_fed:
                montant_taxe_fed = prix_quantite * TAXE_FED
            if article.taxe_prov:
                montant_taxe_prov = prix_quantite * TAXE_PROV
            prix_total = prix_quantite + montant_taxe_fed + montant_taxe_prov
            liste_prix.append(prix_total)
            return liste_prix
