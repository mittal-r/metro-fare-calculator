import unittest
from app.constants import Routes

class TestConstants(unittest.TestCase):
    def test_route_enum_values(self):
        self.assertEqual(Routes.Green.value, "Green")
        self.assertEqual(Routes.Red.value, "Red")
        self.assertNotEqual(Routes.Green.value, Routes.Red.value)
        
    def test_enum_membership(self):
        self.assertIn("Green", [route.value for route in Routes])
        self.assertIn("Red", [route.value for route in Routes])
