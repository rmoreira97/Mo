from flask import Flask, jsonify, request
from flask_cors import CORS
from extensions import db
from models import MomoFamily
import os
import json
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)


    # Set up the Flask app configuration using environment variables
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def hello():
        return 'MOMO!'

    @app.route('/api/gorillas/<int:gorilla_id>/posts', methods=['GET'])
    def get_gorilla_posts(gorilla_id):
     gorilla = db.session.get(MomoFamily, gorilla_id)
     if gorilla:
         gorilla_posts = gorilla.Posts if gorilla.Posts else []
         return jsonify(gorilla_posts)
     else:
         return jsonify({'message': 'Gorilla not found'}), 404

    @app.route('/api/gorillas', methods=['GET'])
    def get_gorillas():
        gorillas = MomoFamily.query.all()
        gorilla_data = [{
            'ID': gorilla.ID,
            'Name': gorilla.Name,
            'About': gorilla.About,
            'ProfilePic': gorilla.ProfilePic,
            'CoverPhoto': gorilla.CoverPhoto,
            'Gallery': gorilla.Gallery,
            'Posts': gorilla.Posts,
            'Bio': gorilla.Bio,
            'Timeline': gorilla.Timeline
        } for gorilla in gorillas]
        return jsonify({'gorillas': gorilla_data})

    @app.route('/api/gorillas/<int:gorilla_id>', methods=['GET'])
    def get_gorilla(gorilla_id):
        gorilla = db.session.get(MomoFamily, gorilla_id)
        if gorilla:
            app.logger.info(f'Found gorilla: {gorilla.Name}, CoverPhoto: {gorilla.CoverPhoto}')
            return jsonify({
                'ID': gorilla.ID,
                'Name': gorilla.Name,
                'About': gorilla.About,
                'ProfilePic': gorilla.ProfilePic,
                'CoverPhoto': gorilla.CoverPhoto,
                'Gallery': gorilla.Gallery,
                'Posts': gorilla.Posts,
                'Bio': gorilla.Bio,
                'Timeline': gorilla.Timeline
            })
        else:
            app.logger.warning('Gorilla not found')
            return jsonify({'message': 'Gorilla not found'}), 404

    @app.route('/api/gorillas/<int:gorilla_id>', methods=['PUT'])
    def update_gorilla(gorilla_id):
        gorilla = db.session.get(MomoFamily, gorilla_id)
        if not gorilla:
            return jsonify({'message': 'Gorilla not found'}), 404

        data = request.json
        # Here you may need to ensure that your JSON structure matches what you expect
        gorilla.About = data.get('About', gorilla.About)
        gorilla.Bio = data.get('Bio', gorilla.Bio)
        gorilla.Gallery = data.get('Gallery', gorilla.Gallery)
       
       
    @app.route('/api/gorillas/<int:gorilla_id>/addPost', methods=['POST'])
    def add_post_to_gorilla(gorilla_id):
            gorilla = db.session.query(MomoFamily).get(gorilla_id)
            if not gorilla:
                return jsonify({'message': 'Gorilla not found'}), 404

            if request.is_json:
                data = request.get_json()
                new_post = {
                    'Date': data.get('Date'),
                    'Caption': data.get('Caption'),
                    'Media': {
                        'Url': data.get('Media', {}).get('Url'),
                        'Type': data.get('Media', {}).get('Type')
                    }
                }

                # Add the new post to the gorilla's posts
                gorilla.Posts = gorilla.Posts or []  # Initialize as an empty list if Posts is None
                gorilla.Posts.append(new_post)

                db.session.add(gorilla)
                db.session.commit()
                return jsonify(new_post), 201
            else:
                return jsonify({'message': 'Invalid JSON data'}), 400

    return app

flask_app = create_app()

if __name__ == '__main__':
    flask_app.run()