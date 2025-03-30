import string

str1 = input(str('Enter your hashtag:'))
no_punct = ''.join(n for n in str1 if n not in string.punctuation)
bywords = no_punct.split()
hashtag = '#' + ''.join(word.capitalize() for word in bywords)

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)