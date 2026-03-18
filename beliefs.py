class Beliefs:
    def __init__(self):
        self.valve_open = True

    def close_valve(self):
        self.valve_open = False

    def open_valve(self):
        self.valve_open = True

    def is_valve_open(self):
        return self.valve_open