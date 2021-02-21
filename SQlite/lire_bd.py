"""
 Copyright 2021 Ela El-Heni

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

"""
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