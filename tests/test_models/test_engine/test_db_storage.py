#!/usr/bin/python3
"""This module contains unit tests for the DBStorage class."""
from datetime import datetime
import inspect
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.db_storage import DBStorage
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json
import os
import pycodestyle
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}
storage_t = os.getenv("HBNB_TYPE_STORAGE")


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "DBStorage only")
class TestDBStorage(unittest.TestCase):
    """Defines the test suite for the DBStorage class."""

    @classmethod
    def setUpClass(cls):
        """Set up the testing environment."""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        cls.db = create_engine(
            f'mysql+mysqldb://{user}:{password}@{host}/{database}',
            pool_pre_ping=True)

    def setUp(self):
        """Set up the test environment."""
        self.session = sessionmaker(bind=self.db)
        self.storage = DBStorage()
        self.storage.reload()

    def tearDown(self):
        """Tear down the test environment."""
        self.storage._DBStorage__session.close()

    def test_all(self):
        """Test the all method."""
        state = State(name='California')
        self.storage.new(state)
        self.storage.save()
        states = self.storage.all(State)
        self.assertIn(state, states.values())

    def test_new(self):
        """Test the new method."""
        state = State(name='California')
        self.storage.new(state)
        self.storage.save()
        states = self.session().query(State).all()
        self.assertIn(state, states)

    def test_save(self):
        """Test the save method."""
        state = State(name='California')
        self.storage.new(state)
        self.storage.save()
        states = self.session().query(State).all()
        self.assertIn(state, states)

    def test_delete(self):
        """Test the delete method."""
        state = State(name='California')
        self.storage.new(state)
        self.storage.save()
        self.storage.delete(state)
        states = self.session().query(State).all()
        self.assertNotIn(state, states)

    def test_reload(self):
        """Test the reload method."""
        state = State(name='California')
        self.storage.new(state)
        self.storage.save()
        self.storage.reload()
        states = self.session().query(State).all()
        self.assertNotIn(state, states)

if __name__ == '__main__':
    unittest.main()
