import os
import csv
from datetime import datetime

from constants import Routes

class InputReader:
    def __init__(self)-> None:
        self.file_path = ""
        self.user_travel_data = []

    def get_input(self)-> None:
        self.file_path = input("Please enter the file path containing user travel data\n")

    def validate_file(self)-> None:
        self._does_file_exist()
        self._check_csv_extension()
        self._check_file_size()

    def _does_file_exist(self)-> None:
        # validate input file path exists
        if not os.path.exists(self.file_path):
            print("File does not exist")
            raise Exception("Invalid file provided")

    def _check_csv_extension(self)-> None:
        # validate input file path is valid csv
        if not self.file_path.lower().endswith('.csv'):
            print("File is not a CSV")
            raise Exception("File is not of type csv")

    def _check_file_size(self)-> None:
        # validate input file size is non 0
        if os.path.getsize(self.file_path) == 0:
            raise Exception("File size is 0")

    def read_csv(self)-> None:
        # read the given csv file into a dictionary
        # also does basic validation in the the entry
        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self._validate_input(row)
                data = {
                    "source": row[0].lower().strip(), # str
                    "destination": row[1].lower().strip(), # str
                    "timestamp": self._get_datetime(row[2].strip()) # datetime
                }
                self.user_travel_data.append(data)

    def _validate_input(self, row: list)-> None:
        # validate number of entries in the csv
        if not len(row) == 3:
            raise Exception(f"Invalid entry {row}")

        # validate datatypes of entries
        for i in (0, 1):
            # Raise error if the given route doesn't match the default routes
            try:
                getattr(Routes, row[i])
            except AttributeError as e:
                raise Exception(f"Invalid metro line: {row[i]}")

    def _get_datetime(self, iso_time: str) -> int:
        # return python datetime for given time string
        try:
            return datetime.strptime(iso_time, "%Y-%m-%dT%H:%M:%S")
        except Exception as e:
            print (f"Error {e}")
            raise Exception(f"Invalid date time format for {iso_time}.")
