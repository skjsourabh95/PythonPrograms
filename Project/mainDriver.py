# main point of execution

from spy_menu import show_menu
import re
from colorama import init
init()
from colorama import Fore
from Global import spy


print Fore.MAGENTA+"WELCOME TO SPYCHAT 1.0"
choice = raw_input("1.Continue as default user\n2.Make a new account\nEnter your choice:")

#function to get new spy
def spydetails():
    global spy_status
    print (Fore.GREEN+"Enter the New Spy Details:\n")
    spy_name = raw_input("Provide your name:\n")

    #pattern to match only alphabets
    pattern = '^[a-zA-Z\s]+$'
    if (re.match(pattern, spy_name) != None):
       if len(spy_name) > 0 and spy_name.isalpha() == True:
        spy_salutation = raw_input("Provide your salutation(Mr/Ms):\n")

        if len(spy_salutation) > 0 and (spy_salutation.upper() == "MR" or spy_salutation.upper() == "MS"):
            spy_name = spy_salutation + "." + spy_name
            spy_status = True
            spy_age = int(raw_input("Enter your age:\n"))
            pattern = '^[0-9]+$'
            if (re.match(pattern, str(spy_age)) != None):
                if spy_age > 12 and spy_age < 50:
                    spy_rating = float(raw_input("Enter your rating:\n"))
                    pattern = '^[0-9]+\.[0-9]+$'
                    if (re.match(pattern, str(spy_rating)) != None):
                        rating=spy_rating

                        if rating > 4.7:
                            print Fore.BLUE+"(Excellent)"
                        elif rating > 3.5 and rating <= 4.5:
                            print "(Good)"
                        elif rating > 2.5 and rating >= 3.5:
                            print "(Average)"
                        else:
                            print "(Poor)"
                        print Fore.YELLOW+"Welcome " + spy_name + "\nhappy to have you! "
                        print spy_name + " is of %d years and has a rating of %f" % (spy_age, spy_rating)
                        spy.setSpy(spy_name,spy_salutation,spy_age,spy_rating,spy_status)
                        option = raw_input("Do you want to go offline?(Y/N):")
                        if (option == "Y" ):
                            spy_status = False
                            print Fore.RED+"You are offline"
                        else:
                            show_menu()
                    else:
                        print Fore.RED+"Invalid rating. Try floating only."
                else:
                    print Fore.RED+"You are not of the age to be a spy"
                    exit()

        else:
            print Fore.RED+"Salutation Incorrect"
            exit()

    else:
        print Fore.RED+"Enter your name correctly"
        exit()

if choice == "1":
    #working with default values of a spy
    spy_name = spy.getName()
    spy_salutation = spy.getSalutation()
    spy_age = spy.getage()
    spy_rating = spy.getrating()
    rating = spy_rating
    spy_status = spy.getstatus()
    spy_name = spy_salutation + "." + spy_name
    print Fore.YELLOW+"Welcome " + spy_name + "\nhappy to have you "
    print spy_name + " is of %d years and has a rating of %f" % (spy_age, spy_rating)
    option = raw_input("Do you want to go offline?(Y/N):")
    if option == "Y" or option == "y":
        spy_status = False
        print Fore.RED+"You are offline"
    elif option == "N" or option == "n":
        show_menu()
    else:
        print Fore.RED+"Enter Correctly(Y/N):"
elif choice == "2":
    spydetails()
else:
     print Fore.RED+"Enter correct value (Y/N)"
     exit()

