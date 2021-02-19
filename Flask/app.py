from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.route("/confirmation")
def confirmation():
    return render_template("confirmation.html")

# Plusierus routes qui pointes vers la meme opération
@app.route("/home", methods=["GET", "POST"] )
@app.route("/", methods=["GET", "POST"])
def formulaire():
    # Si le client envoie une requete GET, on affiche le formulaire
    if request.method == "GET":
        return render_template("formulaire.html")
    # Sinon la méthode est POST, on récupère les informations entrées
    else:
        text = request.form["text"]
        radio1 = request.form.getlist("pchoix") != None
        radio2 = request.form.getlist("dchoix") != None
        select = request.form.get("liste-choix")
        #verification simple des champs non vide
        if text == "" or (radio1 == "" and radio2 == "") or select == "":
            #envoyer une variable interprétable par Jinja2
            return render_template("formulaire.html", error="Tous les champs sont obligatoires!")
            #Plusieurs autres validations peuvent etre faites de la meme façon

        else:
            # On récupère le choix à partir de la check box, un seul choix possible donc l'une des 
            # variable est à None
            if radio1 is None:
                radio = radio2
            else:
                radio = radio1
            # Si valides, on écrit les informations récupérées dans le fichier log.txt
            log = open("log.txt", "w")
            log.write("text : %s"%text + "\nradio : %s"%radio + "\nselect : %s"%select)
            return redirect("/confirmation")
        




