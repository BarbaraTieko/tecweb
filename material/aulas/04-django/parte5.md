# Parte 5: Usando templates

Atualmente a nossa página inicial mostra apenas um texto no navegador. O nosso objetivo nesta parte do handout é mostrar a lista de anotações, assim como fizemos no [Handout 1](../01-getit.md).

Já vimos no primeiro handout que não é uma boa ideia criarmos uma string com todo o HTML dentro do código Python. A nossa vida será muito mais fácil se mantivermos as responsabilidades separadas. Por esse motivo, vamos pular diretamente para o uso de templates no Django.

!!! example "Exercício"
    Crie as pastas `notes/templates/notes` (sim, o `notes` é repetido mesmo) e então crie os dois arquivos a seguir

    === "notes/templates/notes/base.html"
        ```html
        <!DOCTYPE html>
        <html>
          <head>
            <meta charset="UTF-8" />
            <title>Get-it</title>
          </head>

          <body>
            {% block content %} {% endblock %}
          </body>
        </html>
        ```

    === "notes/templates/notes/index.html"
        ```html
        {% extends "notes/base.html" %}

        {% block content %}
        <img src="notes/img/logo-getit.png">
        <p>Como o Post-it, mas com outro verbo</p>

        <form method="post">
          <label for="titulo">Título</label>
          <input id="titulo" type="text" name="titulo" />
          <label for="detalhes">Detalhes</label>
          <textarea id="detalhes" name="detalhes"></textarea>
          <input type="submit" />
        </form>

        <ul>
          <li>Nenhuma anotação por enquanto.</li>
        </ul>
        {% endblock %}
        ```

Mas por que dois arquivos? Para que eles servem?

Provavelmente nós teremos mais do que uma página no nosso projeto. Em Desenvolvimento Colaborativo Ágil vocês aprenderam um pouco sobre as vantagens de evitar repetições de código. Por isso, criamos o arquivo `base.html` com o código HTML que vai se repetir em todas as páginas. No `index.html` nós usamos o `{% extends "notes/base.html" %}` para indicar para a engine de template do Django que nós queremos usar o `base.html` como base. Então modificamos apenas os blocos necessários. O que está entre o `{% block content %}` e `{% endblock %}` no `index.html` substituirá esse mesmo bloco no `base.html`. Você pode dar o nome que quiser para os seus blocos.

## Ok, mas como eu uso isso?

Vamos lá!

!!! example "Exercício"
    Modifique o seu arquivo `notes/views.py` substituindo o seu conteúdo por:

    ```python
    from django.shortcuts import render


    def index(request):
        return render(request, 'notes/index.html')
    ```

    A função `render` recebe um `request` e o nome de um arquivo de template e carrega o seu conteúdo.

    Teste sua página.

A página ainda não está nada elegante, mas já deve mostrar o conteúdo. Ou pelo menos parte dele. Você se lembra que no handout 1 os arquivos estáticos (imagem, css, js) também precisavam ser servidos pelo servidor? Pois é, não temos como fugir disso, mas o Django facilita esse processo.

!!! example "Exercício"
    Crie as pastas `notes/static/notes/img` e salve a imagem abaixo em `notes/static/notes/img/logo-getit.png`.
    
    [Download :material-download:](img/logo-getit.png){ .md-button download="logo-getit.png"}

!!! example "Exercício"
    Modifique o arquivo `notes/templates/notes/index.html` com o seguinte conteúdo:

    ```html hl_lines="2 5"
    {% extends "notes/base.html" %}
    {% load static %}

    {% block content %}
    <img src="{% static 'notes/img/logo-getit.png' %}" />
    <p>Como o Post-it, mas com outro verbo</p>

    <form method="post">
      <label for="titulo">Título</label>
      <input id="titulo" type="text" name="titulo" />
      <label for="detalhes">Detalhes</label>
      <textarea id="detalhes" name="detalhes"></textarea>
      <input type="submit" />
    </form>

    <ul>
      <li>Nenhuma anotação por enquanto.</li>
    </ul>
    {% endblock %}
    ```

    Nessas linhas nós indicamos para a engine de template do Django que queremos usar a [template tag `static`](https://docs.djangoproject.com/en/6.0/ref/templates/builtins/#static){:target="_blank"} (template tags são as tags entre `{%%}`) e depois a utilizamos para carregar o caminho completo do arquivo estático `notes/img/logo-getit.png`.

    Agora sim, a imagem deve ser carregada.

    !!! danger "Se a imagem não carregar"
        Se você fez as modificações pedidas no exercício e a imagem não carregar, tente para a execução do servidor e rode novamente.

    !!! info "Outros arquivos estáticos"
        Assim como acabamos de fazer com a imagem, você pode adicionar outros arquivos estáticos (css, javascript, etc.) na pasta `notes/static/notes` e eles serão disponibilizados pelo servidor. Para manter a organização, você pode criar uma pasta `notes/static/notes/css` para colocar os arquivos css, um `notes/static/notes/script` para os arquivos javascript, e assim por diante.

## A imagem foi, mas e as anotações no banco de dados?

Esse é o nosso próximo passo! Sabemos que as anotações que criamos manualmente pelo Django Admin estão armazenadas no banco de dados, mas como fazemos para acessá-las e depois passar para o template?

O template do Django é capaz de executar um código parecido com Python e inclusive pode receber algumas variáveis! Vamos resolver primeiro o problema de como carregar os dados do banco de dados.

!!! example "Exercício"
    Faça as seguintes modificações no arquivo `notes/views.py`:

    ```python hl_lines="2 6-8"
    from django.shortcuts import render
    from .models import Note


    def index(request):
        all_notes = Note.objects.all()
        print(all_notes)
        return render(request, 'notes/index.html', {'notes': all_notes})
    ```

    Nós estamos importando o modelo `#!python Note` e carregando todas as entradas dessa tabela. O template recebe um dicionário que define as variáveis que estarão disponíveis para ele (chamamos esse dicionário de contexto).

    !!! info "O `Manager` `objects`"
        O atributo `objects` é um objeto do tipo [`Manager`](https://docs.djangoproject.com/en/6.0/topics/db/managers/#django.db.models.Manager){:target="_blank"} criado pelo Django. Ele possui diversos métodos que permitem interagir com o banco de dados. O `all()` lista todas as entradas, mas existem outros métodos bastante úteis, como o `filter()` e o `get()`. Este handout é bastante introdutório, então não vamos discutir todo o potencial desta funcionalidade, mas é provável que você precise desses outros métodos para o projeto.

!!! example "Exercício"
    Modifique o conteúdo da tag `#!html <ul>` no arquivo `index.html` para:

    ```html
    <ul>
      <li>{{notes}}</li>
    </ul>
    ```

    Ele deve mostrar algo estranho como: `<QuerySet [<Note: 1. Receita de miojo>, <Note: 2. Pão doce>, <Note: 3. Sorvete com cristais de leite>]>`

    Esse é o mesmo objeto que estava guardado na variável `all_notes` e foi passado para o contexto do template!

!!! example "Exercício"
    Legal, mas está feio. Vamos deixar a página menos feia. Para isso, precisamos de uma forma de percorrer essas anotações e mostrar cada uma em uma `#!html <li>` diferente. Modifique novamente o conteúdo da tag `#!html <ul>` para:

    ```html
    <ul>
      {% for note in notes %}
      <li>{{ note.title }}</li>
      {% endfor %}
    </ul>
    ```

    Agora sim!

O template tag `{% for %}{% endfor %}` funciona de forma muito parecida com o `#!python for` do Python. O seu conteúdo é executado para cada elemento na lista fornecida. Uma das principais diferenças é a necessidade do `{% endfor %}` ao final. Isso acontece porque no HTML as indentações não podem ser utilizadas para definir blocos como no Python.

Quando queremos mostrar o valor de uma variável no HTML (equivalente ao que fazíamos com o `#!python .format()`) devemos utilizar o `{{}}`.

!!! danger "Importante"
    Muitas coisas aconteceram nesse último exercício. Pare por um instante para refletir e garantir que entendeu o que está acontecendo nele.

Acabou? Vamos para a [parte 6](parte6.md)!
