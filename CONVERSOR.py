import FUNÇÕES as f
import tkinter as tk
import functools as ft
import re


def bt_click(botao):
    if str(x.get()).isnumeric():
        núm = int(x.get())
        if botao["text"] == "dec2bin":
            a = f.dec2bin(núm)
            lb2["text"] = str(a)
        elif botao["text"] == "bin2dec":
            núm = str(núm)
            pattern = re.compile("[0-1]+")
            if pattern.fullmatch(núm):
                núm = int(núm)
                a = f.bin2dec(núm)
                lb2["text"] = str(a)
            else:
                lb2["text"] = "O número não é binário."
        elif botao["text"] == "bin2oct":
            núm = str(núm)
            pattern = re.compile("[0-1]+")
            if pattern.fullmatch(núm):
                núm = int(núm)
                a = f.bin2oct(núm)
                lb2["text"] = str(a)
            else:
                lb2["text"] = "O número não é binário."
        elif botao["text"] == "oct2bin":
            núm = str(núm)
            pattern = re.compile("[0-7]+")
            if pattern.fullmatch(núm):
                núm = int(núm)
                a = f.oct2bin(núm)
                lb2["text"] = str(a)
            else:
                lb2["text"] = "O número não é octal."
        elif botao["text"] == "dec2hex":
            a = f.dec2hex(núm)
            lb2["text"] = a
        elif botao["text"] == "hex2dec":
            a = f.hex2dec(núm)
            lb2["text"] = str(a)
        elif botao["text"] == "hex2bin":
            a = f.hex2bin(núm)
            lb2["text"] = str(a)
        elif botao["text"] == "bin2hex":
            núm = str(núm)
            pattern = re.compile("[0-1]+")
            if pattern.fullmatch(núm):
                núm = int(núm)
                a = f.bin2hex(núm)
                lb2["text"] = str(a)
            else:
                lb2["text"] = "O número não é binário."
    elif str(x.get()) == '':
        lb2["text"] = "Por favor, insira um número."
    else:
        núm = x.get()
        pattern = re.compile("[A-Fa-f0-9]+")
        if pattern.fullmatch(núm):
            if botao["text"] == "hex2dec":
                a = f.hex2dec(núm)
                lb2["text"] = str(a)
            elif botao["text"] == "hex2bin":
                a = f.hex2bin(núm)
                lb2["text"] = str(a)
            else:
                lb2["text"] = "Letras só podem ser usadas em conversão hexinadecimal."
        else:
            lb2["text"] = "O Número inserido utiliza letras e não é hexadecimal."


janela = tk.Tk()
janela.title("Conversor BY:Luan")
janela["bg"] = "black"
janela.geometry("700x500")
janela.resizable(width=False, height=False)
janela.iconbitmap(r'icon.ico')


lb = tk.Label(janela, text="Escolha o metodo de conversão.", font='arial 30', bg='black', fg='white')
lb.pack()

x = tk.Entry(janela, width=16, font='arial 15')
x.pack()

bt = tk.Button(janela, width=15, text="dec2bin", font='arial 15')
bt.pack()
bt["command"] = ft.partial(bt_click, bt)
bt2 = tk.Button(janela, width=15, text="bin2dec", font='arial 15')
bt2["command"] = ft.partial(bt_click, bt2)
bt2.pack()
bt3 = tk.Button(janela, width=15, text="dec2hex", font='arial 15')
bt3["command"] = ft.partial(bt_click, bt3)
bt3.pack()
bt4 = tk.Button(janela, width=15, text="hex2dec", font='arial 15')
bt4["command"] = ft.partial(bt_click, bt4)
bt4.pack()
bt5 = tk.Button(janela, width=15, text="bin2oct", font='arial 15')
bt5["command"] = ft.partial(bt_click, bt5)
bt5.pack()
bt6 = tk.Button(janela, width=15, text="oct2bin", font='arial 15')
bt6["command"] = ft.partial(bt_click, bt6)
bt6.pack()
bt7 = tk.Button(janela, width=15, text="bin2hex", font='arial 15')
bt7["command"] = ft.partial(bt_click, bt7)
bt7.pack()
bt8 = tk.Button(janela, width=15, text="hex2bin", font='arial 15')
bt8["command"] = ft.partial(bt_click, bt8)
bt8.pack()

lb2 = tk.Label(janela, text="O resultado sera exibido aqui.", font='arial 15', bg='black', fg='white')
lb2.pack()

janela.mainloop()