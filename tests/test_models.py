import unittest
from src.models.beverton_holt import beverton_holt

class TestBevertonHoltModel(unittest.TestCase):

    def setUp(self):
        self.R_max = 1000
        self.K = 5000

    def test_population_growth(self):
        initial_population = 500
        expected_population = (self.R_max * initial_population) / (1 + (initial_population / self.K))
        calculated_population = beverton_holt(initial_population, self.R_max, self.K)
        self.assertAlmostEqual(calculated_population, expected_population, places=2)

    def test_population_at_capacity(self):
        initial_population = self.K
        expected_population = self.K  # At capacity, population should remain the same
        calculated_population = beverton_holt(initial_population, self.R_max, self.K)
        self.assertAlmostEqual(calculated_population, expected_population, places=2)

    def test_population_zero(self):
        initial_population = 0
        expected_population = 0  # If there are no individuals, population should remain zero
        calculated_population = beverton_holt(initial_population, self.R_max, self.K)
        self.assertAlmostEqual(calculated_population, expected_population, places=2)

if __name__ == '__main__':
    unittest.main()