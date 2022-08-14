import csv
from flask import Flask,jsonify

with open("articles.csv")as f:
    reader = csv.reader(f)
    data = list(reader)
    allarticles = data[1:]

app = Flask(__name__)
#routing to get all the articles
@app.route("/getarticle")
def getarticle():
    return jsonify({
        "data": allarticles[0]
    })

likedarticles = []
notlikedarticles = []

@app.route("/likedarticles", methods = ["POST"])
def likedarticles():
    articles = allarticles[0]
    likedarticles.append(articles)
    allarticles.pop(0)
    return jsonify({
        "status": "Success"
    })

@app.route("/notlikedarticles", method = ["POST"])
def unlikedarticles():
    articles = allarticles[0]
    notlikedarticles.append(articles)
    allarticles.pop(0)
    return jsonify({
        "status": "Success"
    })

app.run()