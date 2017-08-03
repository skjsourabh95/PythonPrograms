# fibonacci series
a, b = 1, 0
# n = raw_input("Enter the limit:")
while b < 10:
    print b
    a, b = b, a+b

# using for loop
words = ['cat', 'mouse', 'dog']
for w in words:
    print w, len(w)

for w in words[:]:
    if len(w) > 2:
        words.insert(0, w)
        
print words


