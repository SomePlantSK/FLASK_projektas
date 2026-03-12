#app.py - pagrindine Flask aplikacijos logika
#siame faile aprasyti marsrutai (routes)

#reikalingos bibliotekos(importai)
from flask import Flask, render_template

#sukuriame Flask aplikacijos objekta
app = Flask(__name__)

#marsrutas: pagrindinis puslapis
#URL: /
#metodas: GET
#atvaizduoja index.html sablona
@app.route("/") #dekoratorius
def index():
    return render_template("index.html")

#marstrutas: kontaktu puslapis (forma)
#metodai GET ir POST
@app.route("/kontaktai") #dekoratorius
def kontaktai():
    return render_template("kontaktai.html")

#marstrutas: kontaktu puslapis (forma)
#metodai GET ir POST
@app.route("/apie") #dekoratorius
def apie():
    return render_template("apie.html")

#aplikacijos paleidimas
#paleidimo metu kai debug = True - automatinis aplikacijos perkrovimas pakeitus koda + klaidu rodymas
if __name__ == "__main__":
    app.run(debug=True)