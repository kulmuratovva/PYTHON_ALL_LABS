import time
import math

n = int(input("Введите число "))
t = int(input("Введите задержку в мс "))

time.sleep(t/1000) #Делим на 1000, потому что функция принимает только секунды
print(math.sqrt(n))