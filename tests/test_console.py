#!/usr/bin/python3
"""Unittest module for the console"""

import unittest
import os
import json
import pycodestyle
import io
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from unittest.mock import patch
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review



class TestCommand(unittest.TestCase):
    """Class that tests the console"""
    
    def setUp(self):
        """Function empties file.json"""
        FileStorage._FileStorage__objects = {}
        FileStorage().save()

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "Not FileStorage")
    def test_create_fs(self):
        """test the create command"""
        storage = FileStorage()
        storage.reload()
        opt = r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[0-9a-f]{4}-[0-9a-f]{12}'
        with self.assertRaises(AttributeError):
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("create BaseModel updated_at=0.0"
                                     " created_at=0.0")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create User email="printty@gmail.com"'
                                 ' password="peacebeuntoyou"')
        result = f.getvalue().strip()
        self.assertRegex(result, opt)
        email = storage.all()[f'User.{result}'].email
        self.assertEqual(email, "printty@gmail.com")
        password = storage.all()[f'User.{result}'].password
        self.assertEqual(password, "peacebeuntoyou")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create State citychi="bravo"'
                                 ' number="7" pi="3.14"')
        result = f.getvalue().strip()
        self.assertRegex(result, opt)
        citychi = storage.all()[f'State.{result}'].citychi
        self.assertEqual(citychi, "bravo")
        number = storage.all()[f'State.{result}'].number
        self.assertEqual(number, '7')
        pi = storage.all()[f'State.{result}'].pi
        self.assertEqual(pi, '3.14')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create City citychi="bravo" number="7"'
                                 ' pi="3.14"')
        result = f.getvalue().strip()
        self.assertRegex(result, opt)
        citychi = storage.all()[f'City.{result}'].citychi
        self.assertEqual(citychi, "bravo")
        number = storage.all()[f'City.{result}'].number
        self.assertEqual(number, '7')
        pi = storage.all()[f'City.{result}'].pi
        self.assertEqual(pi, '3.14')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create Amenity citychi="bravo"'
                                 ' number="7" pi="3.14"')
        result = f.getvalue().strip()
        self.assertRegex(result, opt)
        citychi = storage.all()[f'Amenity.{result}'].citychi
        self.assertEqual(citychi, "bravo")
        number = storage.all()[f'Amenity.{result}'].number
        self.assertEqual(number, '7')
        pi = storage.all()[f'Amenity.{result}'].pi
        self.assertEqual(pi, '3.14')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create Place citychi="bravo"'
                                 ' number="7" pi="3.14"')
        result = f.getvalue().strip()
        self.assertRegex(result, opt)
        citychi = storage.all()[f'Place.{result}'].citychi
        self.assertEqual(citychi, "bravo")
        number = storage.all()[f'Place.{result}'].number
        self.assertEqual(number, '7')
        pi = storage.all()[f'Place.{result}'].pi
        self.assertEqual(pi, '3.14')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create Review citychi="bravo"'
                                 ' number="7" pi="3.14"')
        result = f.getvalue().strip()
        self.assertRegex(result, opt)
        citychi = storage.all()[f'Review.{result}'].citychi
        self.assertEqual(citychi, "bravo")
        number = storage.all()[f'Review.{result}'].number
        self.assertEqual(number, '7')
        pi = storage.all()[f'Review.{result}'].pi
        self.assertEqual(pi, '3.14')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create')
        opt = '** class name missing **\n'
        self.assertEqual(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create NotClass')
        opt = '** class doesn\'t exist **\n'
        self.assertEqual(f.getvalue(), opt)

    def testPycodeStyle(self):
        """Pycodestyle test for console.py"""
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(['console.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_doc_console(self):
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)


if __name__ == '__main__':
    unittest.main()
