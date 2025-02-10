from collections import defaultdict
from data import fare_rules
from data import peak_hours

class FareCalculator:
    def __init__(self):
        self.fare_breakup = defaultdict(lambda: {"daily_total": [0, 0, 0, 0, 0, 0, 0]})
        # fare_breakup = {source#destination: {"daily_total": [0,0,0,...]}}} # weekday 0, 1 ... 6

    def calculate_fare(self, user_travel_data):
        # import pdb; pdb.set_trace()
        for each in user_travel_data:
            src = each["source"]
            dest = each["destination"]
            timestamp = each["timestamp"]
            fare_rule = fare_rules[src][dest]
            fare_limit = self._get_fare_limit(src, dest, timestamp.weekday(), fare_rule["cap"])
            if fare_limit > 0:
                is_peak = self._is_peak_hour(timestamp)
                price_rule = fare_rule["price"]
                fare = self._get_fare(is_peak, price_rule)
                total_fare = min(fare, fare_limit)
                self.fare_breakup[f"{src}#{dest}"]["daily_total"][timestamp.weekday()] += total_fare

    def _is_peak_hour(self, timestamp):
        # Check if the given timestamp is in peak hour
        day_of_week = timestamp.weekday()
        peak_range = peak_hours[day_of_week]

        for start, end in peak_range:
            if start <= timestamp.time() <= end:
                return True

        return False

    def _get_fare_limit(self, src, dest, weekday, fare_cap_rule):
        # check the weekly and daily cap and return the available fare limit
        fares = self.fare_breakup[f"{src}#{dest}"]['daily_total']

        fare_limit = 0

        weekly_fare_so_far = sum(fares)
        weekly_cap = fare_cap_rule["weekly"]
        if weekly_fare_so_far < weekly_cap:
            fare_limit = weekly_cap - weekly_fare_so_far

        daily_fare_so_far = fares[weekday]
        daily_cap = fare_cap_rule["daily"]
        if daily_fare_so_far < daily_cap:
            fare_limit = min(fare_limit, daily_cap - daily_fare_so_far)
        else:
            fare_limit = 0

        return fare_limit

    def _get_fare(self, is_peak, price_rule):
        if is_peak:
            return price_rule["peak"]
        return price_rule["non_peak"]
