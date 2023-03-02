import sqlite3
from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

class Database:
    def __init__(self, nome_db):
        self.conn = sqlite3.connect(f"{nome_db}.db")

        create = '''
        CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY,
                                          title TEXT,
                                          content TEXT NOT NULL
                                          );
        '''
        self.conn.execute(create)


    def get(self, id):
        cursor = self.conn.execute(f"select id, title, content from note where id ={id}")
        linha = cursor.fetchone()
        note = Note(linha[0], linha[1], linha[2])
        return note
