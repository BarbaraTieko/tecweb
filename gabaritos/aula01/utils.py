import json
from pathlib import Path

def extract_route(requisicao):
    return requisicao.split()[1][1:]

def read_file(filepath):
    # with open(path, "r+b") as arquivo:
    #     content = arquivo.read()
    # return content
    if filepath.suffix in ['.txt', '.html', '.css', '.js']:
        mode = 'r'
    else:
        mode = 'rb'

    with open(filepath, mode=mode) as f:
        return f.read()

def load_data(file_name):
    with open(f"data/{file_name}", "r", encoding="utf-8") as file:
    # with open(Path(__file__).parent.resolve() /"data"/file_name, "r", encoding="utf-8") as file:

        content = file.read()
    return json.loads(content)

def load_template(file_name):
    # with open(f"templates/{file_name}", encoding="utf-8") as file:
    with open(Path(__file__).parent.resolve() / "templates"/file_name, encoding="utf-8") as file:
        content = file.read()
    return content

def save_note(note):
    with open("data/notes.json", "r", encoding="utf-8") as file:
        content = file.read()

    dicio = json.loads(content)
    dicio.append(note)

    text = json.dumps(dicio, indent=4, ensure_ascii=False)

    with open("data/notes.json", "w", encoding="utf-8") as file:
        file.write(text)

def build_response(body="", code=200, reason="OK", headers=""):
    if headers:
        headers = '\n' + headers
    return f'HTTP/1.1 {code} {reason}{headers}\n\n{body}'.encode()
