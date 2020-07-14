import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)



app.config["MONGO_DBNAME"] = 'recipes'
app.config["MONGO_URI"] = 'mongodb+srv://Schnoeff:Brooker3798@recipies-ewzrm.mongodb.net/recipes?retryWrites=true&w=majority'

mongo = PyMongo(app)

# This function allows data to be found on mongodb
@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template('recipes.html', recipes=mongo.db.recipe_details.find())

# This function also allows the data to be found on mongodb
@app.route('/add_recipes')
def add_recipes():
    return render_template('addrecipe.html', course=mongo.db.recipe_course.find())

# This function allows data to be added to the sotrage on mongodb
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipe_details
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))

# This function allows for a single collection of data to be found via object id
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipe_details.find_one({"_id": ObjectId(recipe_id)})
    return render_template('editrecipe.html', recipe=the_recipe)

# This function allows for each field in the each field in the mongodb collection to be accessed and changed 
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipe_details
    recipes.update({'_id': ObjectId(recipe_id)},
                   {
        'recipe_name': request.form.get('recipe_name'),
        'servings': request.form.get('servings'),
        'ingredient_1': request.form.get('ingredient_1'),
        'ingredient_2': request.form.get('ingredient_2'),
        'ingredient_3': request.form.get('ingredient_3'),
        'ingredient_4': request.form.get('ingredient_4'),
        'ingredient_5': request.form.get('ingredient_5'),
        'ingredient_6': request.form.get('ingredient_6'),
        'ingredient_7': request.form.get('ingredient_7'),
        'ingredient_8': request.form.get('ingredient_8'),
        'ingredient_9': request.form.get('ingredient_9'),
        'ingredient_10': request.form.get('ingredient_10'),
        'method_1': request.form.get('method_1'),
        'method_2': request.form.get('method_2'),
        'method_3': request.form.get('method_3'),
        'method_4': request.form.get('method_4'),
        'method_5': request.form.get('method_5'),
        'method_6': request.form.get('method_6'),
        'method_7': request.form.get('method_7'),
        'method_8': request.form.get('method_8'),
        'method_9': request.form.get('method_9'),
        'method_10': request.form.get('method_10'),
    })
    return redirect(url_for('get_recipes'))

# This function allows for any data collection to be deleted 
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipe_details.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
