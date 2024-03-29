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

with open ('input.txt','r') as infile:
    for line in infile:
        #on recupere les donnees du fichier en les separant par '|'
        splitted_line = line.split('|')
        #on essaye de matcher le nom d'artiste dans le fichier avec celui dans la base de donnees
        cursor.execute("select * from artiste where nom like ?", ('%'+splitted_line[0]+'%',))
        #on fetch les artistes qui matchent (si ils existent)
        existe =cursor.fetchall()
        if existe:
            #on recupere l'id
            artiste_id = cursor.fetchone()
            #on update les donnees de l'artiste correspondant a artiste_id en ajoutant le nouvel album à la table album
            cursor.execute(("insert into album(titre,annee,artiste_id)" "values(?,?,?)"),(splitted_line[1], splitted_line[2], artiste_id))
            #on commmit les changements
            connection.commit()
        else:
            #on insere le nouvel artiste dans la table artiste
            cursor.execute(("insert into artiste(nom, est_solo, nombre_individus)" "values(?,?,?)"), (splitted_line[0],0,1))
            #on recupere l'id du dernier artiste ajouté
            cursor.execute("select last_insert_rowid()")
            last_id = cursor.fetchone()[0]
            connection.commit()
            #a partir de l'id du dernier artiste ajouté on ajoute son album a la table album
            cursor.execute(("insert into album(titre,annee,artiste_id)" "values(?,?,?)"),(splitted_line[1], splitted_line[2], last_id))
            connection.commit()
infile.close()
connection.close()
