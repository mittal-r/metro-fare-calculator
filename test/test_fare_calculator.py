import unittest
from datetime import datetime
from app.fare_calculator import FareCalculator
from app.data import fare_rules

class TestFareCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = FareCalculator()
        self.sample_data = [
            {
                "source": "green",
                "destination": "green",
                "timestamp": datetime(2025, 2, 10, 8, 30) # Monday peak
            },
            {
                "source": "red",
                "destination": "red", 
                "timestamp": datetime(2025, 2, 10, 11, 0) # Monday non-peak
            }
        ]

    def test_peak_hour_detection(self):
        # Test peak hour
        peak_time = datetime(2025, 2, 10, 9, 0) # Monday 9AM
        self.assertTrue(self.calculator._is_peak_hour(peak_time))

        # Test non-peak hour
        non_peak_time = datetime(2025, 2, 10, 11, 0) # Monday 11AM
        self.assertFalse(self.calculator._is_peak_hour(non_peak_time))

        # Test weekend peak
        sat_time = datetime(2025, 2, 15, 12, 0) # Saturday noon
        self.assertTrue(self.calculator._is_peak_hour(sat_time))

    def test_fare_calculation(self):
        # Test peak fare
        self.assertEqual(self.calculator._get_fare(True, fare_rules["green"]["green"]["price"]), 2)
        
        # Test non-peak fare
        self.assertEqual(self.calculator._get_fare(False, fare_rules["red"]["red"]["price"]), 2)

    def test_fare_capping(self):
        # Test daily cap enforcement
        self.calculator.calculate_fare([{
            "source": "green",
            "destination": "green",
            "timestamp": datetime(2025, 2, 10, 8, 30)
        }]*10)  # 10 peak trips
        
        key = "green#green"
        monday_index = 0
        self.assertEqual(self.calculator.fare_breakup[key]["daily_total"][monday_index], 8) # Daily cap

    def test_full_calculation_flow(self):
        self.calculator.calculate_fare(self.sample_data)
        
        green_key = "green#green"
        red_key = "red#red"
        
        # Verify green route peak fare
        self.assertEqual(self.calculator.fare_breakup[green_key]["daily_total"][0], 2)
        
        # Verify red route non-peak fare
        self.assertEqual(self.calculator.fare_breakup[red_key]["daily_total"][0], 2)

if __name__ == '__main__':
    unittest.main()
