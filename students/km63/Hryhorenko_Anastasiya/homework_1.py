#task1------------------------------------------------------------
"""
Напишіть програму, яка отримує три числа і друкує їх суму. Кожне число користувач вводить у окремому рядку.

"""
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)
#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Напишіть програму, яка отримує довжини двох катетів прямокутного трикутника та виводить його площу. Користувач вводить довжини катетів у окремих рядках.
"""
b = int(input())
h = int(input())
print(b*h/2)
#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
N студентів отримали K яблук і розподілити їх між собою порівну. Неподілені яблука залишились у кошику. Скільки яблук отримає кожен студент? Скільки яблук залишиться в кошику?
Програма отримує числа N і K. Вона повинна вивести два числа: відповіді на поставлені вище питання.
"""
n = int(input())
k = int(input())
a=print(k // n)
b=print(k % n)
#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
Нехай число N - кількість хвилин, відрахованих після півночі. Скільки годин і хвилин буде показувати цифровий годинник, якщо за відлік взяти 00:00? Програма повинна виводити два числа: кількість годин (від 0 до 23) і кількість хвилин (від 0 до 59). Візьміть до уваги, що починаючи з півночі може пройти декілька днів, тому число N може бути достатньо великим.
"""
a = int(input())
b = a//60
c = a%60
d = b%24
print(d, c)
#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""
Напишіть програму, яка вітає користувача, друкуючи слово "Hello", ім'я користувача і знак оклику після нього. Наприклад “Hello, Mike!”
"""
name = input()
print(("Hello, " + name +"!") )
#-----------------------------------------------------------------


#task6------------------------------------------------------------
"""
Напишіть програму, яка зчитує ціле число і друкує його попереднє і наступне значення за форматом:
The next number for the number 179 is 180.
The previous number for the number 179 is 178.
"""
x = int(input())
print("The next number for the number " + str(x) + " is " + str(x+1))
print("The previous number for the number " + str(x) + " is "+ str(x-1))
#-----------------------------------------------------------------


#task7------------------------------------------------------------
"""
Школа вирішила сформувати три нові групи учнів та надати їм окремі класи. У кожному класі необхідно встановити столи для учнів, у розрахунку, що за одним столом може сидіти не більше двох учнів. Яку мінімальну кількість столів необхідно придбати?

"""
a = int(input())
b = int(input())
c = int(input())
x = a%2+a//2
y = b%2+b//2
z = c%2+c//2
print(x+y+z
#-----------------------------------------------------------------