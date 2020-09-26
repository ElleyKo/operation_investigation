from cvxopt.modeling import variable, op
import time

budget = int(input("Введите Ваш бюджет на рекламу:\n")) # 10000 бюджет на рекламу
minuteTV = int(input("Сколько стоит минута рекламы на ТВ?\n")) # 90 д.е. минута рекламы на ТВ
minuteRad = int(input("Сколько стоит минута рекламы на радио?\n")) # 5 д.е. минута рекламы на радио
effectTV = int(input("Во сколько раз реклама на ТВ эффективнее радиорекламы?\n")) # в 30 раз эффективнее, чем второй вид рекламы
effectRadio = int(input("Во сколько раз радиореклама эффективнее рекламы на ТВ?\n")) # в 1 раз эффективнее, чем второй вид рекламы
relation = int(input("Во сколько раз будет рекламы на ТВ больше, чем на радио?\n")) # в 3 раз больше одного вида, чем второго

start = time.time()
budgetTVAd = variable()
budgetRadioAd = variable()
negativeProfitFunc = -(effectTV * budgetTVAd + effectRadio * budgetRadioAd) #Функция цели
func1 = (minuteTV * budgetTVAd + minuteRad * budgetRadioAd <= budget) #"1"
func2 = (relation * budgetTVAd - budgetRadioAd == 0) # "2"
nonNegativeBudgetTV = (budgetTVAd >= 0) #"3"    
nonNegativeBudgetRadio = (budgetRadioAd >= 0) #"3"    
problem = op(negativeProfitFunc,[func1,func2,nonNegativeBudgetTV,nonNegativeBudgetRadio])
problem.solve(solver='glpk')  
problem.status
print ("Прибыль:")
print(abs(problem.objective.value()[0]))
print ("Результат:")
print(budgetTVAd.value)
print(budgetRadioAd.value)
stop = time.time()
print ("Время :")
print(stop - start)