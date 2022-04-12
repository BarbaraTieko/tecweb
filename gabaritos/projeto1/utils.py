import json
from pathlib import Path
from database import Database


def extract_route(requisicao):
    return requisicao.split()[1][1:]

def read_file(filepath):
    with open(filepath, mode='rb') as f:
        return f.read()

def load_data():
    db = Database('banco')
    return db.get_all()

def load_template(file_name):
    with open(f"templates/{file_name}", encoding="utf-8") as file:
    # with open(Path(__file__).parent.resolve() / "templates"/file_name, encoding="utf-8") as file:
        content = file.read()
    return content

def save_note(note):
    db = Database('banco')
    db.add(note)

def build_response(body="", code=200, reason="OK", headers=""):
    if headers:
        headers = '\n' + headers
    return f'HTTP/1.1 {code} {reason}{headers}\n\n{body}'.encode()
