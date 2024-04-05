BASE = 16
number = int(input('Введите число: '))
print(hex(number))
result = ''
d = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

while number > BASE:
    sym = number % BASE
    if sym > 9:
       sym = d[sym]
    result += str(sym)
    number //= BASE
result += str(number)

print(result[::-1])
