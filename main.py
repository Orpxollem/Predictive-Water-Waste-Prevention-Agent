from agent import WaterAgent

if __name__ == "__main__":
    agent = WaterAgent()

    print("<=== Autonomous Water Waste Prevention Agent Running ===>")

    try:
        while True:
            agent.run()
    except KeyboardInterrupt:
        print("\nSystem stopped by user.")