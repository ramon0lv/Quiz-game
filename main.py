#Um Joguinho de Quiz by Ramon
#Inspirado no Canal Usando Python

import tkinter as tk
from tkinter import PhotoImage
import pandas as pd
import os

# Mudar o diretório de trabalho para o diretório do script
os.chdir(os.path.dirname(__file__))

# Leitura do arquivo Excel
df = pd.read_excel('questions.xlsx')

# Pega 10 perguntas aleatórias
questions = df.sample(n=10).values.tolist()

# Variáveis globais
score = 0
current_question = 0

def display_question():
    global current_question
    if current_question < len(questions):
        question, option1, option2, option3, option4, answer = questions[current_question]
        result_label.config(text=question)
        option1_btn.config(text=option1, command=lambda: check_answer(1, answer))
        option2_btn.config(text=option2, command=lambda: check_answer(2, answer))
        option3_btn.config(text=option3, command=lambda: check_answer(3, answer))
        option4_btn.config(text=option4, command=lambda: check_answer(4, answer))
        # Exibindo os botões
        option1_btn.pack(pady=10)
        option2_btn.pack(pady=10)
        option3_btn.pack(pady=10)
        option4_btn.pack(pady=10)
    else:
        end_game()

def check_answer(selected_option, correct_answer):
    global score, current_question
    if selected_option == correct_answer:
        score += 1
    current_question += 1
    display_question()

def end_game():
    result_label.config(text=f"Você marcou {score} pontos.")
    # Escondendo os botões
    option1_btn.pack_forget()
    option2_btn.pack_forget()
    option3_btn.pack_forget()
    option4_btn.pack_forget()
    # Exibindo o botão 'Jogar Novamente'
    play_again_btn.pack(pady=10)

def restart_game():
    global score, current_question
    score = 0
    current_question = 0
    play_again_btn.pack_forget()
    display_question()

root = tk.Tk()
root.title('Quiz')
root.geometry('420x400')
root.resizable(False, False)

background_color = '#ffdcb9'
text_color = '#333333'
button_color = '#08a9f1'
button_text_color = '#ffffff'

root.config(bg=background_color)
root.option_add('*Font', 'Arial')

# Ícone do app
app_icon = PhotoImage(file='img/quiz_game_icon.png')
app_label = tk.Label(root, image=app_icon, bg=background_color)
app_label.pack(pady=10, padx=(30, 30))

# Componentes da interface
result_label = tk.Label(root, text='', wraplength=380, bg=background_color, fg=text_color, font=('Arial', 12, 'bold'))
result_label.pack(pady=20, padx=(30, 30))

option1_btn = tk.Button(root, text='', width=30, bg=button_color, fg=button_text_color, font=('Arial', 10, 'bold'))
option2_btn = tk.Button(root, text='', width=30, bg=button_color, fg=button_text_color, font=('Arial', 10, 'bold'))
option3_btn = tk.Button(root, text='', width=30, bg=button_color, fg=button_text_color, font=('Arial', 10, 'bold'))
option4_btn = tk.Button(root, text='', width=30, bg=button_color, fg=button_text_color, font=('Arial', 10, 'bold'))

play_again_btn = tk.Button(root, text='Jogar Novamente', width=30, bg=button_color, fg=button_text_color, font=('Arial', 10, 'bold'), command=restart_game)

display_question()

root.mainloop()
