import unittest
from city_functions import city_function


class CityTestCase(unittest.TestCase):
    """Test for city_functions.py"""

    def test_city_country(self):
        """Does the string like city, country?"""
        string = city_function('beijing', 'china')
        self.assertEqual(string, 'Beijing, China')

    def test_city_country_population(self):
        """Does the string also accept population?"""
        string = city_function('santiago', 'chile', '5000000')
        self.assertEqual(string, 'Santiago, Chile - Population 5000000')


unittest.main()
