lst = [19, 56, 12, 43, 8, 2, 0, 54, 4, 5, 7, 8, 9, 11, 29]
lst_2 = [77, 1, 11, 29]
lst_3 = [0]
lst_4 = []
# lst = lst_2
# lst = lst_3
# lst = lst_4
if lst == []:
    print([])
else:
    lst_1 = [lst[-1]]
    length = len(lst)
    lst_1.extend(lst[0:length-1])
    print(lst_1)

