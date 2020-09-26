from scipy.optimize import linprog
import time

budget = int(input("Введите Ваш бюджет на рекламу:\n")) # 10000 бюджет на рекламу
minuteTV = int(input("Сколько стоит минута рекламы на ТВ?\n")) # 90 д.е. минута рекламы на ТВ
minuteRad = int(input("Сколько стоит минута рекламы на радио?\n")) # 5 д.е. минута рекламы на радио
effectTV = int(input("Во сколько раз реклама на ТВ эффективнее радиорекламы?\n")) # в 30 раз эффективнее, чем второй вид рекламы
effectRadio = int(input("Во сколько раз радиореклама эффективнее рекламы на ТВ?\n")) # в 1 раз эффективнее, чем второй вид рекламы
relationTV = int(input("Во сколько раз будет рекламы на ТВ больше, чем на радио?\n")) # в 3 раз больше одного вида, чем второго
relationRadio = int(input("Во сколько раз будет рекламы на ТВ больше, чем на радио?\n")) # в -1 раз больше одного вида, чем второго

start = time.time()
effect = [-effectTV,-effectRadio] #Функция цели
minuteCost = [[minuteTV,minuteRad]]  #'1'   
budgetVariable = [budget]#'1'   
relation = [[relationTV,relationRadio]] #'2'   
variableCheck = [0] #'2'   
print (linprog(effect, minuteCost, budgetVariable, relation, variableCheck))
stop = time.time()
print ("Время :")
print(stop - start)