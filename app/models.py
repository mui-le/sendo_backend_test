import json
from app import db
from datetime import datetime
from flask import current_app

class Voucher(db.Model):
    __tablename__ = 'voucher'
    id    = db.Column(db.Integer, primary_key=True)
    code  = db.Column(db.String(64), index=True)
    value = db.Column(db.Integer)
    start = db.Column(db.DateTime, default=datetime.utcnow)
    end   = db.Column(db.DateTime, default=datetime.utcnow)
    
    def serialize(self):
        return {
            'id': self.id,
            'code': self.code, 
            'value': self.value,
            'start': self.start,
            'end': self.end,
        }
    
    @staticmethod
    def get_all():
        return Voucher.query.all()

    @staticmethod
    def get(id):
        return Voucher.query.filter_by(id=id)
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def is_overlap(self):
        """
        Check overlaping between start and end
        """
        query = "SELECT * FROM voucher v where v.`start` <= Datetime('{}') AND v.`end` >= Datetime('{}') ".format(self.end, self.start)
        result = db.engine.execute(query).fetchall()
        return False if len(result) is 0 else True
    
    def is_overlap_with_other(self):
        """
        Check overlaping between start and end with other for updating
        """
        query = "SELECT * FROM voucher v where v.`start` <= Datetime('{}') AND v.`end` >= Datetime('{}') AND id != '{}'".format(self.end, self.start, self.id)
        result = db.engine.execute(query).fetchall()
        return False if len(result) is 0 else True
    
    def __repr__(self):
        return '<Voucher {}>'.format(self.code)