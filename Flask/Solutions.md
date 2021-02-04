# Solutions :


1. Installer flask : `pip install flask`

2. Pour rouler l'applications :
```
export FLASK_APP=app.py
flask run

```
3. On peut aussi configurer l'environnement de developpement pour que les modifications soient prises en considèration sans avoir à redemarrer l'application :

```
export FLASK_ENV=developpement
```

**RQ : ** la commande `make run` permet de rouler toutes ses étapes.


4. La commande `pip freeze > requirements.txt` permet de lister toutes les librairies (et leurs versions) utilisées par l'application et de rediriger le contenu vers le fichier `requirements.txt`

5. La commande `pip install -r requirements.txt` permet d'installer toutes les librairies contenues dans le fihcier `requirements.txt`
