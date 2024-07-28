#FizzBuzz. Задачка с собеседования
#1Создайте файл 
#lesson_2_task_4.py

#Напишите функцию fizz_buzz, которая принимает один аргумент — n (число).
#Функция должна печатать числа от 1 до n. При этом:
#если число делится на 3, печатать Fizz;
#если число делится на 5, печатать Buzz;
#если число делится на 3 и на 5, печатать FizzBuzz.

n = int (input())
def Fizz_Buzz (n):
    for n in range (1 , n+1):
        if (n % 3 == 0) and (n % 5 == 0):
            print ("FizzBuzz")
        elif n % 5 == 0:
            print ('Buzz')
        elif n % 3 == 0:
            print ('Fizz')
        else:
            print (n)
Fizz_Buzz (n)
