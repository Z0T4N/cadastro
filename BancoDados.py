import sqlite3

class Con_des():
    def conecta_db(self):
        self.con =  sqlite3.connect('client.bd')
        self.cursor = self.con.cursor()

    def desconta_db(self):
        self.con.close()

class Tabela():
    def montaTabelas(self):
        self.conecta_db()
        self.cursor.execute(""" 
           CREATE TABLE IF NOT EXISTS clientes(
               cod INTEGER (3),
               nome_cliente CHAR(30) NOT NULL ,
               operador CHAR(40),
               material CHAR(15),
               peso INTEGER (5), 
               data CHAR(10),
               sequencia INTEGER (3),
               lote INTEGER (8)
    
    
           );
       """)
        self.con.commit();
        print("banco criado")
        self.desconta_db()

