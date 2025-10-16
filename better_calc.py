# calculadora com tkinter
# execute com python better_calc.py

import tkinter as tk
from math import sqrt, log, sin, radians

# ---------------- Funções básicas da calculadora ----------------
def pressionar(botao):
    entrada_texto.set(entrada_texto.get() + str(botao))

def calcular():
    try:
        resultado = str(eval(entrada_texto.get()))
        entrada_texto.set(resultado)
    except:
        entrada_texto.set("Erro")

def limpar():
    entrada_texto.set("")

# ---------------- Função da Bhaskara ----------------
def abrir_bhaskara():
    janela_bhaskara = tk.Toplevel(janela)
    janela_bhaskara.title("Calculadora de Bhaskara")

    def calcular_bhaskara():
        try:
            a = float(entrada_a.get())
            b = float(entrada_b.get())
            c = float(entrada_c.get())
            delta = b**2 - 4*a*c

            if delta < 0:
                resultado_texto.set("Não há raízes reais")
                formula_texto.set(f"Δ = b² - 4ac = {b}² - 4*{a}*{c} = {delta}")
            else:
                x1 = (-b + sqrt(delta)) / (2*a)
                x2 = (-b - sqrt(delta)) / (2*a)
                resultado_texto.set(f"x1 = {x1:.2f}, x2 = {x2:.2f}")
                formula = f"Δ = b² - 4ac = {b}² - 4*{a}*{c} = {delta}\n"
                formula += f"x1 = (-b + √Δ)/(2a) = (-{b} + √{delta})/(2*{a}) = {x1:.2f}\n"
                formula += f"x2 = (-b - √Δ)/(2a) = (-{b} - √{delta})/(2*{a}) = {x2:.2f}"
                formula_texto.set(formula)

        except ValueError:
            resultado_texto.set("Erro: valores inválidos")
            formula_texto.set("")
        except ZeroDivisionError:
            resultado_texto.set("Erro: a não pode ser 0")
            formula_texto.set("")
            
    tk.Label(janela_bhaskara, text="Cálculo de Bhaskara = (-b ± √(b² - 4ac)) / 2a", font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(janela_bhaskara, text="a:").grid(row=1, column=0)
    entrada_a = tk.Entry(janela_bhaskara)
    entrada_a.grid(row=1, column=1)

    tk.Label(janela_bhaskara, text="b:").grid(row=2, column=0)
    entrada_b = tk.Entry(janela_bhaskara)
    entrada_b.grid(row=2, column=1)

    tk.Label(janela_bhaskara, text="c:").grid(row=3, column=0)
    entrada_c = tk.Entry(janela_bhaskara)
    entrada_c.grid(row=3, column=1)

    resultado_texto = tk.StringVar()
    formula_texto = tk.StringVar()

    tk.Label(janela_bhaskara, textvariable=resultado_texto, fg="blue").grid(row=4, column=0, columnspan=2)
    tk.Label(janela_bhaskara, textvariable=formula_texto, justify="left").grid(row=5, column=0, columnspan=2)

    tk.Button(janela_bhaskara, text="Calcular Bhaskara", command=calcular_bhaskara).grid(row=6, column=0, columnspan=2, pady=10)

# ---------------- Função Afim ----------------
def abrir_funcao_afim():
    janela_afim = tk.Toplevel(janela)
    janela_afim.title("Função Afim")

    def calcular_afim():
        try:
            a = float(entrada_a.get())
            b = float(entrada_b.get())
            x = float(entrada_x.get())
            resultado = a * x + b
            resultado_texto.set(f"f({x}) = {resultado:.2f}")
            formula_texto.set(f"f(x) = {a}*{x} + {b} = {resultado:.2f}")
        except ValueError:
            resultado_texto.set("Erro: valores inválidos")
            formula_texto.set("")
    
    tk.Label(janela_afim, text="Cálculo Afim = a*x + b", font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(janela_afim, text="a:").grid(row=1, column=0)
    entrada_a = tk.Entry(janela_afim)
    entrada_a.grid(row=1, column=1)

    tk.Label(janela_afim, text="b:").grid(row=2, column=0)
    entrada_b = tk.Entry(janela_afim)
    entrada_b.grid(row=2, column=1)

    tk.Label(janela_afim, text="x:").grid(row=3, column=0)
    entrada_x = tk.Entry(janela_afim)
    entrada_x.grid(row=3, column=1)

    resultado_texto = tk.StringVar()
    formula_texto = tk.StringVar()

    tk.Label(janela_afim, textvariable=resultado_texto, fg="blue").grid(row=5, column=0, columnspan=2)
    tk.Label(janela_afim, textvariable=formula_texto, justify="left").grid(row=6, column=0, columnspan=2)

    tk.Button(janela_afim, text="Calcular", command=calcular_afim).grid(row=7, column=0, columnspan=2, pady=10)

# ---------------- Função Logarítmica ----------------
def abrir_log():
    janela_log = tk.Toplevel(janela)
    janela_log.title("Função Logarítmica")

    def calcular_log():
        try:
            a = float(entrada_a.get())
            b = float(entrada_b.get())
            x = float(entrada_x.get())
            if a <= 0 or a == 1 or x <= 0:
                raise ValueError("Base ou argumento inválido")
            resultado = log(x, a) + b
            resultado_texto.set(f"f({x}) = {resultado:.2f}")
            formula_texto.set(f"f(x) = log{a}({x}) + {b} = {resultado:.2f}")
        except ValueError:
            resultado_texto.set("Erro: valores inválidos")
            formula_texto.set("")

    tk.Label(janela_log, text="Cálculo Logarítmico = log base(argumento) + constante", font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
    
    tk.Label(janela_log, text="a (base):").grid(row=1, column=0)
    entrada_a = tk.Entry(janela_log)
    entrada_a.grid(row=1, column=1)

    tk.Label(janela_log, text="x (argumento):").grid(row=3, column=0)
    entrada_x = tk.Entry(janela_log)
    entrada_x.grid(row=3, column=1)
    
    tk.Label(janela_log, text="b (constante):").grid(row=2, column=0)
    entrada_b = tk.Entry(janela_log)
    entrada_b.grid(row=2, column=1)

    resultado_texto = tk.StringVar()
    formula_texto = tk.StringVar()

    tk.Label(janela_log, textvariable=resultado_texto, fg="blue").grid(row=4, column=0, columnspan=2)
    tk.Label(janela_log, textvariable=formula_texto, justify="left").grid(row=5, column=0, columnspan=2)

    tk.Button(janela_log, text="Calcular", command=calcular_log).grid(row=6, column=0, columnspan=2, pady=10)

# ---------------- Raiz ----------------
def abrir_raiz():
    janela_raiz = tk.Toplevel(janela)
    janela_raiz.title("Cálculo de Raiz")

    def calcular_raiz():
        try:
            n = float(entrada_n.get())
            raiz = float(entrada_raiz.get())
            if raiz <= 0:
                raise ValueError("Índice da raiz deve ser maior que 0")
            resultado = n ** (1 / raiz)
            resultado_texto.set(f"Resultado: {resultado:.2f}")
            formula_texto.set(f"{raiz}√{n} = {resultado:.2f}")
        except ValueError:
            resultado_texto.set("Erro: valores inválidos")
            formula_texto.set("")
    
    tk.Label(janela_raiz, text="Cálculo de Raiz = raiz√numero", font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
    
    tk.Label(janela_raiz, text="Índice da Raiz:").grid(row=1, column=0)
    entrada_raiz = tk.Entry(janela_raiz)
    entrada_raiz.grid(row=1, column=1)
    
    tk.Label(janela_raiz, text="Número (n):").grid(row=0, column=0)
    entrada_n = tk.Entry(janela_raiz)
    entrada_n.grid(row=0, column=1)

    resultado_texto = tk.StringVar()
    formula_texto = tk.StringVar()

    tk.Label(janela_raiz, textvariable=resultado_texto, fg="blue").grid(row=2, column=0, columnspan=2)
    tk.Label(janela_raiz, textvariable=formula_texto, justify="left").grid(row=3, column=0, columnspan=2)

    tk.Button(janela_raiz, text="Calcular Raiz", command=calcular_raiz).grid(row=4, column=0, columnspan=2, pady=10)

# ---------------- Seno ----------------
def abrir_seno():
    janela_seno = tk.Toplevel(janela)
    janela_seno.title("Cálculo de Seno")
    janela_seno.geometry("300x220")

    def calcular_seno():
        try:
            cateto_oposto = float(entrada_oposto.get())
            hipotenusa = float(entrada_hipotenusa.get())
            if hipotenusa <= 0 or cateto_oposto < 0 or cateto_oposto > hipotenusa:
                raise ValueError("Valores inválidos para cateto ou hipotenusa")
            
            seno = cateto_oposto / hipotenusa
            resultado_texto.set(f"Seno: {seno:.4f}")
            formula_texto.set(f"sen(θ) = cateto oposto / hipotenusa = {cateto_oposto} / {hipotenusa} = {seno:.4f}")
        except ValueError:
            resultado_texto.set("Erro: valor inválido")
            formula_texto.set("")

    tk.Label(janela_seno, text="Cateto oposto (sen = oposto / hipotenusa):", font= ('Arial', 11, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
    
    # Campo cateto oposto
    tk.Label(janela_seno, text="Cateto Oposto:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entrada_oposto = tk.Entry(janela_seno, width=15, font=('Arial', 12))
    entrada_oposto.grid(row=1, column=1, padx=10, pady=5)

    # Campo hipotenusa
    tk.Label(janela_seno, text="Hipotenusa:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entrada_hipotenusa = tk.Entry(janela_seno, width=15, font=('Arial', 12))
    entrada_hipotenusa.grid(row=2, column=1, padx=10, pady=5)

    # Resultado
    resultado_texto = tk.StringVar()
    formula_texto = tk.StringVar()

    tk.Label(janela_seno, textvariable=resultado_texto, fg="blue", font=('Arial', 12)).grid(row=3, column=0, columnspan=2, pady=5)
    tk.Label(janela_seno, textvariable=formula_texto, justify="left", font=('Arial', 10)).grid(row=4, column=0, columnspan=2)

    # Botão Calcular
    tk.Button(janela_seno, text="Calcular", command=calcular_seno, font=('Arial', 12), bg="#d0f0c0").grid(row=5, column=0, columnspan=2, pady=10)

# ---------------- Janela principal ----------------
janela = tk.Tk()
janela.title("Calculadora Completa")
janela.geometry("600x700")

entrada_texto = tk.StringVar()
display = tk.Entry(janela, textvariable=entrada_texto, font=('Arial', 20), bd=10, relief='sunken', justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

linha = 1
coluna = 0
for botao in botoes:
    if botao == '=':
        b = tk.Button(janela, text=botao, width=5, height=2, font=('Arial', 18), command=calcular)
    else:
        b = tk.Button(janela, text=botao, width=5, height=2, font=('Arial', 18), command=lambda b=botao: pressionar(b))
    b.grid(row=linha, column=coluna, padx=5, pady=5)
    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

b_limpar = tk.Button(janela, text='C', width=5, height=2, font=('Arial', 18), command=limpar)
b_limpar.grid(row=linha, column=0, columnspan=4, sticky='we', padx=5, pady=5)

# ---------------- Botão para mostrar/ocultar as fórmulas ----------------
formulas_visiveis = False

def alternar_formulas():
    global formulas_visiveis
    formulas_visiveis = not formulas_visiveis
    if formulas_visiveis:
        b_afim.grid(row=linha+2, column=0, padx=5, pady=5)
        b_bhaskara.grid(row=linha+2, column=1, padx=5, pady=5)
        b_toggle.config(text="Ocultar Fórmulas")
    else:
        b_afim.grid_remove()
        b_bhaskara.grid_remove()
        b_toggle.config(text="Mostrar Fórmulas")

b_toggle = tk.Button(janela, text="Mostrar Fórmulas", font=('Arial', 14), bg='#2e86de', fg='white', command=alternar_formulas)
b_toggle.grid(row=linha+1, column=0, columnspan=4, sticky='we', padx=5, pady=10)

# Botões de fórmulas (ocultos inicialmente)
b_afim = tk.Button(janela, text='Função Afim', font=('Arial', 14), command=abrir_funcao_afim)
b_bhaskara = tk.Button(janela, text='Bhaskara', font=('Arial', 14), command=abrir_bhaskara)

# Botão Logarítmica 
b_log = tk.Button(janela, text='Log', width=5, height=2, font=('Arial', 18), command=abrir_log) 
b_log.grid(row=linha, column=6, columnspan=2, sticky='we', padx=6, pady=6)

# Botão raiz
b_raiz = tk.Button(janela, text='Raiz', width=5, height=2, font=('Arial', 18), command=abrir_raiz)
b_raiz.grid(row=linha+1, column=6, columnspan=2, sticky='we', padx=6, pady=6)

# Botão seno
b_seno = tk.Button(janela, text='Seno', width=5, height=2, font=('Arial', 18), command=abrir_seno)
b_seno.grid(row=linha-1, column=6, columnspan=2, sticky='we', padx=6, pady=6)

janela.mainloop()
