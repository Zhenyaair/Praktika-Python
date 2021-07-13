import http.client
import json
from tkinter import *
import tkinter as tk
root = Tk()
root.title("Covid")
root.geometry('800x800')
root['bg']='#2b5aa6'
n = 10 
conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "1ef98525bemsh87989b428c7abb7p1a0615jsn783fb79eba25",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }
conn.request("GET", "/api/npm-covid-data/asia", headers=headers)
res = conn.getresponse()
data = res.read()
All_Info = data.decode("utf-8")
json = json.loads(All_Info)
frametop=Frame(root)
framebot=Frame(root)
frametop.pack()
framebot.pack()
#Функція, яка заповнює новою інформацію, отриманою на даний момент
def Refresh():
    import json
    TextB.delete(1.0,END)
    conn.request("GET", "/api/npm-covid-data/asia", headers=headers)
    res = conn.getresponse()
    data = res.read()
    All_Info = data.decode("utf-8")
    json = json.loads(All_Info)
    TextB.insert('1.0', '\n')
    TextB.insert('1.0', '~~' * 30)
    for i in range(n):
        TextB.insert('1.0', '\n')
        TextB.insert('1.0', list(json[i].items())[14])
        TextB.insert('1.0', '\n')
        TextB.insert('1.0', list(json[i].items())[12])
        TextB.insert('1.0', '\n')
        TextB.insert('1.0', list(json[i].items())[10])
        TextB.insert('1.0', '\n',)
        TextB.insert('1.0', list(json[i].items())[3])
        TextB.insert('1.0', '\n')
        TextB.insert('1.0', list(json[i].items())[2])
        TextB.insert('1.0', '\n')
        TextB.insert('1.0', '~~' * 30)
# Створення поля для тексту
TextB = Text(framebot,width=500, height=500)
TextB['bg']='#2b5aa6'
TextB['fg']='white'
TextB.pack()
# Клавіша оновлення
RefreshB = Button(frametop, text="Оновити",command=Refresh,width=200, height=2)
RefreshB['bg']='#2b5aa6'
RefreshB['fg']='Yellow'
RefreshB.pack(side=RIGHT)
Refresh()
root.mainloop()
