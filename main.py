import asyncio
import time

from rich import print

from bot import Bot

class Channel:
    def __init__(self, time_limit = 300):
        self.closed = False
        self.time_limit = time_limit
        self.conversation = ["Narrator: Let the scene begin!"]
        self.start = time.time()


    def get_history(self):
        return self.conversation[-5:]

    def add_message(self, message):
        self.conversation.append(message)
        print(message)
        if time.time() - self.start > self.time_limit:
            self.closed = True

if __name__ == "__main__":  
    from prompts import bots
    bots = [Bot(name, system_prompt) for name, system_prompt in bots.items()]
    channel = Channel()

    # Run all the bots at once
    async def run_bots():
        tasks = [bot.run(channel) for bot in bots]
        await asyncio.gather(*tasks)
            

    asyncio.run(run_bots())