# def of chat function
def start_chat(spy_name, spy_age, spy_rating):
    show_menu = True
    while show_menu:
        menu()
        choice = raw_input("Enter your choice:")
        if choice == "1":
            current_status = None
            new_status = add_status(current_status)
        elif choice == "2":
            print "2"
        elif choice == "3":
            print "3"
        elif choice == "4":
            show_menu = False
        else:
            print "Enter correct value"


def add_status(current_status):
    ch=raw_input("1.Select from previous status or 2. Add a new status:")
    if ch=="1":
        pass
    else:
        new_status= raw_input("Enter your new status:")
    return new_status


def menu():
    print "Menu"
    print "1."
    print "2."
    print "3."
    print "4."

