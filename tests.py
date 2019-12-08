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
        start1 = datetime.strptime('2018-09-01 17:00:00', "%Y-%m-%d %H:%M:%S")
        end1   = datetime.strptime('2019-09-15 17:00:00', '%Y-%m-%d %H:%M:%S')
        start2 = datetime.strptime('2019-09-01 17:00:00', '%Y-%m-%d %H:%M:%S')
        end2   = datetime.strptime('2019-09-15 17:00:00', '%Y-%m-%d %H:%M:%S')
        v1 = Voucher(code='SNSD', value=5000, start=start1, end=end1)
        v2 = Voucher(code='SNSD', value=10000, start=start2, end=end2)
        db.session.add(v1)
        db.session.add(v2)
        db.session.commit()
        start3 = datetime.strptime('2019-09-14 17:00:00', "%Y-%m-%d %H:%M:%S")
        end3   = datetime.strptime('2019-09-15 17:00:00', "%Y-%m-%d %H:%M:%S")
        v3     = Voucher(code='SNSD', value=10000, start=start3, end=end3)
        self.assertEqual(v3.is_overlap(), True)
        
        v3.start = datetime.strptime('2020-09-14 17:00:00', "%Y-%m-%d %H:%M:%S")
        v3.end = datetime.strptime('2021-09-14 17:00:00', "%Y-%m-%d %H:%M:%S")
        self.assertEqual(v3.is_overlap(), False)
    
    def test_overlap_with_others(self):
        """Test unit overlap with others for updating"""
        start1 = datetime.strptime('2018-09-01 17:00:00', "%Y-%m-%d %H:%M:%S")
        end1   = datetime.strptime('2019-09-15 17:00:00', '%Y-%m-%d %H:%M:%S')
        start2 = datetime.strptime('2019-09-01 17:00:00', '%Y-%m-%d %H:%M:%S')
        end2   = datetime.strptime('2019-09-15 17:00:00', '%Y-%m-%d %H:%M:%S')
        v1 = Voucher(code='SNSD', value=5000, start=start1, end=end1)
        v2 = Voucher(code='SNSD', value=10000, start=start2, end=end2)
        db.session.add(v1)
        db.session.add(v2)
        db.session.commit()
        v2.start = datetime.strptime('2018-09-01 17:00:00', "%Y-%m-%d %H:%M:%S")
        v2.end   = datetime.strptime('2019-09-15 17:00:00', '%Y-%m-%d %H:%M:%S')
        self.assertEqual(v2.is_overlap_with_other(), True)
        v2.start = datetime.strptime('2020-09-01 17:00:00', "%Y-%m-%d %H:%M:%S")
        v2.end  = datetime.strptime('2021-09-01 17:00:00', "%Y-%m-%d %H:%M:%S")
        self.assertEqual(v2.is_overlap_with_other(), False)

    def test_get_vouchers(self):
        """Test API can get a Voucher (GET request)"""
        res = self.client().get('/api/v1.0/vouchers')
        self.assertEqual(res.status_code, 200)
        self.assertIn('vouchers', str(res.data))

    def test_voucher_creation(self):
        """Test API can create a Voucher (POST request)"""
        v1 = dict(code='SNSD', value=10000, start='2018-09-01 17:00:00', end='2019-09-15 17:00:00')
        res = self.client().post('/api/v1.0/vouchers', data=json.dumps(v1, indent=4), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn('SNSD', str(res.data))

        v2  = dict(code='SNSD', value=10000, start='2018-09-01 17:00:00', end='2019-09-15 17:00:00')
        res = self.client().post('/api/v1.0/vouchers', data=v2, content_type='application/json')
        self.assertEqual(res.status_code, 400)
        self.assertNotIn('SNSD', str(res.data))

    def test_voucher_update(self):
        """Test API can update a Voucher (PUT request)"""
        start1 = datetime.strptime('2018-09-01 17:00:00', "%Y-%m-%d %H:%M:%S")
        end1   = datetime.strptime('2019-09-15 17:00:00', '%Y-%m-%d %H:%M:%S')
        v1 = Voucher(code='SNSD', value=5000, start=start1, end=end1)
        v1.save()
        
        params = dict(code='ABCD', value=10000, start='2018-09-01 17:00:00', end='2019-09-15 17:00:00')
        res = self.client().put('/api/v1.0/vouchers/{}'.format(v1.id), data=json.dumps(params, indent=4), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn('ABCD', str(res.data))

if __name__ == '__main__':
    unittest.main(verbosity = 2)