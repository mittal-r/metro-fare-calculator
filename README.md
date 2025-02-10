# Fare Calculation System

A Python-based system for calculating public transportation fares with peak/non-peak pricing and daily/weekly capping.

## Features

- Peak hour fare calculations
- Route-specific pricing rules
- Daily and weekly fare capping
- CSV input handling
- Comprehensive unit test coverage

## Installation
NA

## Usage

1. Prepare CSV file with format:
```csv
Green,Red,2025-02-10T08:30:00
Red,Green,2025-02-10T09:15:00
```
Here entry contains source,destination,timestamp


2. Run the application:
```bash
python app/main.py
```

## Testing

Run all unit tests with:
```bash
python -m unittest discover test/ -v
```

### Test Coverage
- Data validation and loading
- Fare calculation logic
- Peak hour detection
- Input file handling
- Configuration validation

## Configuration

Modify fare rules in:
- `app/constants.py` - Route definitions
- `app/data.py` - Peak hours and pricing rules

## Input Format
| Column     | Format         | Example                  |
|------------|----------------|--------------------------|
| source     | Route name     | Green                    |
| destination| Route name     | Red                      |
| timestamp  | ISO 8601       | 2025-02-10T08:30:00      |

## Technologies
- Python 3.9+
- unittest framework
- CSV module
- datetime handling
