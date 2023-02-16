import sqlite3

from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

class Database:
    def __init__(self, nome):
        self.conn = sqlite3.connect(nome+'.db')

        # um exemplo
        # cur = self.conn.cursor()
        # cur.execute("""CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY,
        #                                     title TEXT,
        #                                     content TEXT NOT NULL
        #
        #                                     );""")

        self.conn.execute("""CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY,
                                            title TEXT,
                                            content TEXT NOT NULL

                                            );""")
    def add(self, note):
        comando = f"INSERT INTO note (title, content) VALUES ('{note.title}','{note.content}');"
        self.conn.execute(comando)
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        notes = []
        for linha in cursor:
            note = Note()
            note.id= linha[0]
            note.title = linha[1]
            note.content = linha[2]
            notes.append(note)
        return notes

    def update(self, entry):
        comando = f"UPDATE note SET title = '{entry.title}', content='{entry.content}' WHERE id = {entry.id}"
        self.conn.execute(comando)
        self.conn.commit()
