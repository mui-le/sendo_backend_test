from app import app
from app.models import Voucher
from flask import jsonify
from flask import request
from datetime import datetime
from flask import abort
from flask import make_response
from app import db

@app.route('/')
@app.route('/index')
def index():
    return "<span class='welcome'>Sendo Voucher sys test!</span>"

@app.route('/api/v1.0/vouchers')
def get_vouchers():
    """Get all new vouchers"""
    vouchers = Voucher.get_all()
    result = jsonify(vouchers=[e.serialize() for e in vouchers])
    return make_response(result)

@app.route('/api/v1.0/vouchers', methods=['POST'])
def create_voucher():
    """register new voucher"""
    data = request.get_json(silent=True)
    if not data or not 'code' or not 'value' or not 'start' or not 'end' in data:
        abort(400)

    start = datetime.strptime(data['start'], '%Y-%m-%d %H:%M:%S')
    end   = datetime.strptime(data['end'], '%Y-%m-%d %H:%M:%S')
    if end <= start:
        abort(400)
    voucher = Voucher(code=data['code'], value=data['value'], start=start, end=end)
    if voucher.is_overlap():
        abort(400)
    voucher.save()
    return make_response(jsonify(voucher=voucher.serialize()), 201)

@app.route('/api/v1.0/vouchers/<int:voucher_id>')
def get_voucher(voucher_id):
    """get voucher"""

@app.route('/api/v1.0/vouchers/<int:voucher_id>', methods=['PUT'])
def update_voucher(voucher_id):
    """updating voucher"""

@app.route('/api/v1.0/vouchers/<int:voucher_id>', methods=['DELETE'])
def delete_voucher(voucher_id):
    """deleting voucher"""

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)