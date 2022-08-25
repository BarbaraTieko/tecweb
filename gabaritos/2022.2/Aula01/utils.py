from pathlib import Path
import json
from urllib import response
CUR_DIR = Path(__file__).parent

def extract_route(request):
    return request.split()[1][1:]

def read_file(arquivo):
    with open(arquivo, 'rb') as file:
        conteudo = file.read()
        return conteudo

def load_data(arquivo):
    # filename = Path() / 'data' / arquivo
    filename = CUR_DIR  /'data'/ arquivo
    with open(filename, 'r') as file:
        dicionario = json.load(file)
    return dicionario

def load_template(arquivo):
    # filename = Path() / 'templates' / arquivo
    filename = CUR_DIR / 'templates' / arquivo
    with open(filename, 'r') as file:
        conteudo = file.read()
    return conteudo

def save_note(params):
    notas = load_data("notes.json")
    notas.append(params)

    with open("data/notes.json", "w", encoding="utf8") as arquivo:
        json.dump(notas, arquivo, ensure_ascii=False, indent=4)

def build_response(body='', code=200, reason='OK', headers=''):
    if headers == "":
        response = f"HTTP/1.1 {code} {reason}\n\n{body}"
    else: 
        response = f"HTTP/1.1 {code} {reason}\n{headers}\n\n{body}"

    return response.encode()