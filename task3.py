"""
Быстрая сортировка Хоара
"""
import statistics, random, time

def quicksortMedian(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = statistics.median(nums)
   l_nums = [n for n in nums if n < q]
   e_nums = [q] * nums.count(q)
   b_nums = [n for n in nums if n > q]
   return quicksortMedian(l_nums) + e_nums + quicksortMedian(b_nums)

def quicksortRnd(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
   l_nums = [n for n in nums if n < q]
   e_nums = [q] * nums.count(q)
   b_nums = [n for n in nums if n > q]
   return quicksortMedian(l_nums) + e_nums + quicksortMedian(b_nums)

"""
Методология быстрой сортировки Хоара

Для наибыстрой реализации быстрой сортировки, опорный элемент сортировки должен быть медиальным
На практике, может случится так, что выбранный элемент является наименьшим или наибольшим, что превратит ассимптотику срабатывания сортировки
в O(n**2). Для избежания подобных случаев, опорным элементом будет выбираться тот, что вычислится по median() библиотеки statistics. Для ускорения
можно оставить выбор случайным, и в наборе тестов, среднее время будет +- одинаковым в 2 случаях, однако, для стабилизации реализации, я решил
сразу искать медиану. Оставлю 2 реализации для сравнения скорости
"""

#SpeedTest
m = [random.randint(0, 100000) for i in range(100000)]

start = time.process_time()
quicksortMedian(m)
finish = time.process_time()
print(f"quicksortMedian time: {finish-start}")
start = time.process_time()
quicksortRnd(m)
finish = time.process_time()
print(f"quicksortRnd time: {finish-start}")
