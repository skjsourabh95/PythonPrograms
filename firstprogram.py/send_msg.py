from add_friend import select_friend, friends
from steganography.steganography import Steganography
from datetime import datetime


def send_message():

    friend_choice = select_friend()
    original_image = raw_input("What is the name of the image?")
    output_image = raw_input("What is the name of the output image?")
    text = raw_input("What is your message?")
    Steganography.encode(original_image, output_image, text)
    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True
    }

    friends[friend_choice]['chats'].append(new_chat)
    print "Your secret message is ready!"
