import unittest
from city_functions import get_city_country

class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        city_country = get_city_country('london', 'england')
        self.assertEqual(city_country, 'London, England')


    def test_city_country_population(self):
        city_country = get_city_country('london', 'england', 500)
        self.assertEqual(city_country, 'London, England, Population = ' + str(500))

unittest.main()
        
        
