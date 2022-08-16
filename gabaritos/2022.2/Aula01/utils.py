from pathlib import Path
import json
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