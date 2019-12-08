import json
from app import db
from datetime import datetime

class Voucher(db.Model):
    __tablename__ = 'voucher'
    id    = db.Column(db.Integer, primary_key=True)
    code  = db.Column(db.String(64), index=True)
    value = db.Column(db.Integer)
    start = db.Column(db.DateTime, default=datetime.utcnow)
    end   = db.Column(db.DateTime, default=datetime.utcnow)
    
    def is_overlap(self):
        """
        Check overlaping between start and end
        """
        return True
    
    def is_overlap_with_other(self):
        """
        Check overlaping between start and end with other for updating
        """
        return True
    
    def __repr__(self):
        return '<Voucher {}>'.format(self.code)
