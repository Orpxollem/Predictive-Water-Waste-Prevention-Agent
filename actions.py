class Actions:
    async def handle(self, risk, beliefs):
        if not beliefs.is_valve_open():
            print("[SYSTEM] Valve is CLOSED. Auto reopening...")
            beliefs.open_valve()
            return

        if risk == "LOW":
            print("[LOG] Normal usage.")
            return

        print(f"[ALERT] {risk} risk detected!")

        if risk == "HIGH":
            beliefs.close_valve()
            print("[ACTION] Valve automatically closed.")