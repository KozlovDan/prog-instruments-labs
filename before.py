import tkinter as tk
from tkinter import messagebox
import math
import unittest

#глобальные переменные
result = 0
last_op = ""
memory = 0

def ADD(x,y):
 return x+y
def SUBTRACT(x,y):
 return x-y
def MULTIPLY(x,y):
 return x*y
def DIVIDE(x,y):
 if y==0:
  raise ValueError("деление на ноль")
 return x/y
def POWER(x,y):
 return x**y
def SQRT(x):
 if x<0:
  raise ValueError("корень из отрицательного")
 return math.sqrt(x)

class CALCULATOR_APP:
 def __init__(self,root):
  self.root=root
  self.root.title("калькулятор")
  self.expression = ""
  self.input_text = tk.StringVar()
  self.create_widgets()

 def create_widgets(self):
  input_frame = tk.Frame(self.root,width=400,height=50,bd=0,highlightbackground="black",highlightcolor="black",highlightthickness=1)
  input_rect=tk.Entry(input_frame,font=('arial',18,'bold'),textvariable=self.input_text,width=50,bg="#eee",bd=0,justify=tk.RIGHT)
  input_rect.grid(row=0,column=0)
  input_rect.pack(ipady=10)
  input_frame.pack(pady=20)

  btns_frame=tk.Frame(self.root,width=400,height=400,bg="grey")
  btns_frame.pack()
  tk.Button(btns_frame,text="C",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=self.clear).grid(row=0,column=0,padx=1,pady=1)
  tk.Button(btns_frame,text="M+",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=self.mem_plus).grid(row=0,column=1,padx=1,pady=1)
  tk.Button(btns_frame,text="M-",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=self.mem_minus).grid(row=0,column=2,padx=1,pady=1)
  tk.Button(btns_frame,text="/",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:self.btn_click("/")).grid(row=0,column=3,padx=1,pady=1)

  tk.Button(btns_frame,text="7",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:self.btn_click("7")).grid(row=1,column=0,padx=1,pady=1)
  tk.Button(btns_frame,text="8",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:self.btn_click("8")).grid(row=1,column=1,padx=1,pady=1)
  tk.Button(btns_frame,text="9",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:self.btn_click("9")).grid(row=1,column=2,padx=1,pady=1)
  tk.Button(btns_frame,text="*",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:self.btn_click("*")).grid(row=1,column=3,padx=1,pady=1)

  tk.Button(btns_frame,text="4",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:self.btn_click("4")).grid(row=2,column=0,padx=1,pady=1)
  tk.Button(btns_frame,text="5",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:self.btn_click("5")).grid(row=2,column=1,padx=1,pady=1)
  tk.Button(btns_frame,text="6",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:self.btn_click("6")).grid(row=2,column=2,padx=1,pady=1)
  tk.Button(btns_frame,text="-",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:self.btn_click("-")).grid(row=2,column=3,padx=1,pady=1)

  tk.Button(btns_frame,text="1",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:self.btn_click("1")).grid(row=3,column=0,padx=1,pady=1)
  tk.Button(btns_frame,text="2",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:self.btn_click("2")).grid(row=3,column=1,padx=1,pady=1)
  tk.Button(btns_frame,text="3",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:self.btn_click("3")).grid(row=3,column=2,padx=1,pady=1)
  tk.Button(btns_frame,text="+",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:self.btn_click("+")).grid(row=3,column=3,padx=1,pady=1)

  tk.Button(btns_frame,text="0",fg="black",width=21,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:self.btn_click("0")).grid(row=4,column=0,columnspan=2,padx=1,pady=1)
  tk.Button(btns_frame,text=".",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:self.btn_click(".")).grid(row=4,column=2,padx=1,pady=1)
  tk.Button(btns_frame,text="=",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=self.evaluate).grid(row=4,column=3,padx=1,pady=1)

 def btn_click(self,item):
  self.expression += str(item)
  self.input_text.set(self.expression)

 def clear(self):
  self.expression = ""
  self.input_text.set("")

 def evaluate(self):
  try:
   result = eval(self.expression)
   self.input_text.set(result)
   self.expression = str(result)
  except Exception as e:
   messagebox.showerror("ошибка", "некорректное выражение")
   self.clear()

 def mem_plus(self):
  global memory
  try:
   memory += float(self.expression)
  except:pass

 def mem_minus(self):
  global memory
  try:
   memory -= float(self.expression)
  except:pass

def run_calculator():
 root = tk.Tk()
 app = CALCULATOR_APP(root)
 root.mainloop()

#тесты
class TestMathFunctions(unittest.TestCase):
 def test_add(self):
  self.assertEqual(ADD(2,3),5)
 def test_subtract(self):
  self.assertEqual(SUBTRACT(5,3),2)
 def test_multiply(self):
  self.assertEqual(MULTIPLY(2,3),6)
 def test_divide(self):
  self.assertEqual(DIVIDE(6,3),2)
 def test_divide_by_zero(self):
  with self.assertRaises(ValueError):
   DIVIDE(1,0)
 def test_power(self):
  self.assertEqual(POWER(2,3),8)
 def test_sqrt(self):
  self.assertEqual(SQRT(9),3)
 def test_sqrt_negative(self):
  with self.assertRaises(ValueError):
   SQRT(-1)

if __name__ == "__main__":
 #run_calculator()
 unittest.main()