import sys
from fare_calculator import FareCalculator
from input_reader import InputReader


def run():
    try:
        # read and validate input
        input_reader = InputReader()
        input_reader.get_input()
        input_reader.validate_file()
        input_reader.read_csv()
        
        # calculate fare
        fare_calculator = FareCalculator()
        fare_calculator.calculate_fare(input_reader.user_travel_data)
        print(dict(fare_calculator.fare_breakup))

    except Exception as e:
        print(f"{e}")
        sys.exit(1)

if __name__ == "__main__":
    run()
