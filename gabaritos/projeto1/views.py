from urllib.parse import unquote_plus
from utils import load_data, load_template, save_note, build_response
from database import Note

def index(request):
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            result = unquote_plus(chave_valor).split("=")
            params[result[0]] = result[1]

        note = Note()
        note.title = params['titulo']
        note.content = params['detalhes']
        print("*"*50)
        print(params)

        save_note(note)
        return build_response(code=303, reason='See Other', headers='Location: /')
            # AQUI É COM VOCÊ
    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=note.title, details=note.content)
        for note in load_data()
    ]
    notes = '\n'.join(notes_li)

    return build_response() + load_template('index.html').format(notes=notes).encode()
