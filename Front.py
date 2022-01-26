from tkinter import *
from tkinter import ttk

from Funçoes import *

from BancoDados import Tabela




root = Tk()

class Telas():
    def tela(self):
        self.root.title('LOGIN')
        self.root.configure(background='#207293')
        self.root.geometry('1000x700')
        self.root.state('zoomed')
        self.root.resizable(True, True)

        self.root.minsize(width=400, height=300)

        self.root.geometry('1100x650+0+1')

    def frames_da_tela(self):
        # primeiro frame

        self.frames_1 = Frame(self.root, bd=3, highlightbackground='#CBEAF9', bg='#992055')
        self.frames_1.place(relx=0.01, rely=0.01, relheight=0.5, relwidth=0.98)
        self.abas = ttk.Notebook(self.root)
        self.abas.place(x=0, y=0, relwidth=1, relheight=1)

        # segundo frame

        self.aba1 = Frame(self.abas)
        self.aba1.place(relx=0.01, rely=0.01, relheight=0.47, relwidth=0.98)
        self.aba1.configure(highlightbackground='#CBEAF9', bg='#992055')

        self.aba2 = Frame(self.abas)
        self.aba2.place(relx=0.01, rely=0.52, relheight=0.47, relwidth=0.98)
        self.aba2.configure(highlightbackground='#CBEAF9', bg='#992055')

        self.abas.add(self.aba1, text='cliente')
        self.abas.add(self.aba2, text='dados')


class Botaoes(Telas):
    def botaoes(self):
        # BOTAO APAGAR
        self.bt_apagar = Button(self.aba1, text='APAGAR', font='verdona-bold 8',
                        bg='#1b7c83', fg='#93f7b3', command=self.delete_cliente)
        self.bt_apagar.place(rely=0.04, relx=0.31, relwidth=0.1, relheight=0.04)

        # BOTAO BUSCAR
        self.bt_buscar = Button(self.aba1, text='BUSCAR', font='arial 8',
                    bg='#1b7c83', fg='#93f7b3', command=self.buscar_cliente)
        self.bt_buscar.place(rely=0.04, relx=0.42, relwidth=0.1, relheight=0.04)

        # BOTAO LIMPAR
        self.bt_limpar = Button(self.aba1, text='LIMPAR', font='arial 8',
                bg='#1b7c83', fg='#93f7b3', command=self.limpa_tela)
        self.bt_limpar.place(rely=0.04, relx=0.7, relwidth=0.1, relheight=0.04)

        # BOTAO NOVO
        self.bt_new = Button(self.aba1, text='ADICIONAR', font='arial 8',
                     highlightcolor='#93f7b3', bg='#1b7c83', fg='#93f7b3',command=self.add_cliente)
        self.bt_new.place(rely=0.04, relx=0.8, relwidth=0.1, relheight=0.04)

        # BOTAO ALTERAR
        self.bt_alterar = Button(self.aba1, text='ALTERAR', font='arial 8',
                        bg='#1b7c83', fg='#93f7b3', command=self.altera_cliente)
        self.bt_alterar.place(rely=0.04, relx=0.9, relwidth=0.1, relheight=0.04)

    def botao_menus(self):
        # CONFIGURAÇÃO DO MATERIAL
        self.lb_mat = Label(self.aba1, text=' MATERIAL', font='verdona-bold 10',
                                bg='#992055', fg='#93f7b3')
        self.lb_mat.place(relx=0.01, rely=0.3, relheight=0.04, relwidth=0.07)

        self.combo_mat = ttk.Combobox(self.aba1, values=[
            ['PE'],
            ['PP'],
            ['PET'],
            ['PS']
            ], state='readonly')
        self.combo_mat.grid(column=0, row=1)
        self.combo_mat.set("")
        self.combo_mat.place(relx=0.075, rely=0.301, relheight=0.04, relwidth=0.05)


            # ADICIONA O MENU DO MOINHO
        self.moinho = Menubutton(self.aba1, text='MOINHO', relief=RAISED, bg='#992055', fg='#93f7b3')
        self.moinho.place(relx=0.21, rely=0.305, relheight=0.04, relwidth=0.07)
        self.moinho.menu = Menu(self.moinho, tearoff=0)
        self.moinho['menu'] = self.moinho.menu

        moinho_0 = None
        moinho_01 = IntVar()
        moinho_02 = IntVar()
        moinho_03 = IntVar()
        moinho_04 = IntVar()

        self.moinho.menu.add_checkbutton(label=['01'], variable=moinho_01)
        self.moinho.menu.add_checkbutton(label=['02'], variable=moinho_02)
        self.moinho.menu.add_checkbutton(label=['03'], variable=moinho_03)
        self.moinho.menu.add_checkbutton(label=['04'], variable=moinho_04)
        self.moinho.menu.add_checkbutton(label=['NULO'], variable=moinho_0)

        # ADICIONA O MENU DO MICRO
        self.micro = Menubutton(self.aba1, text='MICRO', relief=RAISED, bg='#992055', fg='#93f7b3')
        self.micro.place(relx=0.28, rely=0.305, relheight=0.04, relwidth=0.07)
        self.micro.menu = Menu(self.micro, tearoff=0)
        self.micro['menu'] = self.micro.menu

        self.micro_0 = None
        self.micro_01 = IntVar()
        self.micro_02 = IntVar()
        self.micro_03 = IntVar()
        self.micro_04 = IntVar()

        self.micro.menu.add_checkbutton(label=['01'], variable=self.micro_01)
        self.micro.menu.add_checkbutton(label=['02'], variable=self.micro_02)
        self.micro.menu.add_checkbutton(label=['03'], variable=self.micro_03)
        self.micro.menu.add_checkbutton(label=['04'], variable=self.micro_04)
        self.micro.menu.add_checkbutton(label=['NULO'], variable=self.micro_0)


        # ADICIONA O MENU DO EXTRUSORA
        self.extru_01 = StringVar()
        self.extru_02 = StringVar()

        self.extru = Menubutton(self.aba1, text='EXTRUSORA', relief=RAISED, bg='#992055', fg='#93f7b3')
        self.extru.place(relx=0.35, rely=0.305, relheight=0.04, relwidth=0.08)
        self.extru.menu = Menu(self.extru, tearoff=0)
        self.extru['menu'] = self.extru.menu

        extru_0 = None
        extru_01 = IntVar()
        extru_02 = IntVar()
        self.extru.menu.add_checkbutton(label=['01'], variable=self.extru_01,

                                        onvalue='extrusora 1', offvalue='')
        self.extru.menu.add_checkbutton(label=['02'], variable=self.extru_02,

                                        onvalue='extrusora 2')

        self.extru.menu.add_checkbutton(label=['01'], variable=extru_01)
        self.extru.menu.add_checkbutton(label=['02'], variable=extru_02)

    def menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)

        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)
        filemenu = Menu(self.menubar)
        filemenu2 = Menu(self.menubar)

        def Quit():
            self.root.destroy()

        menubar.add_cascade(label='opcao', menu=filemenu)
        menubar.add_cascade(label='relatorio', menu=filemenu2)
        self.menubar.add_cascade(label='opcao', menu=filemenu)
        self.menubar.add_cascade(label='relatorio', menu=filemenu2)

        filemenu.add_command(label='sair', command=Quit)
        filemenu.add_command(label='produção')
        filemenu.add_command(label='cliente')
        filemenu.add_command(label='sair' )
        filemenu2.add_command(label='relatorio')


class Lb_Ed(Telas):
    def entradas(self):
        # CONFIGURAÇÔA DA ENTRADA COD
        self.lb_cod = Label(self.aba1, text='CODIGO', font='verdona-bold 9',
                                            bg='#992055', fg='#93f7b3')
        self.lb_cod.place(relx=0.01, rely=0.04, relheight=0.04, relwidth=0.05)

        self.ed_cod = Entry(self.aba1, font='arial 10',
                          bg='#f7dff0', fg='#000000')

        self.ed_cod.place(relx=0.07, rely=0.04, relwidth=0.05, relheight=0.03)

        # CONFIGURAÇÔA DA ENTRADA NOME CLIENTE
        self.lb_nome_cliente = Label(self.aba1, text='CLIENTE', font='verdona-bold 10',
                                                                  bg='#992055', fg='#93f7b3')
        self.lb_nome_cliente.place(relx=0.13, rely=0.04, relheight=0.04, relwidth=0.06)

        self.ed_nome_cliente = Entry(self.aba1, font='arial 10', state='normal',
                                                                  bg='#f7dff0', fg='#000000')
        self.ed_nome_cliente.place(relx=0.19, rely=0.042, relwidth=0.1, relheight=0.03)

        # CONFIGURAÇÔA DA ENTRADA NOME
        self.lb_nome = Label(self.aba1, text='OPERADOR', font='verdona-bold 10',
                                                  bg='#992055', fg='#93f7b3')
        self.lb_nome.place(relx=0.01, rely=0.13, relheight=0.04, relwidth=0.07)

        self.ed_nome = Entry(self.aba1, font='arial 10',
                                                  bg='#f7dff0', fg='#000000')
        self.ed_nome.place(relx=0.083, rely=0.13, relwidth=0.4, relheight=0.04)

        # CONFIGURAÇÔA DA ENTRADA DATA
        self.lb_data = Label(self.aba1, text='DATA', font='verdona-bold 9',
                                                  bg='#992055', fg='#93f7b3')

        self.lb_data.place(relx=0.67, rely=0.129, relheight=0.04, relwidth=0.04)

        self.ed_data = Entry(self.aba1, font='arial 10',
                                                  bg='#f7dff0', fg='#000000')
        self.ed_data.place(relx=0.71, rely=0.132, relwidth=0.1, relheight=0.03)

        # CONFIGURAÇÔA DA ENTRADA SEQUENCIA
        self.lb_seq = Label(self.aba1, text='SEQUENCIA',
                                                font='verdona-bold 10', bg='#992055', fg='#93f7b3')
        self.lb_seq.place(relx=0.18, rely=0.22, relheight=0.03, relwidth=0.08)

        self.ed_seq = Entry(self.aba1, font='verona-bold 10',
                                                bg='#f7dff0', fg='#000000')
        self.ed_seq.place(relx=0.255, rely=0.22, relwidth=0.07, relheight=0.03)

        # CONFIGURAÇÔA DA ENTRADA LOTE
        self.lb_lote = Label(self.aba1, text='LOTE',
                      font='verdona-bold 10', bg='#992055', fg='#93f7b3')
        self.lb_lote.place(relx=0.34, rely=0.22, relheight=0.03, relwidth=0.07)

        self.ed_lote = Entry(self.aba1, font='verdona-bold 10',
                                                  bg='#f7dff0', fg='#000000')
        self.ed_lote.place(relx=0.4, rely=0.22, relwidth=0.1, relheight=0.03)

        # LABEL DAS MAQUINAS
        self.lb_maq = Label(self.aba1, text='MAQUINAS', bg='#992055', fg='#93f7b3')
        self.lb_maq.place(relx=0.14, rely=0.3, relwidth=0.07, relheight=0.05)

        # CONFIGURAÇÔA DA ENTRADA PESO
        self.lb_peso = Label(self.aba1, text='PESO',
               font='verdona-bold 10', bg='#992055', fg='#93f7b3')
        self.lb_peso.place(relx=0.01, rely=0.22, relheight=0.03, relwidth=0.05)

        self.ed_peso = Entry(self.aba1, font='verona-bold 10',
                                                  bg='#f7dff0', fg='#000000')
        self.ed_peso.place(relx=0.075, rely=0.22, relwidth=0.08, relheight=0.03)



class Chamadas(Botaoes,Lb_Ed,Func_Botoes,Tabela):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.botaoes()
        self.entradas()
        self.botao_menus()
        self.lista_frame_2()
        self.montaTabelas()
        self.select_list()
        self.menu()
        root.mainloop()

Chamadas()




