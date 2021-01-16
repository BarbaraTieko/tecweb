from utils import load_data, load_template, load_episodes


def index():
    # Cria uma lista de <li>'s para cada série
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    serie_template = load_template('components/serie.html')
    series_li = [
        serie_template.format(title=dados['titulo'], slug=dados['slug'], image=dados['imagem'])
        for dados in load_data('series.json')
    ]
    series = '\n'.join(series_li)

    return load_template('index.html').format(series=series).encode()


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

            return load_template('details.html').format(title=serie['titulo'], image=serie['imagem'], episodes=episodes).encode()
    return bytes()
