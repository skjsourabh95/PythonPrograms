# Palindrome No
print "Palindrome Number"
no = int(raw_input("Enter a no to check:"))
rem, val, temp = 0, 0, no
while temp != 0:
    rem = temp % 10
    val = (val * 10) + rem
    temp = temp / 10

if val == no:
    print "%d is a Palindrome No" % no
else:
    print "%d is not a Palindrome No" % no
