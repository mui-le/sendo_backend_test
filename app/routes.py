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

@app.route('/api/v1.0/vouchers', methods=['POST'])
def create_voucher():
    """register new voucher"""

@app.route('/api/v1.0/vouchers/<int:voucher_id>')
def get_voucher(voucher_id):
    """updating voucher"""

@app.route('/api/v1.0/vouchers/<int:voucher_id>', methods=['PUT'])
def update_voucher(voucher_id):
    """updating voucher"""

@app.route('/api/v1.0/vouchers/<int:voucher_id>', methods=['DELETE'])
def delete_voucher(voucher_id):

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)