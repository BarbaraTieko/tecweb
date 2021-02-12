# 01 - Simpliflix

## Parte 5: Fazendo um formulário de login

Vamos implementar agora um sistema **muito** rudimentar de autenticação. O objetivo é que você aprenda como receber dados no servidor enviados pelo navegador.

Para começar, crie uma nova página na rota `/login` que devolve o seguinte conteúdo:

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>
      Simpliflix - Para quem gosta de assistir Netflix, não os filmes
    </title>
  </head>
  <body>
    <h1>Login</h1>
    <form method="post">
      <label for="usuario">Usuário</label>
      <input id="usuario" type="text" name="usuario" />
      <label for="senha">Senha</label>
      <input id="senha" type="password" name="senha" />
      <input type="submit" />
    </form>
  </body>
</html>
```

Seu código do programa principal deve estar mais ou menos assim:

```python hl_lines="4 29-30"
--8<-- "01-simpliflix/codigo/passo12.py"
```

!!! example "EXERCÍCIO"
    Como já fizemos isso nos passos anteriores, vou deixar você tentar adicionar esta página por conta própria.

    !!! danger "Importante"
        Quando você for testar a página, ao clicar em `submit` a página simplesmente vai recarregar. É isso mesmo que deve ocorrer. Nos próximos passos nós vamos usar essa informação.

## Usando os dados recebidos do formulário

Talvez você tenha notado que no formulário (`<form>`) existe um atributo `method="post"`. Isso quer dizer que os dados do formulário serão enviados utilizando o método HTTP POST (veremos mais detalhes sobre ele no futuro). O que você precisa saber por enquanto é que até o momento nós sempre enviamos requisições do tipo GET para o servidor. Vejamos como é possível receber os dados da requisição POST.

!!! example "EXERCÍCIO"
    Modifique a sua função da rota `/login` no arquivo `views.py` para conter o seguinte conteúdo:

    ```python
    def login(request):
        # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
        if request.startswith('POST'):
            request = request.replace('\r', '')  # Remove caracteres indesejados
            # Cabeçalho e corpo estão sempre separados por duas quebras de linha
            partes = request.split('\n\n')
            corpo = partes[1]
            params = {}
            # Preencha o dicionário params com
            ESSA PARTE É COM VOCÊ

        return load_template('login.html').encode()
    ```

    Note que você terá que passar a requisição na chamada da função.

!!! example "EXERCÍCIO"
    Ainda na função `#!python login(request)` do arquivo `views.py`, salve o nome do usuário (que deverá estar armazenado em `#!python params['usuario']`) em um arquivo.

    Quando for testar o código, o nome do usuário deve ser salvo no arquivo, mas a página de login será mostrada novamente.

## Última refatoração

Seria interessante que após o login, fosse apresentada a página inicial. Para isso vamos precisar entender um pouco sobre códigos de status de respostas HTTP.

Desde a [parte 1](parte1.md) deste handout, nós começamos o cabeçalho das nossas respostas com `#!python 'HTTP/1.1 200 OK'`. O código `200` é [um dos possíveis códigos de status resposta](https://httpstatusdogs.com/). Ele diz para o navegador que a requisição foi processada com sucesso. Para avisarmos para o navegador que depois de fazer o login ele deve carregar a página inicial, vamos precisar do código `303`, que pede para o navegador se redirecionar para outra página após receber a resposta.

Até o momento o nosso servidor sempre utiliza o cabeçalho fixo com código 200. Precisamos refatorá-lo para que possamos responder com códigos diferentes.

!!! example "EXERCÍCIO"
    Implemente a função `#!python build_response` no arquivo `utils.py`. Ele deve receber os seguintes argumentos: `#!python build_response(body='', code=200, reason='OK', headers='')` (talvez você queira ler isso: https://docs.python.org/3/tutorial/controlflow.html#default-argument-values).

    Lembre-se de testar a sua função com `python test_utils.py`.

Agora que você implementou a função `#!python build_response`, vamos refatorar o código para utilizá-la.

Modifique seu programa principal da seguinte maneira:

```python hl_lines="3 26 34"
--8<-- "01-simpliflix/codigo/passo13.py"
```

!!! example "EXERCÍCIO"
    Modifique as funções `#!python index`, `#!python login` e `#!python details` no arquivo `views.py` para que elas devolvam o resultado de `#!python build_response`.

    A função `#!python login` é um pouco mais difícil, então segue uma possível solução:

    ```python
    def login(request):
        if request.startswith('POST'):
            request = request.replace('\r', '')  # Remove caracteres indesejados
            # Cabeçalho e corpo estão sempre separados por duas quebras de linha
            partes = request.split('\n\n')
            corpo = partes[1]
            params = {}
            # SUA IMPLEMENTAÇÃO QUE PREENCHE params E SALVA O USUÁRIO EM UM ARQUIVO
            # DEVE ESTAR AQUI TAMBÉM, MAS NÃO VOU COLOCAR ESSA PARTE DA RESPOSTA
            return build_response(code=303, reason='See Other', headers='Location: /')
        return build_response(load_template('login.html'))
    ```

Se tudo estiver correto você pode entrar na sua página de login e preencher qualquer usuário e senha. Depois de enviar você será automaticamente redirecionado para a página principal.

## Desafios

O handout acabou, mas se quiser praticar um pouco mais você pode:

- Mostrar o nome do usuário nas páginas;
- Devolver uma resposta com código 404 quando o usuário tenta acessar uma página que não existe;
- Fazer um botão de logout;
- Redirecionar para a página de login, caso o usuário não tenha feito o login (o arquivo com o nome do usuário não existe).

## Ufa, cansei

Parabéns! Agora você pode pegar um pote de sorvete e mandar ver enquanto lê as descrições os episódios. Depois disso, se ainda tiver pique, é um bom momento para dar aquela relembrada em CSS para a próxima aula com essa lista de jogos:

- [Flexbox Defense](http://www.flexboxdefense.com/)
- [Flexbox Froggy](https://flexboxfroggy.com)
- [Grid Garden](https://cssgridgarden.com)
- [CSS Diner](http://flukeout.github.io/)
- Se você tem interesse por CSS, você vai gostar disso: https://rupl.github.io/unfold/
