import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipes'
app.config["MONGO_URI"] = 'mongodb+srv://Schnoeff:Brooker3798@recipies-ewzrm.mongodb.net/recipes?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template('recipes.html', recipes=mongo.db.recipe_details.find())

@app.route('/add_recipes')
def add_recipes():
    return render_template('addrecipe.html', course=mongo.db.recipe_course.find())

@app.route('/insert_recipe' , methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipe_details
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)