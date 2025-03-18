#x = 12345
#print(x % 10, x % 100 // 10, x % 1000 // 100, x % 10000 // 1000, x // 10000)
#y = 37568
#print(y % 10, y % 100 // 10, y % 1000 // 100, y % 10000 // 1000, y // 10000)
number = int(input('Enter:'))
n1 = number % 10
n2 = number % 100 // 10
n3 = number % 1000 // 100
n4 = number % 10000 // 1000
n5 = number // 10000
res_number = n1 * 10000 + n2 * 1000 + n3 * 100 + n4 * 10 + n5
print(res_number)