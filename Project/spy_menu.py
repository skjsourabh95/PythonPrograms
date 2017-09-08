from status import add_status
from colorama import init
from friend import add_friend,read_chat
from message import send_a_message,read_a_message
init()
from colorama import Fore
from Global import spy

#user defined menu displaying available options

def show_menu():
    menu = True
    while menu:
        display()
        choice = raw_input(Fore.LIGHTBLACK_EX+"Enter your choice:")
        if choice == "1":
                 current_status =spy.current_status_message
                 print Fore.LIGHTBLACK_EX+"Your current status is " + str(current_status)
                 spy.current_status_message = add_status()
                 if(spy.current_status_message != None):
                  print Fore.LIGHTBLACK_EX+"Your new status is " + str(spy.current_status_message)
        elif choice == "2":
            no = add_friend()
            print Fore.YELLOW+"You have " + str(no) + " friends now!"
        elif choice == "3":
            send_a_message()
        elif choice == "4":
            read_a_message()
        elif choice == "5":
            read_chat()
        elif choice == "6":
            menu = False
        else:
            print Fore.RED+"Enter correct value"


def display():
    print Fore.BLACK+"Menu"
    print "1.Add a status update"
    print "2.Add a friend"
    print "3.Send a secret message"
    print "4.Read a secret message"
    print "5.Read chats from a user"
    print "6.Close Application"