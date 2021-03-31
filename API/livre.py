class Livre:
    def __init__(self, id, titre, auteur, annee_publication, nbr_pages, nbr_chapitres):
        self.id = id
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication
        self.nbr_pages = nbr_pages
        self.nbr_chapitres = nbr_chapitres

    def set_id(self,id):
        self.id = id

    def min_info_dictionnary(self):
        return {
            'id': self.id,
            'titre': self.titre
        }

    def all_info_dictionnary(self):
        return {
            'id': self.id,
            'titre': self.titre,
            'auteur': self.auteur,
            'annee_publication' : self.annee_publication,
            'nbr_pages': self.nbr_pages,
            'nbr_chapitres': self.nbr_chapitres
        }

insert_schema = {
    'type': 'object',
    'required': ['titre', 'auteur', 'annee_publication', 'nbr_pages', 'nbr_chapitres'],
    'proprieties': {
        'titre': {
            'type': 'string'
        },
        'auteur': {
            'type': 'string'
        },
        'annee_publication': {
            'type': 'string'
        },
        'nbr_pages': {
            'type': 'number'
        },
        'nbr_chapitres': {
            'type': 'number'
        }
    },
    'additionalProprieties': False
}