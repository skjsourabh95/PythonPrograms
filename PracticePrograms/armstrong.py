# Armstrong No
print "Armstrong No"
no = int(raw_input("Enter a no to check:"))
rem, val, temp = 0, 0, no
while temp != 0:
    rem = temp % 10
    val = val + (rem**3)
    temp = temp / 10
if val == no:
    print "%d is a Armstrong No" % no
else:
    print "%d is not a Armstrong No" % no



