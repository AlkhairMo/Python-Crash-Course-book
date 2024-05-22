import unittest
from city_functions import get_city


class TestCity(unittest.TestCase):
    def test_city_country(self):
        city_country = get_city('Santiago', 'Chile')
        self.assertEqual(city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        city_country_population = get_city('Khartoum', 'Sudan', 9_000_000)
        self.assertEqual(city_country_population, 'Khartoum, Sudan - population 9000000')


if __name__ == '__main__':
    unittest.main()
