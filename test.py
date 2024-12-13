import unittest

from main import main

class Test01(unittest.TestCase):
    def test_5_columns(self):
        '''
        Here we test if the main function produces 5 lists
        '''
        result = main()
        self.assertEqual(5, len(result.values()))

class Test02(unittest.TestCase):
    def test_5_num(self):
        '''
        Here we test if the main function produces values of 5 numbers
        '''
        result = main()
        self.assertEqual(5, len(result["b"]))


class Test02(unittest.TestCase):
    def test_type_int(self):
        '''
        Here we test if the main function returns a list with only int
        '''
        data = type(0)
        result = main()
        self.assertEqual(data, type(result["b"][0]))
