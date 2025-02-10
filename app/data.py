from datetime import time

# Define fare rule for the given routes.
fare_rules = {
    "green": {
        "green": {
            "price": {
                "peak": 2,
                "non_peak": 1,
            },
            "cap": {
                "daily": 8,
                "weekly": 55
            }
        },
        "red": {
            "price": {
                "peak": 4,
                "non_peak": 3,
            },
            "cap": {
                "daily": 15,
                "weekly": 90
            }
        }
    },
    "red": {
        "green": {
            "price": {
                "peak": 3,
                "non_peak": 2,
            },
            "cap": {
                "daily": 15,
                "weekly": 90
            }
        },
        "red": {
            "price": {
                "peak": 3,
                "non_peak": 2,
            },
            "cap": {
                "daily": 12,
                "weekly": 70
            }
        }
    }
}

# Define peak hours for each day using the weekday number as keys (0=Monday, 6=Sunday)
peak_hours = [
    [(time(8, 0), time(10, 0)), (time(16, 30), time(19, 0))],  # Monday
    [(time(8, 0), time(10, 0)), (time(16, 30), time(19, 0))],  # Tuesday
    [(time(8, 0), time(10, 0)), (time(16, 30), time(19, 0))],  # Wednesday
    [(time(8, 0), time(10, 0)), (time(16, 30), time(19, 0))],  # Thursday
    [(time(8, 0), time(10, 0)), (time(16, 30), time(19, 0))],  # Friday
    [(time(10, 0), time(14, 0)), (time(18, 0), time(23, 0))],  # Saturday
    [(time(18, 0), time(23, 0))]  # Sunday
]
