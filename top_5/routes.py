from top_5 import app
from flask import render_template

#Home Route
@app.route('/')
def home():
    return render_template("home.html")
#Favorite (Top 5) route
@app.route('/favorite', methods=['GET','POST'])
def favorite():
    favorite_dict = {1: "Tom Brady", 2:"Julian Edelman",3:"Kevin Garnett",4:"Paul Pierce",5:"David Ortiz"}
    return render_template('favorite.html', favorite_dict = favorite_dict)