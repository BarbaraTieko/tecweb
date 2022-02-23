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

        #test_create_table_on_init
        create = '''
        CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY,
                                          title TEXT,
                                          content TEXT NOT NULL
                                          );
        '''
        self.conn.execute(create)

    def add(self, note):
        insert = f'INSERT INTO note (title, content) VALUES ("{note.title}", "{note.content}"); '
        self.conn.execute(insert)
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute("select id, title, content from note")
        notes = []

        for item in cursor:
            note = Note(item[0], item[1], item[2])
            notes.append(note)
        return notes

    def update(self, entry):
        update = f'''
        UPDATE note SET title = "{entry.title}", content = "{entry.content}" WHERE id = "{entry.id}"
        '''
        self.conn.execute(update)
        self.conn.commit()

    def delete(self, note_id):
        self.conn.execute(f"DELETE FROM note WHERE id = {note_id}")
        self.conn.commit()
