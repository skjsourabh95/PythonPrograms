from colorama import Fore
from steganography.steganography import Steganography
from friend import select_a_friend
from Global import friends
from datetime import datetime
import re

# a class to store messages send and received
class ChatMessage:

  def __init__(self, message, sent_by_me,no_of_words):
    self.message = message
    self.time = datetime.now()
    self.sent_by_me = sent_by_me
    self.no_of_words=no_of_words

# method to send a message
def send_a_message():
    friend_choice = select_a_friend()
    original_image = raw_input(Fore.MAGENTA+"What is the name of the image?:\n")

    #pattern to check the jpg extension of the image
    pattern = '^[a-zA-Z]+\.jpg$'

    if re.match(pattern, original_image) != None:
       output_image = raw_input(Fore.MAGENTA+"What is the name of the output image?:\n")
       text = raw_input(Fore.MAGENTA+"What is your Secret message?:\n")
       if text:
           Steganography.encode(original_image, output_image, text)

           #counting the no of words in the message
           count=word_count(text)
           new_chat = ChatMessage(text,True,count)
           friends[friend_choice].chats.append(new_chat)

           #removing spy with a msg 100 words long
           if count > 100:
               del friends[friend_choice]
               print Fore.RED + "You have been removed for sending long messages!"
           else:
               print Fore.MAGENTA+"Your secret message was sent!"
       else:
           print Fore.RED+"Enter the secret text to send!"

    else:
       print Fore.RED+"Invalid image name try .jpg images only."

#mfunction to store messages and read them
def read_a_message():
    sender = select_a_friend()
    output_path = raw_input(Fore.MAGENTA+"What is the name of the file?:\n")
    secret_text = Steganography.decode(output_path)
    count=word_count(secret_text)
    new_chat = ChatMessage(secret_text,False,count)
    friends[sender].chats.append(new_chat)

    #sending message when secret text contatins SOS and Save Me
    if emergency(secret_text):
        print Fore.RED+"Help has been dispatched to your location!"
    else:
        print Fore.MAGENTA+"Your secret message has been saved!"

#function to count words
def word_count(string):
    while True:
        count = len(re.findall("[a-zA-Z_]+", string))
        return count

#function to get sos and save me
def emergency(string):
    word_list = re.findall(r"[\w']+", string)
    for word in word_list:
        if word == "SOS" or word == "sos" or word == "SAVE" or word == "save":
            return True
    return False
