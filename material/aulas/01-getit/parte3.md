# 01 - Get-it

## Parte 3: Separando algumas responsabilidades

O nosso código já está ficando grande e ele não faz quase nada! Um dos motivos para isso é a falta de coesão desse arquivo (lembra de Ágil?): esse arquivo possui a string HTML da página, que por sua vez contém todos os dados das anotações disponíveis, além do código que trata as conexões, requisições e respostas. Imagine o que aconteceria com uma quantidade razoável de anotações!

Essas três responsabilidades acumuladas no mesmo arquivo estão relacionadas a um conceito chamado <b>M</b>odel, <b>V</b>iew, <b>C</b>ontroller (MVC). Vocês tiveram um breve contato com esse conceito em Desenvolvimento Colaborativo Ágil, mas nós discutiremos mais a respeito em um futuro próximo.

### Modelo

Vamos começar separando a responsabilidade do modelo (lista de anotações) da responsabilidade de visualização (string HTML). Para isso, vamos criar uma lista de dicionários que contém os dados das anotações e a string HTML será gerada dinamicamente a partir desses dados:

```python hl_lines="3 9-13 28-30 54-62"
--8<-- "01-getit/codigo/passo8.py"
```

Você também vai precisar do arquivo [`notes.json` (clique aqui para baixar)](../codigo/data/notes.json). Coloque-o em uma pasta chamada `data`:

```
- DIRETORIO-DO-SEU-SERVIDOR
  |- servidor.py
  |- utils.py
  |- test_utils.py
  |- data
     |- notes.json
  |- img
     |- logo-getit.png
```

!!! example "EXERCÍCIO"
    Implemente a função `#!python load_data`, que recebe o caminho de um arquivo JSON e devolve o conteúdo do arquivo com esse nome **dentro da pasta `data`** carregado como um objeto Python. Por exemplo: se o conteúdo do arquivo `data/dados.json` for a string `{"chave": "valor"}`, sua função deve devolver o dicionário Python `#!python {"chave": "valor"}` para a entrada `dados.json` (note que o nome da pasta não é enviado como argumento). Dica: já existe uma [função Python para isso](https://docs.python.org/3/library/json.html) (e você viu em Design de Software).

### Visualização

Ufa, já está um pouco melhor. Se quisermos adicionar mais anotações basta modificar o arquivo `notes.json`. Lembra da ideia de mantermos um baixo acoplamento? Aqui nós conseguimos melhorar esse ponto. Se eu quero adicionar mais dados eu só modifico o arquivo de dados (`notes.json`) e nenhum outro. O resto do código é independente disso.

Mas ainda dá para melhorar. Vamos refatorar um pouco mais o nosso código, separando a responsabilidade de visualização (HTML). Para isso, crie uma pasta chamada `templates` e crie dentro dela um arquivo `index.html` com o conteúdo da string `#!python RESPONSE_TEMPLATE` a partir da terceira linha, inclusive, ou seja, a partir de `<!DOCTYPE html>`. Ainda dentro da pasta `templates`, crie outra pasta chamada `components` e dentro dessa nova pasta um arquivo `note.html` com o conteúdo da string `#!python NOTE_TEMPLATE`. A sua estrutura de arquivos agora deve ser:

```
- DIRETORIO-DO-SEU-SERVIDOR
  |- servidor.py
  |- utils.py
  |- test_utils.py
  |- data
     |- notes.json
  |- img
     |- logo-getit.png
  |- templates
     |- index.html
     |- components
        |- note.html
```

!!! example "EXERCÍCIO"
    Implemente a função `#!python load_template` que recebe o nome de um arquivo de template e devolve uma string com o conteúdo desse arquivo. O nome do arquivo não inclui o nome da pasta `templates`. Por exemplo: para a entrada `index.html` você deve carregar o conteúdo do arquivo `templates/index.html`.

Vamos atualizar o código do servidor:

```python hl_lines="3 25 29 31 36 37"
--8<-- "01-getit/codigo/passo9.py"
```

### Controle de rotas

O código do servidor ainda possui duas responsabilidades diferentes: decidir qual rota seguir e o que fazer em cada rota (o que pode ser tão complexo quanto se queira). Vamos separar a responsabilidade de cada rota em uma função diferente:

```python hl_lines="3 4 28-31"
--8<-- "01-getit/codigo/passo10.py"
```

Você também vai precisar criar o arquivo `views.py` com o seguinte conteúdo (note que é exatamente o mesmo código que estava no `#!python else`):

```python
from utils import load_data, load_template

def index():
    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes).encode()
```

Agora o nosso código está pronto para a [parte 4 do handout!](parte4.md)
