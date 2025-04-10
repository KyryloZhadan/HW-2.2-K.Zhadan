import string

user_input = input("Put letters: ")
first, last = user_input.split("-")
letters = string.ascii_letters
first_index = letters.index(first)
last_index = letters.index(last)
result = letters[first_index:last_index + 1]
print(result)
