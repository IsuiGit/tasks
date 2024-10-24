import time

def isEven(x: int) -> bool:
    print("Определение четности делением на 2")
    return x % 2 == 0

def isEvenBit(x: int) -> bool:
    print("Определение четности числа битовой операцией")
    return x & 1 == 0

def isEvenDis(x: int) -> bool:
    print("Определение четности числа по разряду")
    return bin(x).replace('0b', '')[-1] == '0'

#test 1
start = time.monotonic_ns()
print(isEven(1**100))
finish = time.monotonic_ns()
print(f'Время работы isEven: {finish - start}')
#test 2
start = time.monotonic_ns()
print(isEvenBit(1**100))
finish = time.monotonic_ns()
print(f'Время работы isEvenBit: {finish - start}')
#test 3
start = time.monotonic_ns()
print(isEvenDis(1**100))
finish = time.monotonic_ns()
print(f'Время работы isEvenDis: {finish - start}')
