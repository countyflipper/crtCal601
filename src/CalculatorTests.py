import unittest
from Calculator import Calculator
from CsvReader import CsvReader



class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_square(self):
        test_data = CsvReader('/src/Square.csv').data
        for row in test_data:
            self.assertAlmostEqual(self.calculator.square(int(row['Value 1']),int(row['Result'])))
            self.assertAlmostEqual(self.calculator.result, int(row['Result']))
            print(self.calculator.result)
        print("------------------Square-------------------")

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

if __name__ == '__main__':
    unittest.main()