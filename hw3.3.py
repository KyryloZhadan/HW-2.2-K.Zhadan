lst = [1, 2, 3, 4, 5, 6] #=> [[1, 2, 3], [4, 5, 6]]
# lst = [1, 2, 3]# => [[1, 2], [3]]
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] #=> [[1, 2, 3], [4, 5]]
# lst = [1] #=> [[1], []]
# lst = [] #=> [[], []]
length = len(lst)
if not length % 2 == 0:
    mid = int(length / 2 + 1)
else:
    mid = int(length / 2)
lst_separated = [lst[0:mid], lst[mid:length]]
print(lst_separated)


