from app import db
import json


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)

    def to_json(self):
        return {"content": self.content}
