import random
import time

class Environment:
    def get_percepts(self):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        current_day = random.choice(days)

        # Simulate hour (0–23)
        hour = random.randint(0, 23)

        # Determine time period based on day
        if current_day == "Saturday":
            if 6 <= hour <= 13:
                period = "washing_period"
            else:
                period = "off_peak"

        else:
            if 4 <= hour <= 7:
                period = "morning_peak"      # bathing time
            elif 18 <= hour <= 21:
                period = "evening_peak"      # family activity
            else:
                period = "off_peak"

        # Simulate flow rate
        if random.random() < 0.8:
            flow_rate = round(random.uniform(0.5, 5.0), 2)
        else:
            flow_rate = round(random.uniform(6.0, 12.0), 2)

        # Duration in minutes
        duration = round(random.uniform(1, 30), 2)

        percepts = {
            "flow_rate": flow_rate,
            "day": current_day,
            "hour": hour,
            "period": period,
            "duration": duration
        }

        print("\n[PERCEPTS]")
        print(percepts)

        time.sleep(2)
        return percepts