lst = [0, 1, 7, 2, 4, 8] #=> (0 + 7 + 4) * 8 = 88
# lst = [1, 3, 5] # => 30
# lst = [6] # => 36
# lst = [] # => 0
if not lst:
    result = 0
else:
    even_numbs = sum(lst[i] for i in range(0, len(lst), 2))
    result = even_numbs * lst[-1]
print(result)