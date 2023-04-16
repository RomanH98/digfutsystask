from app import db

class SearchRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String)
    group_name = db.Column(db.String)
    query_datetime = db.Column(db.DateTime)
    search_word = db.Column(db.String)