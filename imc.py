import tkinter as tk
from tkinter import messagebox

def Calculo_IMC():
    try:
        altura = float(entry_altura.get())
        peso = float(entry_peso.get())
        
        imc = peso / (altura ** 2)
        resultado.set(f"O seu IMC é igual a: {imc:.2f}")
        
        if imc < 18.5:
            resultadoimc = "Você está abaixo do peso normal."
        elif 18.5 <= imc < 24.9:
            resultadoimc = "Você está com o peso normal."
        elif 25 <= imc < 29.9:
            resultadoimc = "Você está com sobrepeso."
        else:
            resultadoimc = "Você está com obesidade, procure um médico."
            
        messagebox.showinfo("Resultado do cálculo do IMC", f"O seu IMC é igual a: {imc:.2f}\n{resultadoimc}")
        
    except ValueError:
        messagebox.showerror("Ocorreu um erro ao realizar a leitura dos dados.", "Por favor, informe os dados de forma correta para a operação poder ser realizada.")

root = tk.Tk()
root.title("Calculadora de IMC")

tk.Label(root, text="Nome:").grid(row=0, column=0, padx=16, pady=16)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=16, pady=16)

tk.Label(root, text="Altura (m):").grid(row=1, column=0, padx=16, pady=16)
entry_altura = tk.Entry(root)
entry_altura.grid(row=1, column=1, padx=16, pady=16)

tk.Label(root, text="Peso (kg):").grid(row=2, column=0, padx=16, pady=16)
entry_peso = tk.Entry(root)
entry_peso.grid(row=2, column=1, padx=16, pady=16)

resultado = tk.StringVar()
tk.Label(root, textvariable=resultado, justify="left").grid(row=3, column=0, columnspan=2, padx=10, pady=10)

tk.Button(root, text="Calcular IMC", command=Calculo_IMC).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
