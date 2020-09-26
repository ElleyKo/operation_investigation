from pulp import *
import time

budget = int(input("Введите Ваш бюджет на рекламу:\n")) # 10000 бюджет на рекламу
minuteTV = int(input("Сколько стоит минута рекламы на ТВ?\n")) # 90 д.е. минута рекламы на ТВ
minuteRad = int(input("Сколько стоит минута рекламы на радио?\n")) # 5 д.е. минута рекламы на радио
effect = int(input("Во сколько раз реклама на ТВ эффективнее радиорекламы?\n")) # в 30 раз эффективнее, чем второй вид рекламы
relation = int(input("Во сколько раз будет рекламы на ТВ больше, чем на радио?\n")) # в 3 раз больше одного вида, чем второго

start = time.time()
budgetTVAd = pulp.LpVariable("budgetTVAd", lowBound=0)
budgetRadioAd = pulp.LpVariable("budgetRadioAd", lowBound=0)
problem = pulp.LpProblem('0',pulp.LpMaximize)
problem += effect * budgetTVAd + budgetRadioAd, "Функция цели"
problem += minuteTV * budgetTVAd + minuteRad * budgetRadioAd <= budget, "1"
problem += budgetRadioAd == 3 * budgetTVAd, "2"

problem.solve()
print ("Результат:")
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)
print ("Прибыль:")
print (value(problem.objective))
stop = time.time()
print ("Время :")
print(stop - start)