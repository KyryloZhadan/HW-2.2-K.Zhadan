lst = [0, 1, 7, 2, 4, 8] #=> (0 + 7 + 4) * 8 = 88
# lst = [1, 3, 5] # => 30
# lst = [6] # => 36
# lst = [] # => 0
if not lst:
    result = 0
    print(result)
else:
    s = []
    last_i = lst[-1]
    for n in range(len(lst)):
        if n % 2 == 0:
            s.append(lst[n])
    print(sum(s) * last_i)



