lst = [0, 1, 0, 12, 3] #-> [1, 12, 3, 0, 0]
# lst = [0]# -> [0]
# lst = [1, 0, 13, 0, 0, 0, 5]# -> [1, 13, 5, 0, 0, 0, 0]
# lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]# -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]
not_zero_id = 0
for i in range(len(lst)):
    if lst[i] != 0:
        lst[not_zero_id] = lst[i]
        not_zero_id += 1
while not_zero_id < len(lst):
    lst[not_zero_id] = 0
    not_zero_id += 1
print(lst)
