import unittest
from src.services.calculator import calculate_steps_to_burn_calories

class TestCalculator(unittest.TestCase):
    def test_calculate_steps_to_burn_calories(self):
        # Test case 1: Normal case (average pace)
        self.assertAlmostEqual(calculate_steps_to_burn_calories(70, 100, "average"), 2500, delta=50)

        # Test case 2: Slow pace
        self.assertAlmostEqual(calculate_steps_to_burn_calories(70, 100, "slow"), 3125, delta=50)

        # Test case 3: Fast pace
        self.assertAlmostEqual(calculate_steps_to_burn_calories(70, 100, "fast"), 1750, delta=50)

        # Test case 4: Different weight
        self.assertAlmostEqual(calculate_steps_to_burn_calories(80, 100, "average"), 2188, delta=50)

    def test_invalid_pace(self):
        # Test case 5: Invalid pace (should default to average)
        steps_invalid = calculate_steps_to_burn_calories(70, 100, "invalid")
        steps_average = calculate_steps_to_burn_calories(70, 100, "average")
        self.assertEqual(steps_invalid, steps_average)

    def test_edge_cases(self):
        # Test case 6: Zero calories
        self.assertEqual(calculate_steps_to_burn_calories(70, 0, "average"), 0)

        # Test case 7: Very low weight
        self.assertGreater(calculate_steps_to_burn_calories(30, 100, "average"), 0)

        # Test case 8: Very high weight
        self.assertLess(calculate_steps_to_burn_calories(200, 100, "average"), 1000)

if __name__ == '__main__':
    unittest.main()