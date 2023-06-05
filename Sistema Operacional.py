from tkinter import *
import tkinter  as ttk
from tkinter import filedialog, messagebox
from tkinter .filedialog import askopenfilename
from customtkinter import CTkCheckBox
import customtkinter as ctk
from PIL import Image, ImageTk
import webbrowser
import time
#importando os apps
from jogos.snake import Snake
from jogos.pacman import pacman
from programas.lixeira import Lixeira

#TELA
tela = ctk.CTk()

#TITULO PRINCIPAL DA INICIALIZAÇÃO
titulo_HB = ctk.CTkLabel(tela, text="HB SYSTEM", font=("Krona One", 35, "bold"),
fg_color="transparent", bg_color="transparent", text_color="white")
titulo_HB.place(x=580, y= 50)

texto = "By: Haba|"
cont = 0
txt = ''

#TEXTO HABA DA INTRODUCAO
titulo_sobre = ctk.CTkLabel(tela, text=texto, font=("Krona One", 25, "bold"),
fg_color="transparent", bg_color="transparent", text_color="white")

def slider():
    global cont, txt
    if  cont >= len(texto):
        cont = -1 
        txt = ""
        titulo_sobre.configure(text=txt)
    else:
        txt = txt + texto[cont]
        titulo_sobre.configure(text=txt)
    cont += 1 
    titulo_sobre.after(200, slider)
slider()

#ASTRONAUTA DA INICIALIZAÇÃO
foto_inicial = PhotoImage(file="fotos/entrada/astro.png")
space_foto = ctk.CTkLabel(master=tela, image=foto_inicial, text="",
fg_color="transparent",bg_color="transparent", width=2, height=5)
space_foto.place(x=470, y=120)

#TASKBARR DA INICIALIZAÇÃO
carregando_o_app = ctk.CTkProgressBar(master=tela, orientation=HORIZONTAL,
mode="indeterminate", width=1280, progress_color="black",
fg_color="white", corner_radius= 0)
carregando_o_app.place(x=0, y=570)
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
        self.tela.title("HB GOSCH")
        self.tela.iconbitmap("fotos/frame_apps/dev.ico")
        self.tela.resizable(width=False, height=False)
        #self.tela.minsize(width=800, height=400)
        #self.tela.maxsize(width=1280, height=620)

    @staticmethod
    def tela_inicial():
               
        #IMAGENS DA INTRODUÇÃO
        foto_astro = PhotoImage(file="fotos/entrada/hellow.png")
        foto_explorer = PhotoImage(file="fotos/entrada/explorer.png")

        #FRAME DE FUNDO DOS TEXTOS DA INTRODUÇÃO
        frame_fundo  = ctk.CTkFrame(master=tela, width=520, height=500, fg_color="#343434",
        corner_radius=12, bg_color="transparent")
        
        astro = ctk.CTkLabel(master=tela, image=foto_astro, text="",fg_color="transparent",
        bg_color="transparent",width=80, height=80)

        #INTRODUÇÃO TEXTOS E BOTAO DO SISTEMA
        sobre_mim = ctk.CTkLabel(master=frame_fundo, text="Olá, seja muito bem-vindo(a), meu nome é Habacuque Gosch,                  \n"
                                                        "e esse projeto foi desenvolvido com o intuito de simular um si-                  \n"
                                                        "stema operacional assim como o windows ou linux. O projeto                    \n"
                                                        "foi programado somente utilizando python.                                                 \n"
                                , text_color="white", font=("Montserrat", 18), width=10)
        sobre_mim.place(x=15, y= 60)
        
        sobre_o_sistema = ctk.CTkLabel(master=frame_fundo, text="Bem o sistema ele já vem com alguns programamas básicos                   \n"
                                                                "que eu mesmo desenvolvi assim como: calculadora, explor                     \n"
                                                                "ador de arquivos, e o jogo do pacman.                                                     \n"
                                , text_color="white", font=("Montserrat", 18), width=10)
        sobre_o_sistema.place(x=15, y= 180)
        
        inicia_o_sistema = ctk.CTkLabel(master=frame_fundo, text="Para estar dando inicio a o sistema basta clicar no botão logo\n"
                                                            "abaixo:                                                                                      \n"
                                , text_color="white", font=("Montserrat", 18), width=10)
        inicia_o_sistema.place(x=15, y= 300)

        #TELA INICIAL       

        #CORES
        cinza = "#d0d0d0"
        branco_cinza = "#D2D2D2"
        cor_area_de_trabalho = "#0f1014"
        entry_lupa = "#dfdfdf"
        preto = "#000000"
        apps_color = "#D9D9D9"

        area_de_trabalho = ctk.CTkFrame(master=tela, width=1280, height=620)

        windows = PhotoImage(file="fotos/desktop/fundo.png")
        fundo_area_de_trabalho = ctk.CTkLabel(master=area_de_trabalho, image=windows, text="")

        barra_de_tarefas = ctk.CTkFrame(master=area_de_trabalho, width=1280, height=40,
        corner_radius=0, fg_color=cinza)

        home_indicate = ctk.CTkLabel(master=barra_de_tarefas, text='', width=38, height=1, bg_color=cinza)
        home_indicate.place(x= 600, y= 38)

        pesquisa_indicate = ctk.CTkLabel(master=barra_de_tarefas, text='', width=38, height=1, bg_color=cinza)
        pesquisa_indicate.place(x= 640, y =38)

        pesquisa_indicate = ctk.CTkLabel(master=barra_de_tarefas, text='', width=38, height=1, bg_color=cinza)
        pesquisa_indicate.place(x= 680, y =38)

        def hide():
            home_indicate._bg_color = cinza

        def Apps():    
            frame_apps.place(x=450, y=170)
            windows_botao_bar.place(x=5000)
            windows_botao_toggle.place(x=600 ,y=1)
            home_indicate["bg_color"] = preto
            home_indicate._bg_color = preto
            hide()
     
        #FRAME APPS
        frame_apps = ctk.CTkFrame(master=area_de_trabalho, width=400, height=400, fg_color=branco_cinza,
        corner_radius=12, bg_color="#0f1014")

        #CAMPO DE BUSCA DE APLICATIVOS NO FRAME APPS
        pesquisar_apps = ctk.CTkEntry(master=frame_apps, placeholder_text="         Search Apps",
        text_color="black",width=344, height=8, fg_color="#dfdfdf", border_color="black", border_width=2)
        pesquisar_apps.place(x=30, y=20)

        # LUPA NO FRAME APPS
        lupa_frame_apps = PhotoImage(file="fotos/frame_apps/frame_icons/lupa.png")
        lupa_icone_apps = ctk.CTkLabel(master=frame_apps, image=lupa_frame_apps, text="",
        fg_color=entry_lupa, width=1, height=1)
        lupa_icone_apps.place(x=40 ,y=22)

        #AREA DE TRABALHO//FRAME APPS
        user_frame_apps = PhotoImage(file="fotos/frame_apps/frame_icons/user.png")
        off_frame_apps = PhotoImage(file="fotos/frame_apps/frame_icons/off.png")
        encerrando_frame_apps = PhotoImage(file="fotos/frame_apps/frame_icons/off.png")
        windows_bar = PhotoImage(file="fotos/bar/windowsbar.png")
        x_frame_apps = PhotoImage(file="fotos/frame_apps/frame_icons/x.png")
        alfinete_frame_apps = PhotoImage(file="fotos/frame_apps/frame_icons/alfinete.png")
        seta_frame_apps = PhotoImage(file="fotos/frame_apps/frame_icons/seta_apps.png")
        google_frame_apps = PhotoImage(file="fotos/frame_apps/apps/snake.png")
        calculadora_frame_apps = PhotoImage(file="fotos/frame_apps/apps/calculadora.png")
        notas_frame_apps = PhotoImage(file="fotos/frame_apps/apps/notas.png")
        youtube_frame_apps = PhotoImage(file="fotos/frame_apps/apps/youtube.png")
        pacman_frame_apps = PhotoImage(file="fotos/frame_apps/apps/pacman.png")
        paint_frame_apps = PhotoImage(file="fotos/frame_apps/apps/pincel.png")
        opera_frame_apps = PhotoImage(file="fotos/frame_apps/apps/opera.png")
        config_frame_apps = PhotoImage(file="fotos/frame_apps/apps/configuracoes.png")
        xls_frame_apps = PhotoImage(file="fotos/frame_apps/recomendados/xls.png")
        doc_frame_apps = PhotoImage(file="fotos/frame_apps/recomendados/doc.png")

        # LABEL "FIXADO" NO FRAME APPS
        fixado_label = ctk.CTkLabel(master=frame_apps, text="Fixado", text_color="black", font=("Montserrat", 12),
        fg_color=branco_cinza, bg_color=branco_cinza )
        fixado_label.place(x=40, y=50)

        # ICONE ALFINETE NO FRAME APPS
        alfinete_icone_apps = ctk.CTkLabel(master=frame_apps, text="", image=alfinete_frame_apps, bg_color=branco_cinza, fg_color=branco_cinza )
        alfinete_icone_apps.place(x=80, y=50)

        # FRASE "todos os apps" NO FRAME APPS
        all_apps_label = ctk.CTkLabel(master=frame_apps, text="Todos os apps", text_color="black", font=("Montserrat", 12),
        fg_color=branco_cinza, bg_color=branco_cinza )
        all_apps_label.place(x=255, y=50)

        # BOTAO MENU TODOS OS APPS NO FRAME APPS
        botao_all_apps = ctk.CTkButton(master=frame_apps, text="", image=seta_frame_apps,
        bg_color=branco_cinza, fg_color=branco_cinza, hover=None, width=15, height=15)
        botao_all_apps.place(x=340, y=52)

        # APPS EM FRAME APPS

        # GOOGLE CHROME APP FRAME APPS
        snake_app = ctk.CTkButton(master=frame_apps, text="", image=google_frame_apps,
        fg_color=branco_cinza, bg_color=branco_cinza, width=1, height=1, hover_color="gray", command= lambda: Snake.app())
        snake_app.place(x=35, y=90)

        # GOOGLE CHROME LABEL FRAME APPS
        chrome_name_label = ctk.CTkLabel(master=frame_apps, text="Snake",
        text_color="black", fg_color="transparent", bg_color="transparent", font=("Montserrat",12))
        chrome_name_label.place(x=35, y=130)

        # CALCULADORA APP FRAME APPS
        calculadora_app = ctk.CTkButton(master=frame_apps, text="", image=calculadora_frame_apps,
        fg_color=branco_cinza, bg_color=branco_cinza, width=1, height=1, hover_color="gray")
        calculadora_app.place(x=135, y=90)

        # CALCULADORA LABEL FRAME APPS
        calculadora_name_label = ctk.CTkLabel(master=frame_apps, text="Calculadora",
        text_color="black", fg_color="transparent", bg_color="transparent", font=("Montserrat",12))
        calculadora_name_label.place(x=120, y=130)

        # BLOCO DE NOTAS APP FRAME APPS
        bloco_de_notas_app = ctk.CTkButton(master=frame_apps, text="", image=notas_frame_apps,
        fg_color=branco_cinza, bg_color=branco_cinza, width=1, height=1, hover_color="gray")
        bloco_de_notas_app.place(x=235, y=90)
        # BLOCO DE NOTAS LABEL FRAME APPS
        bloco_de_notas_name_label = ctk.CTkLabel(master=frame_apps, text="Bloco de notas",
        text_color="black", fg_color="transparent", bg_color="transparent", font=("Montserrat",12))
        bloco_de_notas_name_label.place(x=210, y=130)

        # APP YOUTUBE FRAME APPS
        def link_youtube():
            webbrowser.open("https://www.youtube.com")

        youtube_app = ctk.CTkButton(master=frame_apps, text="", image=youtube_frame_apps,
        fg_color=branco_cinza, bg_color=branco_cinza, width=1, height=1, hover_color="gray", command=link_youtube)
        youtube_app.place(x=330, y=90)

        # YOUTUBE LABEL FRAME APPS
        youtube_name_label = ctk.CTkLabel(master=frame_apps, text="Youtube",
        text_color="black", fg_color="transparent", bg_color="transparent", font=("Montserrat",12))
        youtube_name_label.place(x=325, y=130)

        # APP PACMAN FRAME APPS
        pacman_app = ctk.CTkButton(master=frame_apps, text="", image=pacman_frame_apps,
        fg_color=branco_cinza, bg_color=branco_cinza, width=1, height=1, hover_color="gray", command= lambda: pacman.pacman_app())
        pacman_app.place(x=35, y=170)

        # APP PACMAN LABEL FRAME APPS
        pacman_name_label = ctk.CTkLabel(master=frame_apps, text="Pacman",
        text_color="black", fg_color="transparent", bg_color="transparent", font=("Montserrat",12))
        pacman_name_label.place(x=30, y=210)

        # APP PAINT FRAME APPS
        paint_app = ctk.CTkButton(master=frame_apps, text="", image=paint_frame_apps,
        fg_color=branco_cinza, bg_color=branco_cinza, width=1, height=1, hover_color="gray")
        paint_app.place(x=135, y=170)

        # PAINT LABEL FRAME APPS
        paint_name_label = ctk.CTkLabel(master=frame_apps, text="Paint",
        text_color="black", fg_color="transparent", bg_color="transparent", font=("Montserrat",12))
        paint_name_label.place(x=140, y=210)

        def link_opera():
            webbrowser.open("https://www.opera.com/pt-br/gx")

        # APP OPERA FRAME APPS
        opera_app = ctk.CTkButton(master=frame_apps, text="", image=opera_frame_apps,
        fg_color=branco_cinza, bg_color=branco_cinza, width=1, height=1, hover_color="gray", command=link_opera)
        opera_app.place(x=235, y=170)

        # OPERA LABEL FRAME APPS
        opera_name_label = ctk.CTkLabel(master=frame_apps, text="Opera Gx",
        text_color="black", fg_color="transparent", bg_color="transparent", font=("Montserrat",12))
        opera_name_label.place(x=230, y=210)

        # APP CONFIGURAÇOES FRAME APPS
        configuraçoes_app = ctk.CTkButton(master=frame_apps, text="", image=config_frame_apps,
        fg_color=branco_cinza, bg_color=branco_cinza, width=1, height=1, hover_color="gray")
        configuraçoes_app.place(x=330, y=170)

        # CONFIGURACOES LABEL FRAME APPS
        configuraçoes_name_label = ctk.CTkLabel(master=frame_apps, text="Configurações",
        text_color="black", fg_color="transparent", bg_color="transparent", font=("Montserrat",12))
        configuraçoes_name_label.place(x=310, y=210)

        # LABEL "RECOMENDADOS" NO FRAME APPS
        recomendados_label = ctk.CTkLabel(master=frame_apps, text="Recomendados", text_color="black", font=("Montserrat", 12),
        fg_color=branco_cinza, bg_color=branco_cinza )
        recomendados_label.place(x=40, y=250)

        # LABEL "MAIS" NO FRAME APPS
        mais_apps_label = ctk.CTkLabel(master=frame_apps, text="Mais", text_color="black", font=("Montserrat", 12),
        fg_color=branco_cinza, bg_color=branco_cinza )
        mais_apps_label.place(x=315, y=250)

        # BOTAO MAIS NO FRAME APPS
        botao_mais_apps = ctk.CTkButton(master=frame_apps, text="", image=seta_frame_apps, bg_color=branco_cinza,
        fg_color=branco_cinza, hover=None, width=15, height=15)
        botao_mais_apps.place(x=340, y=252)

        # XLS RECOMENDADO FRAME APPS
        xsl_recomendados = ctk.CTkButton(master=frame_apps, text="", image=xls_frame_apps,
        fg_color=branco_cinza, bg_color=branco_cinza, width=1, height=1, hover_color="gray")
        xsl_recomendados.place(x=35, y=285)

        # XLS LABEL FRAME APPS
        xsl_name_label = ctk.CTkLabel(master=frame_apps, text="Arquivo 1",
        text_color="black", fg_color="transparent", bg_color="transparent", font=("Montserrat",12))
        xsl_name_label.place(x=75, y=290)

        # DOCS RECOMENDADOS FRAME APPS
        docs_recomendado = ctk.CTkButton(master=frame_apps, text="", image=doc_frame_apps,
        fg_color=branco_cinza, bg_color=branco_cinza, width=1, height=1, hover_color="gray")
        docs_recomendado.place(x=235, y=285)

        # DOCS RECOMENDADOS LABEL FRAME APPS
        docs_name_label = ctk.CTkLabel(master=frame_apps, text="Arquivo 2",
        text_color="black", fg_color="transparent", bg_color="transparent", font=("Montserrat",12))
        docs_name_label.place(x=275, y=290)

        #BOTAO DE FECHAR OS APPS NO FRAME DE APPS
        def fechar_frame_apps():
            frame_apps.place(x=5000)
            home_indicate["bg_color"] = cinza
            home_indicate._bg_color = cinza

        fechar_apps_button = ctk.CTkButton(master=frame_apps, image=x_frame_apps, text="", fg_color="transparent",
        hover=None, bg_color="transparent", width=10, height=10, corner_radius=12, command=fechar_frame_apps)
        fechar_apps_button.place(x=370, y=3)

        #LINHA NO FRAME DE APPS
        frame_line = ctk.CTkFrame(master=frame_apps, width=413, height=1, fg_color="#000000",
        corner_radius=12, bg_color="#000000")
        frame_line.place(x=0, y=340)

        # FOTO DE USUARIO NO FRAME DE APPS
        user = ctk.CTkLabel(master=frame_apps, image=user_frame_apps, text="",
        bg_color=branco_cinza,fg_color=branco_cinza)

        foto_user_label = ttk.Label(frame_apps, bg=branco_cinza, width=35, height=35)
        
        upload_foto_user = ttk.Button(frame_apps, text='upload foto', bg=branco_cinza,
        fg=branco_cinza, image=user_frame_apps)
        upload_foto_user.place(x=27, y=350)
        #TROCAR FOTO DE USUARIO NO FRAME DE APPS
        def trocar_de_foto():
            global img
            filename =  filedialog.askopenfilename(initialdir="C:", title="selecione a imagem", filetypes=(("png images","*.png"),("jpeg images","*.jpeg")))
            img = Image.open(filename)
            img = ImageTk.PhotoImage(img)
            foto_user_label['image'] = img
            upload_foto_user.place(x=5000)

        upload_foto_user['command'] = trocar_de_foto
        foto_user_label.place(x=27, y=350)
     
        #ENTRADA DO NOME DE USUARIO NA INTRODUÇÃO
        insira_o_nome = ctk.CTkEntry(master=frame_fundo, placeholder_text="insira seu nome antes de iniciar",
        placeholder_text_color=branco_cinza,font=("Montserrat", 12), width=195)
        insira_o_nome.place(x=170, y=370)

        #BOTAO DE DESLIGAR NO FRAME DE APPS
        frame_encerramento = ctk.CTkFrame(master=area_de_trabalho, width=1280, height=620, fg_color="black")

        encerrando = ctk.CTkLabel(master=frame_encerramento, text="Bye Bye" ,width=5, height=5,
        bg_color="transparent",fg_color=branco_cinza)

        desligando_label = ctk.CTkLabel(master=frame_encerramento, text="Encerrando",
        font=("Montserrat", 40), text_color="White", bg_color="black", fg_color="black")

        def encerramento():
            frame_apps.pack_forget()
            barra_de_tarefas.pack_forget()
            frame_encerramento.place(x=0, y=0)
            encerrando.place(x=360, y=230)
            desligando_label.place(x=580, y=280)
            tela.destroy()

        def off():
            encerramento()
            
            # time.sleep(3)

        power_off = ctk.CTkButton(master=frame_apps, text="", image=off_frame_apps ,width=5, height=5,
        hover=None, bg_color="transparent",fg_color=branco_cinza, command=off)
        power_off.place(x=360, y=365)

        #BOTAO TOGGLE FRAMES
        def Apps_frame():
            frame_apps.place(x=5000)
            windows_botao_bar.place(x=600 ,y=1)
            windows_botao_toggle.place(x=5000)
            home_indicate["bg_color"] = preto
            home_indicate._bg_color = preto

        windows_botao_toggle = ctk.CTkButton(master=barra_de_tarefas, image=windows_bar, text="",
        fg_color=cinza, hover_color="gray", bg_color=cinza, width=2, height=5, command=Apps_frame)
        
        # ICONES NA AREA DE TRABALHO
        lixeira = PhotoImage(file="fotos/programs/lixeira.png")
        xadrex = PhotoImage(file="fotos/programs/chess.png")

        # APP LIXIERA NA AREA DE TRABALHO
        lixeira_trabalho = ctk.CTkButton(master=area_de_trabalho, image=lixeira, text="",
        fg_color="transparent",bg_color=cor_area_de_trabalho, width=15, height=15, hover_color="gray",
        corner_radius=12, command= lambda: Lixeira.lixeira_app())
        lixeira_trabalho.place(x=17, y=17)

        lixeira_label = ctk.CTkLabel(master=area_de_trabalho, text="Lixeira",
        font=("Montserrat", 16), text_color="White", bg_color= cor_area_de_trabalho, fg_color=cor_area_de_trabalho )
        lixeira_label.place(x=27, y=69)

        # APP XADREZ NA AREA DE TRABALHO
        xadrez_trabalho = ctk.CTkButton(master=area_de_trabalho, image=xadrex, text="",
        fg_color="transparent",bg_color=cor_area_de_trabalho, width=15, height=15, hover_color="gray",
        corner_radius=12)
        xadrez_trabalho.place(x=17, y=103)

        xadrez_label = ctk.CTkLabel(master=area_de_trabalho, text="Xadrez\n"
                                                                   "Online\n",
        font=("Montserrat", 16), text_color="White", bg_color= cor_area_de_trabalho, fg_color=cor_area_de_trabalho )
        xadrez_label.place(x=27, y=160)

        # ICONES NA BARRA DE TAREFAS
        lupa_bar = PhotoImage(file="fotos/bar/lupa.png")
        pasta_bar = PhotoImage(file="fotos/bar/pasta.png")
        seta_bar = PhotoImage(file="fotos/bar/seta/seta.png")
        wifi_bar = PhotoImage(file="fotos/bar/seta/wifi.png")
        volume_bar = PhotoImage(file="fotos/bar/volume/volume_alto.png")
        bateria_bar = PhotoImage(file="fotos/bar//seta/bateria.png")

        # BOTAO WINDOWS NA BARRA DE TAREFAS
        windows_botao_bar = ctk.CTkButton(master=barra_de_tarefas, image=windows_bar, text="",
        fg_color=cinza, hover_color="gray", bg_color=cinza, width=2, height=5, command=Apps)
        windows_botao_bar.place(x=600 ,y=1)
        
        # BOTAO DE BUSCA NA BARRA DE TAREFAS
        lupa_botao_bar = ctk.CTkButton(master=barra_de_tarefas, image=lupa_bar, text="",
        fg_color=cinza, hover_color="gray", bg_color=cinza, width=2, height=5, command=Apps)
        lupa_botao_bar.place(x=640, y=1)

        # BOTAO EXPLORADOR DE ARQUIVOS NA BARRA DE TAREFAS
        pasta_botao_bar = ctk.CTkButton(master=barra_de_tarefas, image=pasta_bar, text="",
        fg_color=cinza, hover_color="gray", bg_color=cinza, width=2, height=5, command=Apps)
        pasta_botao_bar.place(x=680, y=1)

        #BOTAO SETA NA BARRA DE TAREFAS
        seta_botao_bar = ctk.CTkButton(master=barra_de_tarefas, image=seta_bar, text="",
        fg_color=cinza, hover_color="gray", bg_color=cinza, width=2, height=5)
        seta_botao_bar.place(x=1100, y=8)

        # BOTAO WIFI NA BARRA DE TAREFAS
        wifi_botao_bar = ctk.CTkButton(master=barra_de_tarefas, image=wifi_bar, text="",
        fg_color=cinza, hover_color="gray", bg_color=cinza, width=2, height=5)
        wifi_botao_bar.place(x=1130, y=5)

        # ICONE DA BATERIA BARRA DE TAREFAS
        bateria_botao_bar = ctk.CTkButton(master=barra_de_tarefas, image=bateria_bar, text="",
        fg_color=cinza, hover_color="gray", bg_color=cinza, width=2, height=5)
        bateria_botao_bar.place(x=1165, y=5)

        # BOTAO DE VOLUME NA BARRA DE TAREFAS
        volume_botao_bar = ctk.CTkButton(master=barra_de_tarefas, image=volume_bar, text="",
        fg_color=cinza, hover_color="gray", bg_color=cinza, width=2, height=5)
        volume_botao_bar.place(x=1200, y=5)

        #AREA DE TRABALHO
        def Home():
            titulo_HB.pack_forget()
            titulo_sobre.pack_forget()
            area_de_trabalho.place(x=0, y=0)
            fundo_area_de_trabalho.place(x=0, y=0)
            barra_de_tarefas.place(x=0, y=580)
            astro.pack_forget()
            frame_fundo.place(x=5000)
            # SALVA O NOME DE USUARIO
            nome = insira_o_nome.get()
            nome_user = ctk.CTkLabel(master=frame_apps,text=nome, text_color="black", font=("Montserrat", 12))
            nome_user.place(x=75, y=360)
        
        #BOTAO PARA INICIAR O SISTEMA
        play_botao_app = ctk.CTkButton(master=frame_fundo, image=foto_explorer, text="", fg_color="transparent",
        hover_color="gray", bg_color="transparent", hover=None,width=80, height=80, command=Home)

        #TEXTO HABA DA INTRODUCAO
        titulo_carregando = ctk.CTkLabel(tela, text="Carregando...", font=("Krona One", 25, "bold"),
        fg_color="transparent", bg_color="transparent", text_color="white")
        titulo_carregando.place(x=30, y= 530)

        def introducao():
            play_botao_inicia.place(x=5000)
            titulo_HB.place(x=5000)
            space_foto.place(x=5000)
            carregando_o_app.place(x=5000)
            astro.place(x=150, y= 50)
            frame_fundo.place(x=690, y= 50)
            play_botao_app.place(x=80, y=400)
            titulo_sobre.place(x=30, y= 530)
            titulo_carregando.place(x=5000)

        #BOTAO PRA INICIAR A INTRODUÇÃO
        foto_play = PhotoImage(file="fotos/entrada/play.png")
        play_botao_inicia = ctk.CTkButton(master=tela, image=foto_play, text="",fg_color="transparent",
        hover_color="gray", bg_color="transparent", hover=None,width=80, height=80, command=introducao)
        play_botao_inicia.place(x=620, y=460)

Application()
