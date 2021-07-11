import tkinter as tk
import math
class Calculator(tk.Frame):
    #Створення вікна
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.master.geometry()
        self.master.title('Calculator')
        self.entry = tk.Entry(self.master, justify='right')
        self.creat_widgets()

    #Ввід числа
    def input(self, num):
        def n():
            self.entry.insert(tk.END, num)
        return n

    #Динамічне виконання виразів
    def one_hundredth(self):
        text = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, eval(text + '/100'))

     #Сінус
    def sin(self):
        text=self.entry.get()
        x=float(text)
        text=math.sin(x)
        self.entry.delete(0,tk.END)
        self.entry.insert(0,text)

        #Косинус
    def cos(self):
        text=self.entry.get()
        x=float(text)
        text=math.cos(x)
        self.entry.delete(0,tk.END)
        self.entry.insert(0,text)

          #Тангенс
    def tan(self):
        text=self.entry.get()
        x=float(text)
        text=math.tan(x)
        self.entry.delete(0,tk.END)
        self.entry.insert(0,text)

      #Котан
    def ctan(self):
        text=self.entry.get()
        x=float(text)
        text= math.cos(x)/math.sin(x)
        self.entry.delete(0,tk.END)
        self.entry.insert(0,text)

      #преобразование строки
    def cotan(self):
        text=self.entry.get()
        n=int(text)
        b = ''
        while n > 0:
             b = str(n % 2) + b
             n = n // 2
             print(b)
        self.entry.delete(0,tk.END)
        self.entry.insert(0,b)
        
    def log(self):
       text=self.entry.get()
       x=float(text)
       text=math.log2(x)
       self.entry.delete(0,tk.END)
       self.entry.insert(0,text)

    def ln(self):
       text=self.entry.get()
       x=float(text)
       text=math.log10(x)
       self.entry.delete(0,tk.END)
       self.entry.insert(0,text)
    #Повна чистка рядка
    def clear_all(self):
        self.entry.delete(0, tk.END)

    #Чистка по 1
    def clear_one(self):
        text = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, text[:-1])

    #Зрівняння
    def equals(self):
        self.value = eval(self.entry.get().replace('÷', '/').replace('×', '*').replace('＋', '+').replace('－', '-'))
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.value)


    #Дисплей ( вивід на екран)
    def creat_widgets(self):
        Buttons = [ 
        ['7', '8', '9'], 
        ['4', '5', '6'], 
        ['1', '2', '3'], 
        ]
        self.entry.grid(row=0, column=0, columnspan=6, sticky='nsew')
        for i, ro in enumerate(Buttons):
            for j, co in enumerate(ro):
                tk.Button(self.master, text=co, width=20, command=self.input(co)).grid(row=i+2, column=j)
        
        tk.Button(self.master, text='%', width=20, command=lambda: self.one_hundredth()).grid(row=1, column=0)
        tk.Button(self.master, text='CE', width=20, command=lambda: self.clear_all()).grid(row=1, column=1)
        tk.Button(self.master, text='2k', width=20, command=lambda: self.cotan()).grid(row=1, column=2)
        tk.Button(self.master, text='÷', width=20, command=self.input('÷')).grid(row=1, column=3)
        tk.Button(self.master, text='×', width=20, command=self.input('×')).grid(row=2, column=3)
        tk.Button(self.master, text='－', width=20, command=self.input('－')).grid(row=3, column=3)
        tk.Button(self.master, text='＋', width=20, command=self.input('＋')).grid(row=4, column=3)
        tk.Button(self.master, text='＝', width=20, command=lambda: self.equals()).grid(row=5, column=3)
        tk.Button(self.master, text='0', width=42, command=self.input('0')).grid(row=5, column=0,columnspan=2)
        tk.Button(self.master, text='.', width=20, command=self.input('.')).grid(row=5, column=2)
        tk.Button(self.master,foreground="yellow", text='Практика', background="gray", width=10, command=lambda: Prak()).grid(row=3, column=5)
        tk.Button(self.master, text='log', width=10,height=3, command=lambda: self.ln()).grid(row=4, column=5,rowspan=2)
        tk.Button(self.master, text='ln', width=10,height=3,command=lambda: self.log()).grid(row=1, column=5, rowspan=2)
        tk.Button(self.master, text='⇦', width=20, command=lambda: self.clear_one()).grid(row=1, column=4)
        tk.Button(self.master, text='sin', width=20, command=lambda: self.sin()).grid(row=2, column=4)
        tk.Button(self.master, text='cos', width=20, command=lambda: self.cos()).grid(row=3, column=4)
        tk.Button(self.master, text='tg', width=20, command=lambda: self.tan()).grid(row=4, column=4)
        tk.Button(self.master, text='ctg', width=20, command=lambda: self.ctan()).grid(row=5, column=4)
calc = Calculator(tk.Tk())
calc.mainloop()
