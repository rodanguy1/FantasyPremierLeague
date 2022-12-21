import os
import pywhatkit


def send_message_to_group(message):
    pywhatkit.sendwhatmsg_to_group_instantly(os.getenv('WHATSAPP_GROUP_ID'), message)
