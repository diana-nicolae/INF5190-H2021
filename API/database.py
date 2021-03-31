import sqlite3
from livre import Livre


class Database:
    def __init__(self):
        self.connection = None
    
    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db/livre.db')
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    def get_livres(self):
        cursor = self.get_connection().cursor()
        cursor.execute('select * from livre')
        livres = cursor.fetchall()
        return (Livre(livre[0], livre[1], livre[2], livre[3], livre[4], livre[5]) for livre in livres)
    
    def get_livre(self, id):
        cursor = self.get_connection().cursor()
        cursor.execute('select * from livre where id=?', (id,))
        livre = cursor.fetchone()
        return(Livre(livre[0], livre[1], livre[2], livre[3], livre[4], livre[5]))

    def set_livre(self, livre):
        connection = self.get_connection()
        connection.execute('insert into livre(titre, auteur, annee_publication, nbr_pages, nbr_chapitres)' 'values(?,?,?,?,?)', (livre.titre, livre.auteur, livre.annee_publication, livre.nbr_pages, livre.nbr_chapitres))
        connection.commit()
        cursor = connection.cursor()
        cursor.execute('select last_insert_rowid()')
        result = cursor.fetchone()
        livre.set_id(result[0])
        return livre

    def delete_livre(self, livre):
        connection = self.get_connection()
        connection.execute("delete from livre where id=?", (livre.id,))
        connection.commit()