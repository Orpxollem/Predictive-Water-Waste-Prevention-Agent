class DecisionEngine:
    def evaluate(self, percepts):
        flow = percepts["flow_rate"]
        day = percepts["day"]
        period = percepts["period"]

        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

        # Usage is suspicious when high during time periods when people are likely away 
        if day in weekdays and period == "off_peak" and flow > 1:
            return "HIGH"

        if flow < 5:
            return "LOW"
        elif flow <= 8:
            return "MEDIUM"
        else:
            return "HIGH"