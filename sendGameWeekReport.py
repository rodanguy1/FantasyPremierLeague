import asyncio

from weeklyH2H.matchDataExtractor import weekly_h2h
from whatsapp.messagesSender import send_message_to_group

if __name__ == '__main__':
    message = asyncio.run(weekly_h2h())
    print(message)
    # send_message_to_group(message)
