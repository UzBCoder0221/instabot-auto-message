from instagrapi import Client
from time import sleep
import os
from random import shuffle,choices,randint
from string import ascii_lowercase, ascii_uppercase

def login(username, password):
    cl = Client(proxy="https://45.126.168.81:4145")
    cl.login(username, password)
    return cl

def send_message(cl, recipient_username, message):
    user_id = cl.user_id_from_username(recipient_username)
    cl.direct_send(message, [user_id])
    print(f"Sent message to {recipient_username}")

def generate_lorem():
    num=randint(5,50)
    lsit=list(ascii_lowercase)+list(ascii_uppercase)+list(" "*num)
    shuffle(lsit)
    lorem=choices(lsit,k=num)
    lorem="".join(lorem).strip()
    return lorem


if __name__ == "__main__":
    username = "yuldoshevb_0221"
    recipient_username = "anime._.uz"
    password = os.getenv('PASSWORD')
    print(password)

    try:
        cl = login(username, password)

        while True:
            send_message(cl, recipient_username, f"{generate_lorem()}")
            sleep(1)
    except Exception as e:
        print(f"An error occurred: {e}")
