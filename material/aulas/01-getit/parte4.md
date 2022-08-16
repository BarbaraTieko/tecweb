# 01 - Get-it

## Parte 4: Fazendo um formulário de criação de anotação

Vamos implementar agora a funcionalidade de adicionar anotações. O objetivo é que você aprenda como receber dados no servidor enviados pelo navegador.

Para começar, modifique o template `index.html` para adicionar o `#!html <form>`:

```html
<!-- DOCTYPE, HTML, HEAD DEVEM CONTINUAR AQUI -->
<body>
  <img src="img/logo-getit.png">
  <p>Como o Post-it, mas com outro verbo</p>

  <form method="post">
    <label for="titulo">Título</label>
    <input id="titulo" type="text" name="titulo" />
    <label for="detalhes">Detalhes</label>
    <input id="detalhes" name="detalhes" />
    <input type="submit" />
  </form>
  <!-- O RESTO DO HTML A PARTIR DAQUI -->
```

Seu código do programa principal não precisa ser modificado ainda.

!!! example "EXERCÍCIO"
    Execute o servidor e teste a página.

    !!! danger "Importante"
        Quando você for testar a página, ao clicar em `submit` a página simplesmente vai recarregar. É isso mesmo que deve ocorrer. Nos próximos passos nós vamos usar essa informação.

## Usando os dados recebidos do formulário

Talvez você tenha notado que no formulário (`<form>`) existe um atributo `method="post"`. Isso quer dizer que os dados do formulário serão enviados utilizando o método HTTP POST (veremos mais detalhes sobre ele no futuro). O que você precisa saber por enquanto é que até o momento nós sempre enviamos requisições do tipo GET para o servidor. Para entender melhor o que está acontecendo, observe a saída do seu terminal. Deve haver uma requisição parecida com essa:

```
POST / HTTP/1.1
Host: 0.0.0.0:8080
Connection: keep-alive
Content-Length: 25
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://0.0.0.0:8080
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://0.0.0.0:8080/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,pt;q=0.8

titulo=Sorvete+de+banana&detalhes=Coloque+uma+banana+no+congelador+e+espere.+Pronto%21+1%2B1%3D2.
```

Há dois pontos importantes:

1. A primeira linha da requisição está diferente. Existe um `POST` ao invés de `GET`, mas a rota é a mesma (`/`).
2. O corpo da requisição (última linha) parece um dicionário, mas está um pouco estranho.

Vamos utilizar o começo da string de requisição para saber o seu tipo (`GET` ou `POST`). Além disso, vamos processar o corpo da requisição para obter as informações recebidas do usuário. Para isso, você vai precisar da função `#!python urllib.parse.unquote_plus` [(veja a documentação aqui)](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.unquote_plus)

!!! example "EXERCÍCIO"
    Modifique a sua função `index` no arquivo `views.py` para conter o seguinte conteúdo:

    ```python
    def index(request):
        # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
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
                # AQUI É COM VOCÊ

        # O RESTO DO CÓDIGO DA FUNÇÃO index CONTINUA DAQUI PARA BAIXO...
    ```

    **Importante:** note que você terá que passar a requisição na chamada da função.

!!! example "EXERCÍCIO"
    Ainda na função `#!python index(request)` do arquivo `views.py`, adicione a nova anotação (que deverá estar armazenada em `#!python params['titulo']` e `#!python params['detalhes']`) ao arquivo `notes.json`.

    Dica: crie uma função no arquivo `utils.py` que recebe a nova anotação e a adiciona à lista do arquivo `notes.json`.

## Última refatoração

Envie novamente uma nova anotação e recarregue a página. O navegador deve perguntar se você quer reenviar o formulário. Se você confirmar, a anotação deve ser adicionada mais uma vez, ficando duplicada no arquivo `notes.json`. Por que isso acontece? Como podemos corrigir? Para isso vamos precisar entender um pouco sobre códigos de status de respostas HTTP.

Desde a [parte 1](parte1.md) deste handout, nós começamos o cabeçalho das nossas respostas com `#!python 'HTTP/1.1 200 OK'`. O código `200` é [um dos possíveis códigos de status resposta](https://httpstatusdogs.com/). Ele diz para o navegador que a requisição foi processada com sucesso. Para avisarmos para o navegador que depois de enviar a anotação ele deve recarregar a lista de anotações, vamos precisar do código `303`, que pede para o navegador se redirecionar para outra página após receber a resposta. No nosso caso, vamos redirecionar para a mesma página, mas a nova requisição será novamente do tipo GET (para saber um pouco mais [leia este artigo](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Redirecionamento#redirecionamentos_tempor%C3%A1rios)).

Até o momento o nosso servidor sempre utiliza o cabeçalho fixo com código 200. Precisamos refatorá-lo para que possamos responder com códigos diferentes.

!!! example "EXERCÍCIO"
    Implemente a função `#!python build_response` no arquivo `utils.py`. Ele deve receber os seguintes argumentos: `#!python build_response(body='', code=200, reason='OK', headers='')` (talvez você queira ler isso: https://docs.python.org/3/tutorial/controlflow.html#default-argument-values).

    Lembre-se de testar a sua função com `python test_utils.py`.

Agora que você implementou a função `#!python build_response`, vamos refatorar o código para utilizá-la.

Modifique seu programa principal da seguinte maneira:

```python hl_lines="3 28 34"
--8<-- "01-getit/codigo/passo11.py"
```

!!! example "EXERCÍCIO"
    Modifique a função `#!python index` no arquivo `views.py` para que ela devolva o resultado de `#!python build_response`.

    Dica: no caso do `POST`, você deve devolver o resultado de `#!python build_response(code=303, reason='See Other', headers='Location: /')`.

Se tudo estiver correto você pode preencher o formulário e enviar. A lista de anotações deve ser atualizada e, ao recarregar a página, o navegador não deve perguntar novamente se você quer reenviar o formulário.

## Desafio

O handout acabou, mas se quiser praticar um pouco mais você pode fazer o servidor devolver uma resposta com o código 404 quando a requisição é feita a uma página/recurso que não existe (dica: você só vai precisar modificar uma linha).

## Ufa, cansei

Parabéns! Agora você pode tentar fazer alguma das receitas da nossa lista de anotações. Depois disso, se ainda tiver pique, é um bom momento para dar aquela relembrada em CSS para a próxima aula com essa lista de jogos:

- [Flexbox Defense](http://www.flexboxdefense.com/)
- [Flexbox Froggy](https://flexboxfroggy.com)
- [Grid Garden](https://cssgridgarden.com)
- [CSS Diner](http://flukeout.github.io/)
- Se você tem interesse por CSS, você vai gostar disso: https://rupl.github.io/unfold/
