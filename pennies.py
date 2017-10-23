a = int(input())
b = int(input())
n = int(input())

pennies = (b * n) % 100
roubles = (a * n) + (b * n) // 100

print(roubles, pennies)
