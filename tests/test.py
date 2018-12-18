#coding=utf-8
#pylint: disable=invalid-name

"""
    Тестирование по unittest
"""

import unittest
import main


class Test_Main(unittest.TestCase):
    """ Тестирующий класс """

    def testSum(self):
        """ Тестирование суммирования """
        self.assertEqual(main.mySum([1, 2, 3]), 6)
        self.assertEqual(main.mySum([1, 2, 2]), 5)


if __name__ == '__main__':
    unittest.main()
