from application import db
from datetime import datetime
class Species(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(36), nullable=False)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    
    