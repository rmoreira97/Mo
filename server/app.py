from flask import Flask, jsonify, request
from flask_cors import CORS
from extensions import db
from models import MomoFamily
import os
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def hello():
        return 'MOMO!'

    @app.route('/api/gorillas', methods=['GET'])
    def get_gorillas():
        gorillas = MomoFamily.query.all()
        gorilla_data = [{
            'ID': gorilla.ID,
            'Name': gorilla.Name,
            'About': gorilla.About,
            'ProfilePic': gorilla.ProfilePic,
            'CoverPhoto':gorilla.CoverPhoto,
            'Gallery': gorilla.Gallery,
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
        db.session.commit()
        return jsonify({
            'ID': gorilla.ID,
            'Name': gorilla.Name,
            'About': gorilla.About,
            'ProfilePic': gorilla.ProfilePic,
            'CoverPhoto':gorilla.CoverPhoto,
            'Gallery': gorilla.Gallery,
            'Bio': gorilla.Bio,
            'Timeline': gorilla.Timeline
        }), 200
        
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)