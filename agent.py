from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
import asyncio

from environment import Environment
from beliefs import Beliefs
from decision_engine import DecisionEngine
from actions import Actions


class WaterAgent(Agent):

    async def setup(self):
        print("[SETUP] Agent starting...")

        self.env = Environment()
        self.beliefs = Beliefs()
        self.decision_engine = DecisionEngine()
        self.actions = Actions()

        self.add_behaviour(self.MainBehaviour())

    class MainBehaviour(CyclicBehaviour):
        async def run(self):
            percepts = self.agent.env.get_percepts()
            print("\n[PERCEPTS]", percepts)

            risk = self.agent.decision_engine.evaluate(percepts)
            print("[DECISION] Risk:", risk)

            await self.agent.actions.handle(risk, self.agent.beliefs)

            await asyncio.sleep(3)