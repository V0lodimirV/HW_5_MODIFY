def high_2(n):
    # если число n является степенью 2,то просто возвращаем его
    if (not (n & (n - 1))):
        return n
    # иначе установим самый значимый бит)
    return 0x8000000000000000 >> (64 - n.bit_length())
n = int(input('введите значение:\n'))
print(high_2(n))



"""from math import log
n = int(log(int(input('введите число:\n')),2))
print(n)
num = 1
for i in range(n):
    num = num*2
print(num)"""