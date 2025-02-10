import unittest
from unittest.mock import patch, mock_open
from datetime import datetime
from app.input_reader import InputReader
from app.constants import Routes
import os

class TestInputReader(unittest.TestCase):
    @patch('builtins.input', return_value='test.csv')
    def test_get_input(self, mock_input):
        reader = InputReader()
        reader.get_input()
        self.assertEqual(reader.file_path, 'test.csv')

    def test_file_validation(self):
        reader = InputReader()
        reader.file_path = 'test.csv'
        
        with patch('os.path.exists', return_value=True):
            reader._does_file_exist()
            
        with patch('os.path.exists', return_value=False):
            with self.assertRaises(Exception):
                reader._does_file_exist()

    def test_csv_extension_validation(self):
        reader = InputReader()
        reader.file_path = 'valid.csv'
        reader._check_csv_extension()  # Should not raise
        
        reader.file_path = 'invalid.txt'
        with self.assertRaises(Exception):
            reader._check_csv_extension()

    @patch('os.path.getsize')
    def test_file_size_validation(self, mock_getsize):
        reader = InputReader()
        reader.file_path = 'empty.csv'
        
        mock_getsize.return_value = 0
        with self.assertRaises(Exception):
            reader._check_file_size()

    def test_csv_parsing(self):
        test_data = '''Green,Red,2025-02-10T08:30:00
Red,Green,2025-02-10T09:15:00'''
        
        with patch('builtins.open', mock_open(read_data=test_data)):
            reader = InputReader()
            reader.file_path = 'test.csv'
            reader.read_csv()
            
            self.assertEqual(len(reader.user_travel_data), 2)
            self.assertEqual(reader.user_travel_data[0]['source'], 'green')
            self.assertIsInstance(reader.user_travel_data[0]['timestamp'], datetime)

    def test_invalid_row_handling(self):
        test_data = '''Green,Red
Red,Green,2025-02-10T09:15:00,extra'''
        
        with patch('builtins.open', mock_open(read_data=test_data)):
            reader = InputReader()
            reader.file_path = 'test.csv'
            with self.assertRaises(Exception):
                reader.read_csv()

    def test_datetime_parsing(self):
        reader = InputReader()
        valid_time = '2025-02-10T08:30:00'
        self.assertIsInstance(reader._get_datetime(valid_time), datetime)
        
        with self.assertRaises(Exception):
            reader._get_datetime('invalid-date')

if __name__ == '__main__':
    unittest.main()
