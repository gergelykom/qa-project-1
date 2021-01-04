import unittest
import pytest
from flask import url_for
from flask_testing import TestCase



class TestBase(TestCase):
    def create_app(self):

        
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True
                )
        return app

    def setUp(self):
        db.create_all()
        test_species = Species(description = 'Test the app')
        db.session.add(test_species)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_home_get(self):

        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_create_get(self):

        response = self.client.get(url_for('create'))
        self.assertEqual(response.status_code, 200)

    def test_update_get(self):
        response = self.client.get(url_for('update', id=1), follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_confirm_get(self):
        response = self.client.get(url_for('confirm', id=1), follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_unconfirmed_get(self):
        response = self.client.get(url_for('unconfirmed', id=1), follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_delete_get(self):
        response = self.client.get(url_for('delete', id=1), follow_redirects=True)
        self.assertEqual(response.status_code,200)

class TestRead(TestBase):
    def test_read_species(self):
        response = self.client.get(url_for('home'))
        self.assertIn(b'Test the app', response.data)

class TestCreate(TestBase):
    def test_create_species(self):
        response = self.client.post(url_for('create'),
            data=dict(description = 'Create a new species'),
            follow_redirects = True
        )
        self.assertIn(b'Create a new species', response.data)

class TestUpdate(TestBase):
    def test_update_species(self):
        response = self.client.post(url_for('update', id=1),
            data=dict(description = 'Update new species'),
            follow_redirects = True
        )
        self.assertIn(b'Update new species', response.data)

class TestDelete(TestBase):
    def test_delete_species(self):
        response = self.client.get(url_for('delete', id=1),
            follow_redirects = True
        )
        self.assertNotIn(b'Test the app', response.data)


class TestConfirm(TestBase):
    def test_confirm_species(self):
        response = self.client.get(url_for('confirm', id=1),
            follow_redirects = True
        )
        self.assertIn(b'Test the app', response.data)

class TestUnconfirmed(TestBase):
    def test_confirm_species(self):
        response = self.client.get(url_for('unconfirmed', id=1),
            follow_redirects = True
        )
        self.assertIn(b'Test the app', response.data)
