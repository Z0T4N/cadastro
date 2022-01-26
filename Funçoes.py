from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from BancoDados import Con_des

class Relatorio():
    pass

class Erros():

    def extrusora(self):
        self.extru1 = self.extru_01.get()
        self.extru2 = self.extru_02.get()

    def variaveis(self):
        try:
            self.cod = int(self.ed_cod.get())
            self.cliente = str(self.ed_nome_cliente.get())
            self.nome = str(self.ed_nome.get())
            self.data = self.ed_data.get()
            self.seq = int(self.ed_seq.get())
            self.lote = int(self.ed_lote.get())
            self.peso = int(self.ed_peso.get())

        except ValueError:
            try:
                self.cliente = str(self.ed_nome_cliente.get())
                self.nome = str(self.ed_nome.get())
                self.mat = str(self.combo_mat.get())
                self.data = str(self.ed_data.get())
                if (self.cod or self.seq or self.data == str):
                    messagebox.showerror('Erro 01', 'campos:\ncodigo, sequencia e lote\nNão aceitão caracteres ')

            except AttributeError:
                messagebox.showerror('Erro 02', 'campo vazio')

class Func_Botoes(Con_des,Erros):
    def limpa_tela(self):
        self.ed_cod.delete(0, END)
        self.ed_nome_cliente.delete(0, END)
        self.ed_peso.delete(0, END)
        self.combo_mat.delete(0, END)
        self.ed_nome.delete(0, END)
        self.ed_data.delete(0, END)
        self.ed_seq.delete(0, END)
        self.ed_lote.delete(0, END)


    def add_cliente(self):
        self.variaveis()
        try:
            self.cursor.execute(""" INSERT INTO clientes (cod, nome_cliente, operador, material, peso, data, sequencia, lote)
                   VALUES ( ?, ?, ?, ?, ?, ?, ?, ? )""", (self.cod, self.cliente, self.nome, self.mat, self.peso,
                                                          self.data, self.seq, self.lote))
        except AttributeError:
            pass

        self.con.commit()
        self.desconta_db()
        self.select_list()


    def select_list(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_db()
        lista = self.cursor.execute("""SELECT cod, nome_cliente, operador, material, peso, data, sequencia, lote
        FROM clientes ORDER BY cod, data, sequencia ASC""")
        for i in lista:
            self.listaCli.insert("", END, values=i)


    def duplo_click(self, event):
           self.limpa_tela()
           self.listaCli.selection()

           for n in self.listaCli.selection():
               col1, col2, col3, col4, col5,col6,col7,col8 = self.listaCli.item(n, 'values')
               self.ed_cod.insert(END, col1)
               self.ed_nome_cliente.insert(END, col2)
               self.ed_nome.insert(END, col3)
               self.ed_data.insert(END, col4)
               self.ed_seq.insert(END, col5)
               self.ed_lote.insert(END, col6)

               self.combo_mat.insert(END, col4)
               self.ed_peso.insert(END, col5)
               self.ed_data.insert(END, col6)
               self.ed_seq.insert(END, col7)
               self.ed_lote.insert(END, col8)


    def delete_cliente(self):
           self.variaveis()
           self.conecta_db()
           self.cursor.execute(""" DELETE FROM clientes
            WHERE sequencia = ? AND data = ?  AND cod = ? AND material = ?""",
                               (self.seq, self.data,self.cod,self.mat))
           self.con.commit()
           self.desconta_db()
           self.limpa_tela()
           self.select_list()


    def altera_cliente(self):
           self.variaveis()
           self.conecta_db()
           self.cursor.execute(""" UPDATE  clientes SET cod = ?, nome_cliente = ?, operador = ?, material = ?, peso = ?, data = ?,lote = ?
                                       WHERE sequencia = ?  """,
           (self.cod, self.cliente, self.nome, self.mat, self.peso, self.data, self.lote, self.seq))
           self.con.commit()
           self.desconta_db()
           self.select_list()
           self.limpa_tela()


    def buscar_cliente(self):
        self.conecta_db()
        self.listaCli.delete(*self.listaCli.get_children())

        self.ed_cod.insert(END, '%')
        cod = self.ed_cod.get()

        self.cursor.execute("""SELECT cod, nome_cliente, operador, material, peso, data, sequencia, lote
        FROM clientes WHERE cod LIKE '%s' ORDER BY data, sequencia ASC """ % cod)

        buscarcodCli = self.cursor.fechall()
        for i in buscarcodCli:
               self.listaCli.insert("", END, values=i)
        self.limpa_tela()

        self.desconta_db()


    def lista_frame_2(self):
        self.listaCli = ttk.Treeview(self.aba1, height=2, columns=("col0", "col1", "col2", "col3", "col4",
                                                                   "col5", "col6", "col7"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="codigo", )
        self.listaCli.heading("#1", text="codigo")
        self.listaCli.heading("#2", text="cliente")
        self.listaCli.heading("#3", text="operador")
        self.listaCli.heading("#4", text="data")
        self.listaCli.heading("#5", text="sequencia")
        self.listaCli.heading("#6", text="lote")
        self.listaCli.heading("#4", text="material")
        self.listaCli.heading("#5", text="peso")
        self.listaCli.heading("#6", text="data")
        self.listaCli.heading("#7", text="sequencia")
        self.listaCli.heading("#8", text="lote")

        self.listaCli.column("#0", width=1, stretch=False)
        self.listaCli.column("#1", width=20, stretch=True)
        self.listaCli.column("#2", width=50, stretch=True)
        self.listaCli.column("#3", width=125, stretch=True)
        self.listaCli.column("#4", width=50, stretch=True)
        self.listaCli.column("#5", width=20, stretch=True)
        self.listaCli.column("#6", width=25, stretch=True)
        self.listaCli.column("#7", width=25, stretch=True)
        self.listaCli.column("#8", width=20, stretch=True)

        self.listaCli.column("#1", anchor=CENTER)
        self.listaCli.column("#2", anchor=CENTER)
        self.listaCli.column("#3", anchor=CENTER)
        self.listaCli.column("#4", anchor=CENTER)
        self.listaCli.column("#5", anchor=CENTER)
        self.listaCli.column("#6", anchor=CENTER)
        self.listaCli.column("#7", anchor=CENTER)
        self.listaCli.column("#8", anchor=CENTER)

        self.listaCli.place(relx=0.005, rely=0.468, relwidth=0.978, relheight=0.54)

        self.scroollista = Scrollbar(self.aba1, orient=VERTICAL)
        self.listaCli.configure(yscroll=self.scroollista.set)
        self.scroollista.place(relx=0.985, rely=0.468, relwidth=0.012, relheight=0.52)

        self.scroollistaH = Scrollbar(self.aba1, orient=HORIZONTAL)
        self.listaCli.configure(xscroll=self.scroollistaH.set)
        self.scroollistaH.place(relx=0.005, rely=0.97, relwidth=0.978, relheight=0.02)

        self.listaCli.bind("<Double-1>", self.duplo_click)





