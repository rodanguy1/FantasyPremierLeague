import asyncio
from time import sleep

from weeklyH2H.cleanMatch import weekly_h2h
from whatsapp.messagesSender import send_message_to_group

if __name__ == '__main__':
    message = asyncio.run(weekly_h2h())
    print(message)
    sleep(10)
    send_message_to_group(message)
