# Calculator
print "Calculator"
a = int(raw_input("Enter first no:"))
b = int(raw_input("Enter second no:"))
print "1 for Addition"
print "2 for Subtraction"
print "3 for Division"
print "4 for Multiplication"
c = raw_input("Enter your Choice:")
if c == "1":
    print "Sum is:" + str(a+b)
elif c == 2:
    print "Difference is:" + str(a-b)
elif c == 3:
    print "Division is:" + str(a/b)
elif c == 4:
    print "Multiplication is:" + str(a*b)
else:
    print "Wrong Selection"

