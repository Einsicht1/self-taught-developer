import time

li = [x for x in range(0,1000000)]

li_start = time.time()
print(999999 in li)
li_end = time.time()
print(li_end - li_start)



li = set([x for x in range(0,1000000)])
s_start = time.time()
print(999999 in li)
s_end = time.time()
print(s_end - s_start)
