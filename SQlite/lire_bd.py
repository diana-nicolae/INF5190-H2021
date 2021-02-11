import sqlite3

#etablir une connexion avec la BD
connection = sqlite3.connect('musique.db')
#definir un curseur
cursor = connection.cursor()

#recuperer tous les artistes
cursor.execute("select * from artiste")
for row in cursor:
    #on range toutes les données dans des variables
    identifier, nom, est_solo, combien = row
    print("Artiste n: %d Nom : %s\n" %(identifier,nom))

print ("Choisissez un artiste en entrant son id :")
#on recupère le choix de l'utilisateur et on le cast en int
choix = int(input())
#pas sécuritère d'utiliser 'where artisteé-id=%d'
cursor.execute("select titre, annee from album where artiste_id=%d" %choix)
for row in cursor:
    titre,annee = row
    print ("%s %d\n" %(titre, annee))

# ne jamais oublier de fermer la connexion
connection.close()