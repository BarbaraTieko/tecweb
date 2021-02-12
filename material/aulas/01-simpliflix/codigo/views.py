from utils import load_data, load_template, load_episodes, build_response


def index():
    # Cria uma lista de <li>'s para cada série
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    serie_template = load_template('components/serie.html')
    series_li = [
        serie_template.format(title=dados['titulo'], slug=dados['slug'], image=dados['imagem'])
        for dados in load_data('series.json')
    ]
    series = '\n'.join(series_li)

    return build_response(load_template('index.html').format(series=series))


def login(request):
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        for chave_valor in corpo.split('&'):
            param = chave_valor.split('=')
            params[param[0]] = param[1]
        return build_response(code=303, reason='See Other', headers='Location: /')
    return build_response(load_template('login.html'))


def details(route):
    series = load_data('series.json')
    for serie in series:
        if serie['slug'] == route:
            episodes_template = load_template('components/episode.html')
            episodes_li = [
                episodes_template.format(title=dados['titulo'], thumbnail=dados['thumbnail'], description=dados['descricao'])
                for dados in load_episodes(serie['slug'], 'episodes.json')
            ]
            episodes = '\n'.join(episodes_li)

            return build_response(load_template('details.html').format(title=serie['titulo'], image=serie['imagem'], episodes=episodes))
    return build_response()
