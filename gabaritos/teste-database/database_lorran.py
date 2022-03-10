from operator import contains
import sqlite3
from dataclasses import dataclass
from turtle import title
from unicodedata import name

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''


class Database():
    def __init__(self, name):
        self.conn = sqlite3.connect(name+".db")
        self.note = self.conn.execute('''CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY,
                                                        title TEXT,
                                                        content TEXT NOT NULL);''')
    def add(self, note):
        # print(f"INSERT INTO note (title, content) VALUES ('{note.title}','{note.content}');")
        self.conn.execute(f"INSERT INTO note (title, content) VALUES ('{note.title}','{note.content}');")
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute("SELECT * FROM note")
        myresult = cursor.fetchall()

        notes = []
        for linha in myresult:
            id = linha[0]
            title = linha[1]
            content = linha[2]

            # get_all = verificar id no objeto note
            notes.append(Note(id=id,title=title,content=content))

        return notes

    def update(self,entry):
        teste = f"UPDATE note SET title = '{entry.title}', content = '{entry.content}' WHERE id = {entry.id}"
        print("-------------------------")
        print("\n\n\n")
        print(teste)
        self.conn.execute(teste)
                           #UPDATE dados_pessoais SET cpf = '555.555.555-55' WHERE identificador = 2
        self.conn.commit()

    def delete(self, note_id):
        # 'DELETE FROM NOME_DA_TABELA WHERE CONDICAO;'
        self.conn.execute(f"DELETE FROM note WHERE id = {note_id}")
        self.conn.commit()
