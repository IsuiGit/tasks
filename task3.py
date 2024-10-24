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
