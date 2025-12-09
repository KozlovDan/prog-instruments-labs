import os
import sys
import math
import random
import tkinter as tk
from tkinter import messagebox, simpledialog
import datetime

#глобальные_переменные_в_нижнем_регистре_но_это_глобалы_так_что_всё_равно_плохо
current_user = "guest"
app_mode = "console"
DEBUG_MODE = True
MAX_HISTORY_SIZE = 100
history_log = []
RESULT_PRECISION = 5

def PRINT(msg):
 print(str(msg))

def GET_USER_INPUT(prompt):
 if app_mode == "gui":
  return simpledialog.askstring("Ввод", prompt)
 else:
  return input(prompt)

def LOG_ACTION(action):
 global history_log
 history_log.append(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {action}")
 if len(history_log) > MAX_HISTORY_SIZE:
  history_log.pop(0)

def CLEAR_HISTORY():
 global history_log
 history_log = []
 PRINT("История очищена")

def SHOW_HISTORY():
 for i,entry in enumerate(history_log):
  PRINT(f"{i+1}: {entry}")

def calculate_sum(a,b):
 return a+b
def calculate_difference(a,b):
 return a-b
def calculate_product(a,b):
 return a*b
def calculate_division(a,b):
 if b == 0:
  raise Exception("Деление на ноль!")
 return a/b
def calculate_power(base,exp):
 return base**exp
def calculate_sqrt(x):
 if x<0:
  raise Exception("Нельзя извлечь корень из отрицательного числа")
 return math.sqrt(x)
def calculate_sin(x):
 return math.sin(x)
def calculate_cos(x):
 return math.cos(x)
def calculate_tan(x):
 return math.tan(x)
def calculate_log(x,base=math.e):
 if x<=0:
  raise Exception("Логарифм определён только для положительных чисел")
 if base<=0 or base==1:
  raise Exception("Основание логарифма должно быть >0 и !=1")
 return math.log(x,base)
def calculate_factorial(n):
 if n<0 or n!=int(n):
  raise Exception("Факториал определён только для неотрицательных целых чисел")
 return math.factorial(int(n))
def generate_random_number(min_val=0,max_val=100):
 return random.randint(min_val,max_val)

class SUPER_MATH_TOOL_GUI:
 def __init__(self,root):
  self.root = root
  self.root.title("Супер Математический Инструмент v1.0")
  self.root.geometry("500x600")
  self.expression = ""
  self.setup_ui()

 def setup_ui(self):
  self.display = tk.Entry(self.root,font=("Arial",16),justify="right",state="readonly",textvariable=tk.StringVar())
  self.display.grid(row=0,column=0,columnspan=4,sticky="ew",padx=5,pady=5)
  buttons = [
   ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
   ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
   ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
   ('0',4,0),('.',4,1),('=',4,2),('+',4,3),
   ('C',5,0),('√',5,1),('^',5,2),('!',5,3),
   ('sin',6,0),('cos',6,1),('tan',6,2),('log',6,3),
   ('rand',7,0),('hist',7,1),('clear_hist',7,2),('quit',7,3)
  ]
  for (text,row,col) in buttons:
   tk.Button(self.root,text=text,width=8,height=2,command=lambda t=text:self.on_button_click(t)).grid(row=row+1,column=col,padx=2,pady=2)
  self.root.grid_columnconfigure((0,1,2,3),weight=1)


 def on_button_click(self,btn):
  try:
   if btn == '=':
    result = eval(self.expression)
    self.display.config(text=str(round(result,RESULT_PRECISION)))
    LOG_ACTION(f"Вычислено: {self.expression} = {result}")
    self.expression = str(result)
   elif btn == 'C':
    self.expression = ""
    self.display.config(text="")
   elif btn == '√':
    if self.expression:
     val = float(self.expression)
     res = calculate_sqrt(val)
     self.display.config(text=str(round(res,RESULT_PRECISION)))
     LOG_ACTION(f"Корень: √{val} = {res}")
     self.expression = str(res)
   elif btn == '^':
    self.expression += '**'
    self.display.config(text=self.expression)
   elif btn == '!':
    if self.expression:
     val = float(self.expression)
     res = calculate_factorial(val)
     self.display.config(text=str(res))
     LOG_ACTION(f"Факториал: {val}! = {res}")
     self.expression = str(res)
   elif btn == 'sin':
    if self.expression:
     val = float(self.expression)
     res = calculate_sin(val)
     self.display.config(text=str(round(res,RESULT_PRECISION)))
     LOG_ACTION(f"sin({val}) = {res}")
     self.expression = str(res)
   elif btn == 'cos':
    if self.expression:
     val = float(self.expression)
     res = calculate_cos(val)
     self.display.config(text=str(round(res,RESULT_PRECISION)))
     LOG_ACTION(f"cos({val}) = {res}")
     self.expression = str(res)
   elif btn == 'tan':
    if self.expression:
     val = float(self.expression)
     res = calculate_tan(val)
     self.display.config(text=str(round(res,RESULT_PRECISION)))
     LOG_ACTION(f"tan({val}) = {res}")
     self.expression = str(res)
   elif btn == 'log':
    if self.expression:
     val = float(self.expression)
     res = calculate_log(val)
     self.display.config(text=str(round(res,RESULT_PRECISION)))
     LOG_ACTION(f"ln({val}) = {res}")
     self.expression = str(res)
   elif btn == 'rand':
    res = generate_random_number()
    self.display.config(text=str(res))
    LOG_ACTION(f"Случайное число: {res}")
    self.expression = str(res)
   elif btn == 'hist':
    SHOW_HISTORY()
   elif btn == 'clear_hist':
    CLEAR_HISTORY()
   elif btn == 'quit':
    self.root.destroy()
   else:
    self.expression += btn
    self.display.config(text=self.expression)
  except Exception as e:
   messagebox.showerror("Ошибка",str(e))
   self.expression = ""
   self.display.config(text="")


def RUN_CONSOLE_MODE():
 global app_mode
 app_mode = "console"
 PRINT("=== Супер Математический Инструмент (Консоль) ===")
 while True:
  PRINT("\nДоступные команды:")
  PRINT("1. sum a b")
  PRINT("2. diff a b")
  PRINT("3. prod a b")
  PRINT("4. div a b")
  PRINT("5. pow base exp")
  PRINT("6. sqrt x")
  PRINT("7. sin x")
  PRINT("8. cos x")
  PRINT("9. tan x")
  PRINT("10. log x [base]")
  PRINT("11. fact n")
  PRINT("12. rand [min max]")
  PRINT("13. history")
  PRINT("14. clear_hist")
  PRINT("15. quit")
  try:
   cmd = GET_USER_INPUT("Введите команду: ").strip().split()
   if not cmd: continue
   action = cmd[0]
   if action=="quit" or action=="15":
    break
   elif action in ("1","sum"):
    a,b=float(cmd[1]),float(cmd[2])
    res=calculate_sum(a,b)
    PRINT(f"Результат: {res}")
    LOG_ACTION(f"sum({a},{b}) = {res}")
   elif action in ("2","diff"):
    a,b=float(cmd[1]),float(cmd[2])
    res=calculate_difference(a,b)
    PRINT(f"Результат: {res}")
    LOG_ACTION(f"diff({a},{b}) = {res}")
   elif action in ("3","prod"):
    a,b=float(cmd[1]),float(cmd[2])
    res=calculate_product(a,b)
    PRINT(f"Результат: {res}")
    LOG_ACTION(f"prod({a},{b}) = {res}")
   elif action in ("4","div"):
    a,b=float(cmd[1]),float(cmd[2])
    res=calculate_division(a,b)
    PRINT(f"Результат: {res}")
    LOG_ACTION(f"div({a},{b}) = {res}")
   elif action in ("5","pow"):
    base,exp=float(cmd[1]),float(cmd[2])
    res=calculate_power(base,exp)
    PRINT(f"Результат: {res}")
    LOG_ACTION(f"pow({base},{exp}) = {res}")
   elif action in ("6","sqrt"):
    x=float(cmd[1])
    res=calculate_sqrt(x)
    PRINT(f"Результат: {res}")
    LOG_ACTION(f"sqrt({x}) = {res}")
   elif action in ("7","sin"):
    x=float(cmd[1])
    res=calculate_sin(x)
    PRINT(f"Результат: {round(res,RESULT_PRECISION)}")
    LOG_ACTION(f"sin({x}) = {res}")
   elif action in ("8","cos"):
    x=float(cmd[1])
    res=calculate_cos(x)
    PRINT(f"Результат: {round(res,RESULT_PRECISION)}")
    LOG_ACTION(f"cos({x}) = {res}")
   elif action in ("9","tan"):
    x=float(cmd[1])
    res=calculate_tan(x)
    PRINT(f"Результат: {round(res,RESULT_PRECISION)}")
    LOG_ACTION(f"tan({x}) = {res}")
   elif action in ("10","log"):
    x=float(cmd[1])
    base=float(cmd[2]) if len(cmd)>2 else math.e
    res=calculate_log(x,base)
    PRINT(f"Результат: {round(res,RESULT_PRECISION)}")
    LOG_ACTION(f"log({x}, {base}) = {res}")
   elif action in ("11","fact"):
    n=float(cmd[1])
    res=calculate_factorial(n)
    PRINT(f"Результат: {res}")
    LOG_ACTION(f"fact({n}) = {res}")
   elif action in ("12","rand"):
    if len(cmd)>2:
     mn,mx=int(cmd[1]),int(cmd[2])
     res=generate_random_number(mn,mx)
    else:
     res=generate_random_number()
    PRINT(f"Результат: {res}")
    LOG_ACTION(f"rand({cmd[1] if len(cmd)>1 else '0,100'}) = {res}")
   elif action in ("13","history"):
    SHOW_HISTORY()
   elif action in ("14","clear_hist"):
    CLEAR_HISTORY()
   else:
    PRINT("Неизвестная команда")
  except IndexError:
   PRINT("Недостаточно аргументов")
  except ValueError:
   PRINT("Некорректное число")
  except Exception as e:
   PRINT(f"Ошибка: {e}")


def MAIN():
 global current_user
 PRINT("Добро пожаловать в Супер Математический Инструмент!")
 if len(sys.argv)>1 and sys.argv[1]=="gui":
  global app_mode
  app_mode = "gui"
  root = tk.Tk()
  app = SUPER_MATH_TOOL_GUI(root)
  LOG_ACTION("Запуск GUI-режима")
  root.mainloop()
 else:
  name = GET_USER_INPUT("Введите имя (или нажмите Enter для 'guest'): ")
  if name: current_user = name
  LOG_ACTION(f"Пользователь вошёл как: {current_user}")
  RUN_CONSOLE_MODE()
 LOG_ACTION("Выход из приложения")
        
        
# Точка входа
if __name__ == "__main__":
 MAIN()