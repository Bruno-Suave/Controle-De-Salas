import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

# window
window = ttk.Window(themename = 'journal')
window.title('Controle de Salas')
window.geometry('1024x768')

# title
docente_label = ttk.Label(master = window, text = 'Nome do Docente')
docente_label.pack(side = 'left') 

# run
window.mainloop()