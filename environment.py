import random

class Environment:
    def get_percepts(self):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        current_day = random.choice(days)
        hour = random.randint(0, 23)

        if current_day == "Saturday":
            period = "washing_period" if 6 <= hour <= 13 else "off_peak"
        else:
            if 4 <= hour <= 7:
                period = "morning_peak"
            elif 18 <= hour <= 21:
                period = "evening_peak"
            else:
                period = "off_peak"

        flow_rate = round(random.uniform(0.5, 12.0), 2)

        return {
            "flow_rate": flow_rate,
            "day": current_day,
            "hour": hour,
            "period": period
        }