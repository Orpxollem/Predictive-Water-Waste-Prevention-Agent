class DecisionEngine:
    def evaluate(self, percepts):
        flow = percepts["flow_rate"]
        day = percepts["day"]
        period = percepts["period"]

        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

        # 🚨 Rule 1: Off-peak weekday usage = suspicious
        if day in weekdays and period == "off_peak" and flow > 1:
            return "HIGH"

        # 📊 Rule 2: Normal classification
        if flow < 5:
            return "LOW"
        elif flow <= 8:
            return "MEDIUM"
        else:
            return "HIGH"