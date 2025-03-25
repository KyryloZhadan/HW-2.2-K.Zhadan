# [1, 2, 3, 4, 5, 6, 7, 9] #== [1, 3, 7]
# [1, 1, 2, 1]# == [1, 2, 2]
# lst = [6, 3, 7]# == [6, 7, 3]
import random
lst = [random.randint(1, 100) for i in range(random.randint(3, 11))]
print(lst)
fe = lst[0]
te = lst[2]
last = lst[-2]
result = [fe, te, last]
print(result)