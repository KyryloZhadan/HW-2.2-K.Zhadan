
import string
import keyword
# print(keyword.kwlist)

name = input(str('Enter your name:'))

valid_numeric = False
valid_lower = False
valid_punctuation = False
valid_banned = False
valid_space = ' ' not in name

if name[0].isnumeric():
    valid_numeric = False
else:
    valid_numeric = True

if not name == name.lower():
    valid_lower = False
else:
    valid_lower = True

for n in name:
    if n in string.punctuation and n != '_':
        valid_punctuation = False
        break
    else:
        valid_punctuation = True
if name in keyword.kwlist:
    valid_banned = False
else:
    valid_banned = True
print(valid_numeric and valid_lower and valid_punctuation and valid_banned and valid_space)



# print(string.punctuation)