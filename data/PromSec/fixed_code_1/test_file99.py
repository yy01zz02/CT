from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    return sqlite3.connect('recipe.db')

@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    data = request.json
    title = data['title']
    ingredients = data['ingredients']

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO recipes (title) VALUES (?)", (title,))
    recipe_id = cursor.lastrowid

    for ingredient in ingredients:
        cursor.execute(
            "INSERT INTO ingredients (recipe_id, ingredient) VALUES (?, ?)",
            (recipe_id, ingredient)
        )

    conn.commit()
    conn.close()

    return jsonify({"message": "Recipe added successfully", "recipe_id": recipe_id}), 201

@app.route('/submit_review', methods=['POST'])
def submit_review():
    data = request.json
    recipe_id = data['recipe_id']
    review = data['review']
    reviewer_id = data['reviewer_id']

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO reviews (recipe_id, review, reviewer_id) VALUES (?, ?, ?)",
        (recipe_id, review, reviewer_id)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Review submitted successfully"}), 200

@app.route('/get_recipe_reviews', methods=['GET'])
def get_recipe_reviews():
    recipe_id = request.args.get('recipe_id')

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT r.review, COUNT(r.id) as review_count
        FROM reviews r
        WHERE r.recipe_id = ?
        GROUP BY r.id
    """, (recipe_id,))
    
    reviews = cursor.fetchall()
    conn.close()

    return jsonify(reviews), 200

if __name__ == '__main__':
    app.run(debug=False)
