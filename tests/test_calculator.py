import unittest
from src.services.calculator import calculate_steps
from src.config import Config

class TestCalculator(unittest.TestCase):
    def test_calculate_steps(self):
        # Test case 1: Normal case
        self.assertEqual(calculate_steps(100, 70, "Moderate"), 2473)

        # Test case 2: Different pace
        self.assertEqual(calculate_steps(100, 70, "Brisk"), 2040)

        # Test case 3: Different weight
        self.assertEqual(calculate_steps(100, 80, "Moderate"), 2164)

    def test_invalid_pace(self):
        # Test case 4: Invalid pace
        with self.assertRaises(KeyError):
            calculate_steps(100, 70, "Invalid")

    def test_config_values(self):
        # Test that the calculation uses values from Config
        original_met = Config.MET_VALUES["Moderate"]
        original_steps_per_minute = Config.STEPS_PER_MINUTE

        try:
            # Modify Config values
            Config.MET_VALUES["Moderate"] = 4.0
            Config.STEPS_PER_MINUTE = 120

            # Test with modified values
            self.assertEqual(calculate_steps(100, 70, "Moderate"), 2448)
        finally:
            # Restore original values
            Config.MET_VALUES["Moderate"] = original_met
            Config.STEPS_PER_MINUTE = original_steps_per_minute

if __name__ == '__main__':
    unittest.main()