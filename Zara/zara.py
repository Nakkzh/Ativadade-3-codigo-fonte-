import tkinter as tk
from datetime import datetime
import pygame
import pyglet
import webbrowser
import requests

cor1 = "#3d3d3d"  # preta
cor2 = "#fafcff"  # branca
cor3 = "#21c25c"  # verde
cor4 = "#eb463b"  # vermelha
cor5 = "#dedcdc"  # cinza
cor6 = "#3080f0"  # azul

root = tk.Tk()
root.title("ZARA")
root.geometry("440x250")
root.configure(bg=cor1)
root.resizable(width=False, height=True)

#RELOGIO
def relogio():
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%B")
    ano = tempo.strftime("%Y")

    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=f"{dia_semana}  {dia} / {mes} / {ano}")

l1 = tk.Label(root, text="", font=("digital-7", 80), bg=cor1, fg=cor2)
l1.grid(row=0, column=0, sticky="nw", padx=5)

l2 = tk.Label(root, text="", font=("digital-7", 20), bg=cor1, fg=cor2)
l2.grid(row=1, column=0, sticky="nw", padx=5)

#ALARME
frame = tk.Frame(root, bg=cor1)
frame.grid(row=2, column=0, padx=5, pady=10, sticky="w")

hora = tk.StringVar(root)
minuto = tk.StringVar(root)
segundo = tk.StringVar(root)

horas = [str(i).zfill(2) for i in range(24)]
minutos_segundos = [str(i).zfill(2) for i in range(60)]

hora.set(horas[0])
minuto.set(minutos_segundos[0])
segundo.set(minutos_segundos[0])

hora_menu = tk.OptionMenu(frame, hora, *horas)
hora_menu.config(bg=cor5, fg=cor1)
hora_menu.pack(side=tk.LEFT)

minuto_menu = tk.OptionMenu(frame, minuto, *minutos_segundos)
minuto_menu.config(bg=cor5, fg=cor1)
minuto_menu.pack(side=tk.LEFT)

segundo_menu = tk.OptionMenu(frame, segundo, *minutos_segundos)
segundo_menu.config(bg=cor5, fg=cor1)
segundo_menu.pack(side=tk.LEFT)

pygame.mixer.init()

def tocar_som():
    pygame.mixer.Sound("U:/JoaoG/Zara/Despertador.mp3").play()

#CLIMA

API_KEY = "3ee945b64b61d78758e92f37b51f1bfa"
cidade = "Presidente Prudente"

l3 = tk.Label(root, text="", font=("digital-7", 20), bg=cor1, fg=cor2)
l3.grid(row=3, column=0, sticky="nw", padx=5)

def clima():
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"
    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()
    
    descricao = requisicao_dic['weather'][0]['description']
    temperatura = requisicao_dic['main']['temp'] - 273.15
    
    l3.config(text=f"{temperatura:.2f}°C - {descricao}")

clima()
relogio()
root.mainloop()