from spy_details import spy
from start_chat import start_chat
print "Continue as default user or make a new account:"
if 'name' in spy:
    print "Key present."
    choice = raw_input( "Continue as " + spy['name'] + "\nEnter (Y/N):")
    if choice == "N" or choice == "n":
            print "Enter the Spy Details:"
            spy_name = raw_input("Provide your name:")
            spy_age = 0
            spy_rating = 0.0
            spy_status = False
            if len(spy_name) < 0 and spy_name.isalpha() == True:
                spy_salutation = raw_input("Provide Mr/Ms:")
                if len(spy_salutation) > 0 and (spy_salutation.upper() == "MR" or spy_salutation.upper() == "MS"):
                    spy_name = spy_salutation + "." + spy_name
                    print "Welcome " + spy_name + " Happy to have you "
                    spy_status= True
                    spy_age = int(raw_input("Enter your age"))
                    if spy_age > 18 and spy_age < 50:
                        spy_rating = float(raw_input("Enter your rating"))
                        if spy_rating > 4.7:
                            print "You are awesome"
                        elif spy_rating > 3.5 and spy_rating <= 4.5:
                            print "You are good"
                        elif spy_rating > 2.5 and spy_rating >=3.5:
                            print "You can survive"
                        else:
                            print "Work Hard"
                        print"Authentication complete"
                        print spy_name+"is of %d years and has a rating of %f" %(spy_age,spy_rating)
                    else:
                        print "You are not of age to be a spy"
                else:
                    print "Enter you salutation"
            else:
                print "Enter your name correctly"
            option = raw_input("Do you want to go offline?(Y/N):")
            if option == "Y":
                spy_status = False
                print"You are offline"
            else:
                print"Keep working!"
    elif choice == "Y" or choice == "y":
        start_chat()
        print"Enter correct value (Y/N)"
else:
    print "Key does not exist."


