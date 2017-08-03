print "Enter the Spy Details:"
spy_name = raw_input("Provide your name:")

if len(spy_name) == 0:
    spy_salutation = raw_input("Provide Mr/Ms:")

    if len(spy_salutation) == 0:

        spy_name = spy_salutation + "." + spy_name
        print "Welcome " + spy_name + " Happy to have you back"

    else:
        print "Enter you salutation"

else:
    print "Enter your name"

