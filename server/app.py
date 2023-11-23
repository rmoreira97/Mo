from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gorilla_database.db'  # Use SQLite for simplicity
db = SQLAlchemy(app)

# Import the MomoFamily model from models.py
from models import MomoFamily

@app.route('/api/gorillas', methods=['GET'])
def get_gorillas():
    gorillas = MomoFamily.query.all()
    gorilla_data = []

    for gorilla in gorillas:
        gorilla_data.append({
            'ID': gorilla.ID,
            'Name': gorilla.Name,
            'Gender': gorilla.Gender,
            'Birthdate': gorilla.Birthdate,
            'Location': gorilla.Location,
            'Father': gorilla.Father,
            'Mother': gorilla.Mother,
            'ImageUrl': gorilla.ImageUrl,
        })

    return jsonify({'gorillas': gorilla_data})

@app.route('/api/gorillas/<int:gorilla_id>', methods=['GET'])
def get_gorilla(gorilla_id):
    gorilla = MomoFamily.query.get(gorilla_id)
    if gorilla:
        return jsonify({
            'ID': gorilla.ID,
            'Name': gorilla.Name,
            'Gender': gorilla.Gender,
            'Birthdate': gorilla.Birthdate,
            'Location': gorilla.Location,
            'Father': gorilla.Father,
            'Mother': gorilla.Mother,
            'ImageUrl': gorilla.ImageUrl,
            'Gallery': gorilla.Gallery,
            'Bio': gorilla.Bio,
        })
    else:
        return jsonify({'message': 'Gorilla not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
