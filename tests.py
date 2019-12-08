from flask import current_app
from datetime import datetime, timedelta
import unittest
import json

from app import db, create_app
from app.models import Voucher
from config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

class VoucherModelCase(unittest.TestCase):
    """This class represents the Voucher test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client
        db.create_all()

    def tearDown(self):
        """teardown all initialized variables."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_overlap(self):
        """Test unit overlap"""
    
    def test_overlap_with_others(self):
        """Test unit overlap with others for updating"""

    def test_get_vouchers(self):
        """Test API can get a Voucher (GET request)"""

    def test_voucher_creation(self):
        """Test API can create a Voucher (POST request)"""

    def test_voucher_update(self):
        """Test API can update a Voucher (PUT request)"""

if __name__ == '__main__':
    unittest.main(verbosity = 2)