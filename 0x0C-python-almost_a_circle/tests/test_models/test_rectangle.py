#!/usr/bin/python3
import inspect
from contextlib import redirect_stdout
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
import json
import io
from io import StringIO
import sys

"""Runs test cases for the Rectangle module"""

class test_rectangle(unittest.TestCase):
    """tests the tectangle"""

    def width_testn(self):
        """tests rect width"""
        self.assertEqual(7, self.r.width)

    def height_test(self):
        """tests rect height"""
        self.assertEqual(12, self.r.height)

    def x_test(self):
        """tests rect x"""

        self.r.x = 54
        self.assertEqual(54, self.r.x)
        self.assertEqual(0, self.r.y)

    def y_test(self):
        """tests rect y"""
        self.r.y = 45
        self.assertEqual(45, self.r.y)
        self.assertEqual(0, self.r.x)

    def test_update_x(self):
        '''
            Testing the update method
        '''
        self.r.update(54, 20, 10, 9)
        self.assertEqual(9, self.r.x)
