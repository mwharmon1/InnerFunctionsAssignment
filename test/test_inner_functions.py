"""Author: Michael Harmon
   Last Date Modified: 9/30/2019
   Description: Unit tests for the measurements function.
"""

import unittest
from source_files import inner_functions_assignment as ifa


class MyTestCase(unittest.TestCase):
    def test_measurements_rectangle(self):
        self.assertEqual(ifa.measurements([2.1, 3.4]), "Perimeter = 11.0 Area = 7.14")

    def test_measurements_square(self):
        self.assertEqual(ifa.measurements([3.5]), "Perimeter = 14.0 Area = 12.25")


if __name__ == '__main__':
    unittest.main()
