from extensions import db
from sqlalchemy import JSON

class MomoFamily(db.Model):
    __tablename__ = 'momofamily'

    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    About = db.Column(db.JSON)  # Assuming you want to store this as a JSON
    ProfilePic = db.Column(db.String(255))
    CoverPhoto = db.Column(db.String(255))
    Gallery = db.Column(db.JSON)
    Posts = db.Column(db.JSON)  # Change the data type to JSON for Posts
    Bio = db.Column(db.JSON)
    Timeline = db.Column(db.JSON)

    def __init__(self, Name, About, ProfilePic, CoverPhoto, Gallery, Posts, Bio, Timeline):
        self.Name = Name
        self.About = About
        self.ProfilePic = ProfilePic
        self.CoverPhoto = CoverPhoto
        self.Gallery = Gallery
        self.Posts = Posts  # Store Posts as JSON
        self.Bio = Bio
        self.Timeline = Timeline

    def __repr__(self):
        return f"<MomoFamily {self.ID}: {self.Name}>"