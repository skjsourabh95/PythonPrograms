# def of chat function
def start_chat(spy_name, spy_age, spy_rating):
    show_menu = True
    while show_menu:
        menu()
        choice = raw_input("Enter your choice:")
        if choice == "1":
            current_status = add_status()
            print "Your new status is"+current_status
        elif choice == "2":
            print "2"
        elif choice == "3":
            print "3"
        elif choice == "4":
            show_menu = False
        else:
            print "Enter correct value"

STATUS_MESSAGES = ['My name is Sourabh, James Bond is my hero', 'Shaken, not stirred.']


def add_status():
    updated_msg = None
    ch = raw_input("1.Select from previous status \n 2. Add a new status:")

    if ch == "1":
        item_pos = 1
        for message in STATUS_MESSAGES:
            print item_pos + ". " + message
            item_pos = item_pos + 1
            message_selected = int(raw_input("\nChoose from the above messages "))
            if len(STATUS_MESSAGES) >= message_selected:
                updated_msg = STATUS_MESSAGES[message_selected - 1]

    else:
            new_status = raw_input("Enter your new status:")
            if len(new_status) > 0:
                updated_msg = new_status
            STATUS_MESSAGES.append(updated_msg)
    return updated_msg


def menu():
    print "Menu"
    print "1.Add Status."
    print "2."
    print "3."
    print "4."

