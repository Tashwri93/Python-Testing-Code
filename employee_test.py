import unittest
from employee_class import Employee

class TestRaiseSalary(unittest.TestCase):

    def setUp(self):
        self.sam = Employee('sam', 'smith', 30000)


    def test_give_default_raise(self):
        self.sam.give_raise()
        self.assertEqual(self.sam.annual_salary, 35000)


    def test_give_custome_raise(self):
        self.sam.give_raise(500)
        self.assertEqual(self.sam.annual_salary, 30500)
unittest.main()
