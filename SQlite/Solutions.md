## Solutions 

### Pour créer la base de données :

1. Telecharger sqlite3 :

*MACOS* : 
```
brew install sqlite3
```

*LINUX* :
```
apt-get install sqlit3
```

2. Ouvrir la console `sqlite3` en specifiant la base de données à créer :
```
sqlite3 musique.db
```
3. Créer la base de données à partir du script SQL :
```
> .read script.sql
```
4. Fermer la console :
```
> .exit
```
