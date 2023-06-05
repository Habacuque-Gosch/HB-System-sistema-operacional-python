from tkinter import *
import tkinter  as ttk
import customtkinter as ctk

def lixeira_app():

    tela = ctk.CTk()


    class Application():
        def __init__(self):
            self.tela = tela
            self.tema()
            self.layout()
            self.tela_inicial()
            tela.mainloop()

        @staticmethod
        def tema():
            ctk.set_appearance_mode("dark")
            ctk.set_default_color_theme("dark-blue")

        def layout(self):
            self.tela.geometry("400x300")
            self.tela.title("Lixeira")
            self.tela.iconbitmap("fotos/programs/lixeira.ico")
            self.tela.resizable(width=False, height=False)
            #self.tela.minsize(width=800, height=400)
            #self.tela.maxsize(width=1280, height=620)

        @staticmethod
        def tela_inicial():
            cinza = "#d0d0d0"
            branco_cinza = "#D2D2D2"
            cor_area_de_trabalho = "#0f1014"
            entry_lupa = "#dfdfdf"
            preto = "#000000"
            apps_color = "#D9D9D9"

            frame_inicial = ctk.CTkFrame(master=tela, width=400, height=300, fg_color=apps_color,
            bg_color=cor_area_de_trabalho, corner_radius=0)
            frame_inicial.place(x=0, y=0)

            lixeira_label = ctk.CTkLabel(master=frame_inicial, text="A lixeira está vazia", text_color="black")
            lixeira_label.place(x= 150, y= 100)

            frame_line = ctk.CTkFrame(master=frame_inicial, width=400, height=1, fg_color="#000000",
            corner_radius=12, bg_color="#000000")
            frame_line.place(x=0, y=240)

            botao_restaurar = ctk.CTkButton(master=frame_inicial, text="RESTAURAR", hover_color="gray",
            width=131, height=26)
            botao_restaurar.place(x=9,y=260)

            botao_restaurar = ctk.CTkButton(master=frame_inicial, text="ESVAZIAR", hover_color="gray",
            width=90, height=26)
            botao_restaurar.place(x=155 ,y=260)

            botao_restaurar = ctk.CTkButton(master=frame_inicial, text="EXCLUIR", hover_color="gray",
            width=131, height=26)
            botao_restaurar.place(x=260,y=260)

    Application()