# Janela -> 500x500
# Título -> Conversor de moedas
# Campos de selecionar moedas de origem e destino (campos de listas) com labels Selecione a moeda de origem
# Botão de "Converter"
# Lista de Exibição com os nomes das moedas

import customtkinter
from pegar_moedas import nomes_moedas, conversoes_disponiveis

# criar e configurar a janela
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x500")

dic_conversoes_disponiveis = conversoes_disponiveis()

# criar os botões, textos e outros elementos
titulo = customtkinter.CTkLabel(janela, text="Conversor de moedas", font=('Arial', 20))
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem")
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino")

def carregar_moedas_destino(moeda_selecionada):
    lista_moedas_destino = dic_conversoes_disponiveis[moeda_selecionada]
    campo_moeda_destino.configure(values=lista_moedas_destino)
    campo_moeda_destino.set(lista_moedas_destino[0])

campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=list(dic_conversoes_disponiveis.keys()),
                                                 command=carregar_moedas_destino)
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=['Selecione uma moeda de origem'])

def converter_moeda():
    print('convertendo')
botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda)

listas_moedas = customtkinter.CTkScrollableFrame(janela)

moedas_disponiveis = nomes_moedas()

for codigo_moeda in moedas_disponiveis:
    nome_moeda =moedas_disponiveis[codigo_moeda]
    text_moeda = customtkinter.CTkLabel(listas_moedas, text=f'{codigo_moeda}: {nome_moeda}')
    text_moeda.pack()


# colocar todos os elementos na tela
titulo.pack(padx= 10, pady=10)
texto_moeda_origem.pack(padx= 10, pady=10)
campo_moeda_origem.pack(padx= 10)
texto_moeda_destino.pack(padx= 10, pady=10)
campo_moeda_destino.pack(padx= 10, pady=10)
botao_converter.pack(padx=10)
listas_moedas.pack(padx=10, pady=10)

# rodar a janela
janela.mainloop()