import asyncio
from agent import WaterAgent

async def main():
    agent = WaterAgent("admin@localhost", "admin")
    await agent.start()

    print("<=== Water Waste Prevention Agent Running ===>")

    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        print("\nSystem stopped by user.")
        await agent.stop()

if __name__ == "__main__":
    asyncio.run(main())