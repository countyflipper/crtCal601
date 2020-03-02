import unittest
from Calculator import Calculator
from CsvReader import CsvReader



class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_subtraction(self):
        self.test_data = CsvReader('/src/Subtraction.csv').data
        for row in self.test_data:
            self.assertEqual(self.calculator.subtract(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
            print(self.calculator.result)
        print("------------------Subtraction-------------------")

    def test_addition(self):
        self.test_data = CsvReader('/src/Addition.csv').data
        for row1 in self.test_data:
            result1 = float(row1['Result'])
            self.assertEqual(self.calculator.add(int(row1['Value 1']), int(row1['Value 2'])), int(row1['Result']))
            self.assertEqual(self.calculator.result, int(row1['Result']))
            print(self.calculator.result)
        print("------------------Addition-------------------")

    def test_multiplication(self):
        self.test_data = CsvReader('/src/Multiplication.csv').data
        for row in self.test_data:
            self.assertEqual(self.calculator.multiply(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
            print(self.calculator.result)
        print("------------------Multiplication-------------------")

    def test_divide(self):
        self.test_data = CsvReader('/src/Division.csv').data
        for row in self.test_data:
            self.assertAlmostEqual(self.calculator.division(int(row['Value 1']), int(row['Value 2'])), float(row['Result']))
            self.assertAlmostEqual(self.calculator.result, float(row['Result']))
            print(self.calculator.result)
        print("------------------Division-------------------")

    def test_square(self):
        self.test_data = CsvReader('/src/Square.csv').data
        for row in self.test_data:
            self.calculator.square(int(row['Value 1']))
            self.assertAlmostEqual(self.calculator.result, int(row['Result']))
            print(self.calculator.result)
        print("------------------Square-------------------")


    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

if __name__ == '__main__':
    unittest.main()