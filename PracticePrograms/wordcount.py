import re
string = raw_input("Enter String:")
word_list = re.findall(r"[\w']+", string)
print {word for word in word_list}