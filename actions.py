import time
import threading
import sys

class Actions:
    def handle(self, risk, beliefs):
        # 1. State Check: If valve is closed, must reopen before checking new flow
        if not beliefs.is_valve_open():
            # Clear any trailing characters from previous lines
            print("\r" + " " * 60, end="\r") 
            print("[SYSTEM] Valve is CLOSED.")
            choice = input("Press R to reopen valve: ").strip().upper()
            if choice == "R":
                beliefs.open_valve()
                print("[ACTION] Valve reopened.")
            return

        # 2. Logic for Low Risk
        if risk == "LOW":
            print("[LOG] Normal usage.")
            return

        # 3. Logic for Medium/High Risk with Countdown
        print(f"\n[{'ALERT' if risk == 'HIGH' else 'WARNING'}] Potential waste detected!")
        prompt = "S: Shut Valve | O: Open (Ignore)" if risk == "HIGH" else "S: Shut | I: Ignore"
        print(prompt)
        
        user_choice = {"value": None}
        stop_event = threading.Event()

        def get_input():
            try:
                # sys.stdin.readline is more thread-safe for simulations
                line = sys.stdin.readline().strip().upper()
                user_choice["value"] = line
                stop_event.set()
            except EOFError:
                pass

        input_thread = threading.Thread(target=get_input, daemon=True)
        input_thread.start()

        # 15-second countdown loop [as per your requirement]
        for remaining in range(15, 0, -1):
            if stop_event.is_set():
                break
            # Overwrite the same line using \r to prevent the "flicker"
            print(f"/Auto-action in {remaining:2d} seconds... ", end="\r", flush=True)
            time.sleep(1)
        
        # Clear the countdown line before printing the result
        print("\r" + " " * 60, end="\r")

        # Final decision based on input or timeout
        choice = user_choice["value"]
        if choice == "S":
            beliefs.close_valve()
            print(f"[ACTION] Valve closed by user.")
        elif choice in ["O", "I"]:
            print(f"[INFO] User acknowledged and kept valve open.")
        else:
            # Autonomous safety action [Implementation requirement]
            beliefs.close_valve()
            print("[TIMEOUT] No response. Valve closed automatically for safety.")