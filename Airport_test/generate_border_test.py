
import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PlaneClient import generate_border_coordinate 


class TestBorderGenerate(unittest.TestCase):

  #  def setUp(self):

    def test_function(self):
        result=generate_border_coordinate()
        self.assertIsInstance(result,tuple)
        print(result)
