# 01 - Simpliflix

## Parte 2: Respondendo com páginas HTML

Nosso servidor já responde com `Hello World`, mas queremos muito mais que isso. Queremos implementar o nosso Simpleflix e para isso a página precisa ter muito mais conteúdo e precisa ser apresentado de maneira estruturada. Está na hora de trazermos o bom e velho HTML de volta!

Mas antes disso, nosso servidor atualmente responde uma requisição e para de rodar. Seria interessante que ele fosse capaz de responder mais do que uma requisição. Modifique seu programa da seguinte maneira:

```python hl_lines="13"
--8<-- "01-simpliflix/codigo/passo4.py"
```

A única diferença é que colocamos a parte do código que aceita a conexão do cliente, recebe a requisição e devolve a resposta dentro de um `#!python while True`. Então podemos recarregar a página no navegador quantas vezes quisermos e ela continuará a ser recebida.

!!! danger "Importante"
    Agora o servidor é um programa em loop infinito. Se quiser parar de rodar, basta encerrar o programa com ++ctrl+c++.

## Agora sim, o HTML

Vamos devolver uma página HTML simples, apenas para relembrar as coisas:

```python hl_lines="6-21 36"
--8<-- "01-simpliflix/codigo/passo5.py"
```

Testou? Funcionou? Podemos ir para o próximo passo.

## Mostrando a lista de séries

Podemos começar a pensar no conteúdo da nossa página principal. Vamos começar mostrando uma lista simples com os cartazes das séries, os nomes e os links para os detalhes. Você vai precisar baixar as [imagens do handout clicando neste link](../img.zip). Descompacte este arquivo zip na mesma pasta onde está o seu código do servidor. Ou seja, o conteúdo da sua pasta será:

```
- DIRETORIO-DO-SEU-SERVIDOR
  |- servidor.py
  |- img
     |- breakingbad
        |- ...
     |- friends
        |- ...
     |- ...
```

Para mostrar a lista de séries vamos utilizar as tags HTML *unordered list* (`#!html <ul>`), *list item* (`#!html <li>`), *anchor* (`#!html <a>`) e *image* (`#!html <img>`):

```python hl_lines="19-74"
--8<-- "01-simpliflix/codigo/passo6.py"
```

Se você rodou o código acima deve ter percebido que algo deu errado. Você não achou que seria tão simples assim, não é mesmo?

Os arquivos existem no seu computador, mas o servidor precisa enviar esses arquivos como resposta quando forem solicitados.

## Diferenciando rotas

Temos que implementar algumas coisas, mas vamos por partes. Verifique a saída no seu terminal. Você deve encontrar vários blocos de texto, um para cada requisição feita pelo navegador. Alguns exemplos:

=== "favicon.ico"

    ```
    GET /favicon.ico HTTP/1.1
    Host: 0.0.0.0:8080
    Connection: keep-alive
    Pragma: no-cache
    Cache-Control: no-cache
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
    Accept: image/avif,image/webp,image/apng,image/*,*/*;q=0.8
    Referer: http://0.0.0.0:8080/
    Accept-Encoding: gzip, deflate
    Accept-Language: en-US,en;q=0.9,pt;q=0.8
    ```

=== "Stranger Things"

    ```
    GET /img/strangerthings/stranger-things.jpg HTTP/1.1
    Host: 0.0.0.0:8080
    Connection: keep-alive
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
    Accept: image/avif,image/webp,image/apng,image/*,*/*;q=0.8
    Referer: http://0.0.0.0:8080/
    Accept-Encoding: gzip, deflate
    Accept-Language: en-US,en;q=0.9,pt;q=0.8
    ```

=== "Friends"

    ```
    GET /img/friends/friends.jpg HTTP/1.1
    Host: 0.0.0.0:8080
    Connection: keep-alive
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
    Accept: image/avif,image/webp,image/apng,image/*,*/*;q=0.8
    Referer: http://0.0.0.0:8080/
    Accept-Encoding: gzip, deflate
    Accept-Language: en-US,en;q=0.9,pt;q=0.8
    ```

O nosso servidor responde a mesma página HTML para **todas as requisições**. Não importa se o cliente está pedindo a imagem `/img/strangerthings/stranger-things.jpg` ou o `favicon.ico`. Ele **sempre** responde a mesma página HTML.

Repare que a primeira linha da requisição HTTP sempre possui uma palavra (`GET` - voltaremos a falar sobre ele mais para a frente no curso) seguida de uma rota (por exemplo, `/img/strangerthings/stranger-things.jpg`). Nós podemos utilizar essa rota no servidor para decidir o que devemos responder.

Altere novamente o código do seu servidor para:

```python hl_lines="2-3 5 26-32"
--8<-- "01-simpliflix/codigo/passo7.py"
```

Crie também o arquivo `utils.py` na pasta do seu servidor. Você deverá implementar os métodos `#!python extract_route` e `#!python read_file`. Para te ajudar, baixe também o arquivo [`test_utils.py`](../codigo/test_utils.py). Ele possui alguns testes para verificar se a sua implementação está dentro do esperado. Para executar os testes basta rodar o arquivo no terminal: `python test_utils.py` (ele tem alguns testes para outras funções das próximas partes do handout - você pode ignorar os erros delas por enquanto).

!!! example "EXERCÍCIO"
    Implemente a função `#!python extract_route`, que recebe uma string com a requisição e devolve a rota, excluindo o primeiro caractere (`#!python /`). Por exemplo, para a requisição "Stranger Things" acima, sua função deve devolver `#!python 'img/strangerthings/stranger-things.jpg'`.

!!! example "EXERCÍCIO"
    Implemente a função `#!python read_file`, que recebe um argumento do tipo [`#!python Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path) e devolve o conteúdo desse arquivo. Se a extensão do arquivo for alguma entre `.txt`, `.html`, `.css`, `.js`, sua função deve ler o arquivo como text e devolver uma string. Leia qualquer outro tipo de arquivo como binário e devolve os `#!python bytes`. Se precisar refrescar a memória, leia a [documentação da função `#!python open`](https://docs.python.org/3/library/functions.html#open).

Depois de implementar as duas funções acima e atualizar o código, o servidor deve funcionar corretamente, mostrando as imagens. Sim, está feio, mas nós resolvemos isso na próxima aula. Por enquanto vai ficar assim mesmo.

As páginas de detalhes ainda não estão prontas, mas antes disso precisamos refatorar o código porque ele já está acumulando muitas responsabilidades. Depois de se hidratar e fazer um alongamento, siga para a [parte 3 do handout](parte3.md).
