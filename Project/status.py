from colorama import Fore
STATUS_MESSAGES = []
from Global import spy

#function to add a status for a spy

def add_status():
    updated_msg = None
    ch = raw_input(Fore.GREEN+"1.Select from previous status"
                   "\n2.Add a new status"
                   "\nEnter your Choice:")

    if ch == "1":
        if(spy.current_status_message != None):
            item_pos = 1
            print "\nPrevious Status"
            print"................\n"
            for message in STATUS_MESSAGES:
                print str(item_pos) + ". " + message
                item_pos = item_pos + 1
            message_selected = int(raw_input("\nChoose from the above messages:"))
            if len(STATUS_MESSAGES) >= message_selected:
                updated_msg = STATUS_MESSAGES[message_selected - 1]

            else:
                print Fore.RED+"wrong selection"
        else:
            print  Fore.RED+"You don't have any previous status add new status!"

    elif ch == "2":
            new_status = raw_input(Fore.GREEN+"Enter your new status:\n")
            if len(new_status) > 0:
                updated_msg = new_status
            STATUS_MESSAGES.append(updated_msg)


    else:
        print  Fore.RED+"Enter correct option"
    return updated_msg
