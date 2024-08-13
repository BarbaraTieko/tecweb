import unittest
import sqlite3
from unittest.mock import patch, create_autospec
from pathlib import Path
import database


DB_NAME = 'banco-teste'
DB_FILENAME = f'{DB_NAME}.db'
TABLE_NAME = 'note'


class DatabaseTestCase(unittest.TestCase):
    def setUp(self):
        self.marcador = '\n' + '*' * 50 + '\n'
        db_file = Path.cwd() / DB_FILENAME
        try:
            db_file.unlink()  # Apaga o arquivo, caso exista
        except FileNotFoundError:
            pass

    def error_message(self, msg):
        marker = '\033[91m'
        end_marker = '\033[0m'
        return f'\n{marker}{msg}{end_marker}\n'

    def verifica_se_a_classe_database_existe(self):
        try:
            db = database.Database(DB_NAME)
        except AttributeError:
            msg = self.error_message(f"{self.marcador}Algo deu errado! A classe Database não foi definida corretamente.{self.marcador}")
            assert False, msg

    def test_exercicio_01_connect_on_init(self):
        mock_connection = create_autospec(sqlite3.Connection)
        with patch('sqlite3.connect', return_value=mock_connection) as mock_connect:
            self.verifica_se_a_classe_database_existe()
            db = database.Database(DB_NAME)

            assert mock_connect.called, self.error_message(f'{self.marcador}A função sqlite3.connect não foi chamada.{self.marcador}')
            assert mock_connect.call_args[0][0] == DB_FILENAME, self.error_message(f'{self.marcador}Nome do banco incorreto. Deveria ser {DB_FILENAME}{self.marcador}')
            assert hasattr(db, 'conn'), self.error_message(f'{self.marcador}Não criou o atributo conn.{self.marcador}')
            assert db.conn is mock_connection, self.error_message(f'{self.marcador}Não armazenou a conexão no atributo conn.{self.marcador}')

    def test_exercicio_02_create_table_on_init(self):
        db_file = Path.cwd() / DB_FILENAME
        self.verifica_se_a_classe_database_existe()
        db = database.Database(DB_NAME)
        if not db_file.is_file():
            raise NotImplementedError(self.error_message(f'{self.marcador}A conexão com o banco não foi implementada ainda. Ignore se ainda não chegou neste exercício.{self.marcador}'))

        conn = sqlite3.connect(DB_FILENAME)
        cursor = conn.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{TABLE_NAME}';")
        assert len([row for row in cursor]) == 1, self.error_message(f'{self.marcador}A tabela {TABLE_NAME} não foi criada. Se você está no primeiro exercício, ignore este erro.{self.marcador}')

        cursor = conn.execute(f"PRAGMA table_info({TABLE_NAME});")
        found_count = 0
        for i, (_, name, coltype, notnull, _, pk) in enumerate(cursor):
            if i == 0:
                assert name == 'id', self.error_message('Para facilitar os testes, a primeira coluna deve obrigatoriamente ser a coluna id.')
                assert coltype == 'INTEGER', self.error_message('A coluna id deveria ser do tipo inteiro')
                assert pk, self.error_message('A coluna id deveria ser a chave primária')
            elif i == 1:
                assert name == 'title', self.error_message('Para facilitar os testes, a segunda coluna deve obrigatoriamente ser a coluna title.')
                assert coltype == 'STRING' or coltype == 'TEXT', self.error_message('A coluna title deveria ser do tipo texto')
                assert not notnull, self.error_message('A coluna title deveria poder ser vazia')
                assert not pk, self.error_message('A coluna title não deveria ser chave primária')
            elif i == 2:
                assert name == 'content', self.error_message('Para facilitar os testes, a terceira coluna deve obrigatoriamente ser a coluna content.')
                assert coltype == 'STRING' or coltype == 'TEXT', self.error_message('A coluna content deveria ser do tipo texto')
                assert notnull, self.error_message('A coluna content não deveria poder ser vazia')
                assert not pk, self.error_message('A coluna content não deveria ser chave primária')
            else:
                raise AssertionError(self.error_message(f'{self.marcador}Não deveria existir uma coluna chamada {name}.{self.marcador}'))
            found_count += 1

    def test_exercicio_03_add_rows(self):
        self.verifica_se_a_classe_database_existe()
        db = database.Database(DB_NAME)
        if not hasattr(db, 'add') or not hasattr(database, 'Note'):
            raise NotImplementedError(self.error_message(f'{self.marcador}Método add ou classe Note não foram implementadas ainda. Ignore se ainda não chegou no exercício 03.{self.marcador}'))

        data = [
            ('Pão doce', 'Abra o pão e coloque o seu suco em pó favorito.'),
            ('', 'Lembrar de tomar água'),
        ]
        try:
            for title, content in data:
                db.add(database.Note(title=title, content=content))
        except sqlite3.OperationalError:
            raise SyntaxError(self.error_message(f"{self.marcador}Algo deu errado! Veja se não esqueceu as aspas em torno dos valores.{self.marcador}"))

        conn = sqlite3.connect(DB_FILENAME)
        cursor = conn.execute(f"SELECT * FROM {TABLE_NAME}")
        result = [(title, content) for _, title, content in cursor]
        result.sort(key=lambda r: r[1])
        assert data == result, self.error_message(f'{self.marcador}Os dados não foram inseridos corretamente. Era esperado: {data}\nporém foi obtido {result}.{self.marcador}')

    def test_exercicio_04_select_rows(self):
        self.verifica_se_a_classe_database_existe()
        db = database.Database(DB_NAME)
        if not hasattr(db, 'add') or not hasattr(db, 'get_all') or not hasattr(database, 'Note'):
            raise NotImplementedError(self.error_message(f'{self.marcador}Método add ou get_all ou a classe Note não foram implementadas ainda. Ignore se ainda não chegou no exercício 04.{self.marcador}'))

        data = [
            database.Note(title='Hidratação', content='Lembrar de tomar água'),
            database.Note(title='Pão doce', content='Abra o pão e coloque o seu suco em pó favorito.'),
        ]
        for note in data:
            db.add(note)

        try:
            notes = sorted(db.get_all(), key=lambda n: n.title)
        except:
            raise Exception(self.error_message(f"{self.marcador}Verifique se o método get_all está retornando uma lista de Note.{self.marcador}"))

        assert isinstance(notes, list), self.error_message(f'{self.marcador}O método get_all deveria devolver uma lista. Obtido: {notes}{self.marcador}')
        assert len(data) == len(notes), self.error_message(f'{self.marcador}A lista devolvida tem uma quantidade de elementos diferente do esperado. Esperado: {len(data)}. Obtido: {len(notes)}.{self.marcador}')
        assert all(n.id != None for n in notes), self.error_message(f'{self.marcador}As notas estão sem a informação do id.{self.marcador}')
        assert all(d.title == n.title and d.content == n.content for d, n in zip(data, notes)), self.error_message(f'{self.marcador}A lista de anotações é diferente da esperada. Esperada: {data}. Obtida: {notes}.{self.marcador}')

    def test_exercicio_05_update_row(self):
        self.verifica_se_a_classe_database_existe()
        db = database.Database(DB_NAME)
        if not hasattr(db, 'add') or not hasattr(db, 'get_all') or not hasattr(db, 'update') or not hasattr(database, 'Note'):
            raise NotImplementedError(self.error_message(f'{self.marcador}Método add, get_all ou update ou a classe Note não foram implementadas ainda. Ignore se ainda não chegou no exercício 05.{self.marcador}'))

        data = [
            database.Note(title='Hidratação', content='Lembrar de tomar água'),
            database.Note(title='Pão doce', content='Abra o pão e coloque o seu suco em pó favorito.'),
        ]
        for note in data:
            db.add(note)

        notes = sorted(db.get_all(), key=lambda n: n.title)
        new_title = 'Zebra'
        new_content = 'É um animal que começa com a letra Z.'
        updated_row = notes[1]
        updated_row.title = new_title
        updated_row.content = new_content

        try:
            db.update(updated_row)
        except sqlite3.OperationalError:
            raise SyntaxError(self.error_message(f"{self.marcador}Algo deu errado! Veja se não esqueceu as aspas em torno dos valores.{self.marcador}"))

        notes = sorted(db.get_all(), key=lambda n: n.title)


        data[1].title = new_title
        data[1].content = new_content
        assert isinstance(notes, list), self.error_message(f'{self.marcador}O método get_all deveria devolver uma lista. Obtido: {notes}{self.marcador}')
        assert len(data) == len(notes), self.error_message(f'{self.marcador}A lista devolvida tem uma quantidade de elementos diferente do esperado. Esperado: {len(data)}. Obtido: {len(notes)}.{self.marcador}')
        assert all(d.title == n.title and d.content == n.content for d, n in zip(data, notes)), self.error_message(f'{self.marcador}A lista de anotações é diferente da esperada. Esperada: {data}. Obtida: {notes}.{self.marcador}')

    def test_exercicio_06_delete_row(self):
        self.verifica_se_a_classe_database_existe()
        db = database.Database(DB_NAME)
        if not hasattr(db, 'add') or not hasattr(db, 'get_all') or not hasattr(db, 'delete') or not hasattr(database, 'Note'):
            raise NotImplementedError(self.error_message(f'{self.marcador}Método add, get_all ou delete ou a classe Note não foram implementadas ainda. Ignore se ainda não chegou no exercício 06.{self.marcador}'))

        data = [
            database.Note(title='Hidratação', content='Lembrar de tomar água'),
            database.Note(title='Pão doce', content='Abra o pão e coloque o seu suco em pó favorito.'),
        ]
        for note in data:
            db.add(note)

        db.delete(1)
        notes = sorted(db.get_all(), key=lambda n: n.title)
        assert isinstance(notes, list), self.error_message(f'{self.marcador}O método get_all deveria devolver uma lista. Obtido: {notes}{self.marcador}')
        assert len(notes) == 1, self.error_message(f'{self.marcador}A lista devolvida deveria ter apenas 1 elemento. Obtido: {len(notes)}.{self.marcador}')
        note = notes[0]
        assert data[1].title == note.title and data[1].content == note.content, self.error_message(f'{self.marcador}Foi removido o elemento errado.{self.marcador}')

if __name__ == '__main__':
    unittest.main()
