from tkinter import *
from tkinter import messagebox
from customtkinter import CTkCheckBox
import customtkinter as ctk
import time

tela = ctk.CTk()

titulo_HB = ctk.CTkLabel(tela, text="HB SYSTEM", font=("Krona One", 25, "bold"),
fg_color="transparent", bg_color="transparent", text_color="white")
titulo_HB.place(x=590, y= 50)

titulo_sobre = ctk.CTkLabel(tela, text="By: Haba", font=("Krona One", 25),
fg_color="transparent", bg_color="transparent", text_color="white")
titulo_sobre.place(x=30, y= 570)

foto_inicial = PhotoImage(file="fotos/entrada/astro.png")
space_foto = ctk.CTkLabel(master=tela, image=foto_inicial, text="",
fg_color="transparent",bg_color="transparent", width=2, height=5)
space_foto.place(x=470, y=120)

carregando_o_app = ctk.CTkProgressBar(master=tela,
orientation=HORIZONTAL, mode="indeterminate", width=500, progress_color="black", fg_color="white")
carregando_o_app.place(x=390, y=550)
carregando_o_app.start()



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
        self.tela.geometry("1280x620")
        self.tela.title("Sistema Operacional 1.0 V")
        #self.tela.iconbitmap("fotos/pro.ico")
        self.tela.resizable(width=False, height=False)
        #self.tela.minsize(width=800, height=400)
        #self.tela.maxsize(width=1280, height=620)

    @staticmethod
    def tela_inicial():

        area_de_trabalho = ctk.CTkFrame(master=tela, width=1280, height=620)

        windows = PhotoImage(file="fotos/desktop/fundo.png")
        
        fundo_windows = ctk.CTkLabel(master=area_de_trabalho, image=windows, text="")

        barra_de_tarefas = ctk.CTkFrame(master=area_de_trabalho, width=1280, height=40,
        corner_radius=0, fg_color="white")
        
        def Apps():    
            frame_apps.place(x=450, y=170)
            windows_botao.place(x=5000)
            windows_botao1.place(x=520 ,y=1)
                   
        #frame de aplicativos do windows
        frame_apps = ctk.CTkFrame(master=area_de_trabalho, width=400, height=400, fg_color="white",
        corner_radius=12, bg_color="transparent")
        
        #botao windows
        windows_bar = PhotoImage(file="fotos/bar/windowsbar.png")
        windows_botao = ctk.CTkButton(master=barra_de_tarefas, image=windows_bar, text="",
        fg_color="white", hover_color="gray", bg_color="white", width=2, height=5, command=Apps)

        def Apps_frame():
            frame_apps.place(x=5000)
            windows_botao.place(x=520 ,y=1)
            windows_botao1.place(x=5000)

        windows_botao1 = ctk.CTkButton(master=barra_de_tarefas, image=windows_bar, text="",
        fg_color="white", hover_color="gray", bg_color="white", width=2, height=5, command=Apps_frame)

        #campo de busca de aplicativos dentro do frame apps
        pesquisar_apps = ctk.CTkEntry(master=frame_apps, placeholder_text="        Search Apps",text_color="white",
        width=300, height=8, fg_color="gray", border_color="black", border_width=2)
        pesquisar_apps.place(x=50, y=20)

        lixeira = PhotoImage(file="fotos/icons/lixeira.png")
        lixeira_trabalho = ctk.CTkButton(master=area_de_trabalho, image=lixeira, text="",
        fg_color="black",bg_color="black", width=15, height=15, hover_color="gray")
        lixeira_trabalho.place(x=15, y=15)
        
        #botao lupa
        lupa_bar = PhotoImage(file="fotos/bar/lupa.png")
        lupa_botao = ctk.CTkButton(master=barra_de_tarefas, image=lupa_bar, text="",
        fg_color="white", hover_color="gray", bg_color="white", width=2, height=5, command=Apps)

        #botao explorer
        pasta_bar = PhotoImage(file="fotos/bar/pasta.png")
        pasta_botao = ctk.CTkButton(master=barra_de_tarefas, image=pasta_bar, text="",
        fg_color="white", hover_color="gray", bg_color="white", width=2, height=5, command=Apps)

        def Fechar_Apps():
            frame_apps.place(x=5000)

        x_fechar = PhotoImage(file="fotos/icons/x.png")
        fechar_apps_button = ctk.CTkButton(master=frame_apps, image=x_fechar, text="", fg_color="transparent",
        hover=None, bg_color="transparent", width=10, height=10, corner_radius=12, command=Fechar_Apps)
        fechar_apps_button.place(x=370, y=3)

        #area de trabalho
        def Home():
            titulo_HB.pack_forget()
            titulo_sobre.pack_forget()
            play_botao.place(x=5000)
            area_de_trabalho.place(x=0, y=0)
            fundo_windows.place(x=0, y=0)
            barra_de_tarefas.place(x=0, y=580)
            windows_botao.place(x=520 ,y=1)
            lupa_botao.place(x=560, y=1)
            pasta_botao.place(x=605, y=1)

        #botao iniciar
        foto_play = PhotoImage(file="fotos/entrada/play.png")
        play_botao = ctk.CTkButton(master=tela, image=foto_play, text="",fg_color="transparent",
        hover_color="gray", bg_color="transparent", hover=None,width=80, height=80, command=Home)
        play_botao.place(x=620, y=460)


Application()

