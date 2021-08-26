import sqlite3
from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''
# class Note:
#     def __init__(self, id=None, title=None, content=''):
#         self.id = id
#         self.title = title
#         self.content = content


class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(f'{db_name}.db')
        self.conn.execute('CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title STRING, content STRING NOT NULL);')

    def add(self, note):
        self.conn.execute(f"INSERT INTO note (title,content) VALUES ('{note.title}','{note.content}');")
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute(f"SELECT id, title, content FROM note;")
        return [Note(*row) for row in cursor]

    def update(self, value):
        self.conn.execute(f"UPDATE note SET title = '{value.title}', content = '{value.content}' WHERE id = {value.id};")
        self.conn.commit()

    def delete(self, note_id):
        self.conn.execute(f"DELETE FROM note WHERE id = {note_id}")
        self.conn.commit()
