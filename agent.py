from environment import Environment
from beliefs import Beliefs
from decision_engine import DecisionEngine
from actions import Actions


class WaterAgent:
    def __init__(self):
        self.env = Environment()
        self.beliefs = Beliefs()
        self.decision_engine = DecisionEngine()
        self.actions = Actions()

    def run(self):
        percepts = self.env.get_percepts()
        risk = self.decision_engine.evaluate(percepts)
        print(f"[DECISION] Risk Level: {risk}")
        self.actions.handle(risk, self.beliefs)