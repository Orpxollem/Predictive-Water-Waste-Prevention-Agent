import time
import threading

class Actions:
    def handle(self, risk, beliefs):
        # 1. Handle Reopening if Valve is Closed
        if not beliefs.is_valve_open():
            print("[SYSTEM] Valve is CLOSED.")
            # We use a standard input here because the agent should wait for the user to reopen it
            choice = input("Press R to reopen valve: ").strip().upper()
            if choice == "R":
                beliefs.open_valve()
                print("[ACTION] Valve reopened.")
            return

        # 2. Handle Low Risk
        if risk == "LOW":
            print("[LOG] Normal usage.")
            return

        # 3. Handle Medium & High Risk with 15-second timeout
        # Determine the prompts based on risk level
        if risk == "MEDIUM":
            print("[WARNING] Suspicious usage detected.")
            prompt_msg = "Press S to shut valve | I to ignore"
        else: # HIGH
            print("[ALERT] HIGH RISK! Possible leak detected!")
            prompt_msg = "Press S to shut valve NOW | O to keep open"

        print(prompt_msg)
        
        # Helper for timed input
        user_choice = {"value": None}
        def get_input():
            try:
                user_choice["value"] = input("Your choice: ").strip().upper()
            except EOFError:
                pass

        input_thread = threading.Thread(target=get_input)
        input_thread.daemon = True
        input_thread.start()

        # 15 Second Countdown
        for remaining in range(15, 0, -1):
            if user_choice["value"] is not None:
                break
            print(f"Auto action in {remaining} seconds...", end="\r")
            time.sleep(1)
        
        print() # Clear the line after countdown

        # Decision Logic
        choice = user_choice["value"]
        
        if choice == "S":
            beliefs.close_valve()
            print(f"[ACTION] Valve closed by user (Risk: {risk}).")
        elif choice in ["I", "O"]:
            print(f"[INFO] User opted to keep valve open.")
        else:
            # This covers both the "None" (timeout) and invalid inputs
            print("[TIMEOUT/NO INPUT] Safety protocol triggered.")
            beliefs.close_valve()
            print("[ACTION] Valve closed automatically.")