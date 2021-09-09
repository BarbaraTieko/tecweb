# Parte 6: Trabalhando com formulários e o método POST

Faça um teste na sua página. Preencha os dados no formulário e clique no botão para submetê-lo. Uma página parecida com essa deve ter aparecido:

![](img/csrf.png)

O [*Cross Site Request Forgery*](https://docs.djangoproject.com/en/3.1/ref/csrf/) é um tipo de ataque no qual um site malicioso utiliza um link/form/javascript para submeter dados utilizando um usuário logado no seu sistema. Para se proteger desse tipo de ataque, todos os formulários do seu sistema devem enviar, através de um [campo escondido](https://www.w3schools.com/tags/att_input_type_hidden.asp), um token gerado pelo servidor. Assim, o servidor saberá que a requisição foi feita por um cliente confiável.

Isso pode soar complexo, mas basta inserir uma template tag no seu formulário. O Django cuida do resto.

!!! example "Exercício"
    Modifique o `#!html <form>` do arquivo `index.html` com o seguinte conteúdo:

    ```html hl_lines="2"
    <form method="post">
      {% csrf_token %}
      <label for="titulo">Título</label>
      <input id="titulo" type="text" name="titulo" />
      <label for="detalhes">Detalhes</label>
      <textarea id="detalhes" name="detalhes"></textarea>
      <input type="submit" />
    </form>
    ```

    Se você testar novamente, o erro não deve ocorrer mais.

## Recebendo requisições POST

O próximo passo é diferenciar o tipo da requisição recebida. O objeto `#!python request` recebido como argumento nas suas views possui um [atributo `method`](https://docs.djangoproject.com/en/3.1/ref/request-response/#django.http.HttpRequest.method). Esse atributo é uma string contendo o nome do método em letras maiúsculas (`#!python 'GET'` ou `#!python 'POST'`). Além disso, caso seja uma requisição do tipo POST, haverá também um [atributo `POST`](https://docs.djangoproject.com/en/3.1/ref/request-response/#django.http.HttpRequest.POST) com um dicionário (na verdade um *dictionary-like*) cujas chaves são os nomes (atributo `#!html name`) dos inputs e os valores são os valores contidos no input.

!!! example "Exercício"
    Modifique o arquivo `notes/views.py` com o seguinte conteúdo:

    ```python hl_lines="6-11"
    from django.shortcuts import render, redirect
    from .models import Note


    def index(request):
        if request.method == 'POST':
            title = request.POST.get('titulo')
            content = request.POST.get('detalhes')
            # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
            return redirect('index')
        else:
            all_notes = Note.objects.all()
            return render(request, 'notes/index.html', {'notes': all_notes})

    ```

    Como você pode ver no comentário, você tem a tarefa de criar um novo `Note` no banco de dados com o título e conteúdo recebidos pela requisição. Esta página da documentação pode ser útil: https://docs.djangoproject.com/en/3.1/topics/db/queries/

Parabéns! Você terminou o handout de Django!
