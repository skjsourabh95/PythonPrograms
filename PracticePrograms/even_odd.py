# to check weather the no is even or odd
def even_odd(num):
    answer = None
    if num % 2 == 0:
        answer = "EVEN NO"
    else:
        answer = "ODD NO"
    return answer
no = input("Enter a number to check:")
output = even_odd(no)
print("%d is a "+output) % no

