import datetime, sys
from functools import lru_cache

# @lru_cache
# def fibonacci(n):
#     if n in (0, 1):
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)





# if __name__ == '__main__':
#     qty = 1000

#     t1 = datetime.datetime.now()
#     list_fib = [fibonacci(i) for i in range(qty)]
#     t2 = datetime.datetime.now()
#     dt_list = t2 - t1


#     t1 = datetime.datetime.now()
#     gen_fib = (fibonacci(i) for i in range(qty))
#     t2 = datetime.datetime.now()
#     dt_gen = t2 - t1
#     print(list_fib, 'list_fib')
#     print(gen_fib, 'gen_fib')
#     print(sys.getsizeof(list_fib), 'list_memory') # 8856 list_memory
#     print(sys.getsizeof(gen_fib), 'gen_memory') # 112 gen_memory было одинакова всегда
#     print(dt_list, 'list time') #0:00:00.001001 list time
#     print(dt_gen, 'gen time') #0:00:00 gen time так же с временем

# Генератор не хранит элементы и последовательности в явном виде, а лишь 
# закономерность по которой рассчитывается следующий элемент
# 
# Недостатки:
# 
# 1) Напрямую по индексу мы не можем обратиться к генератору
# 2) Не можем получить длину
# 3) Генератор позволяет пролистать себя только один раз
# Единственное что можем это узнать следующий элемент next(gen_fibo)
# 
#        


@lru_cache
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a # шаг выполняется и останавливается тут
        a, b = b, a + b
        print('Я тут')


qty = 10
t1 = datetime.datetime.now()
g = fibonacci(qty)
t2 = datetime.datetime.now()
gen_time = t2 - t1
gen_mem = sys.getsizeof(g) 
print(next(g))                         
print(next(g))  
print(next(g))   
print(next(g))            
print(gen_mem ,gen_time)

# 0
# Я тут
# 1
# 112 0:00:00

for i in g:
    print(i)