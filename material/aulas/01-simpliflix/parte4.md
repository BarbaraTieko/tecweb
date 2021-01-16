# 01 - Simpliflix

## Parte 4: Criando a página de detalhes

Finalmente chegamos à última parte do handout! Agora só falta criar as páginas de detalhes das séries. Vamos ver se as refatorações da parte 3 foram úteis.

Queremos que o servidor responda com uma página específica com os detalhes de uma série quando a rota `/slug-da-serie` for acessada. Para isso precisamos de poucas modificações no programa principal:

```python hl_lines="4 31"
--8<-- "01-simpliflix/codigo/passo11.py"
```

## Carregando os dados dos episódios de uma série

Antes de implementar a função `#!python details`, baixe o [arquivo de dados de episódios clicando aqui](../codigo/data/episodes.json) e implemente a última função que falta no arquivo `utils.py`.

!!! example "EXERCÍCIO"
    Implemente a função `#!python load_episodes` que recebe o slug de uma série e o nome do arquivo JSON que contém os dados dos episódios e devolve uma lista contendo apenas os dicionários de episódios daquela série **ordenada pelo `numero`**. O nome do arquivo não inclui o nome da pasta `data`. Por exemplo: para a entrada `friends` e `episodes.json` você deve carregar o conteúdo do arquivo `data/episodes.json` e devolver apenas os episódios da série Friends ordenados pelo número.

## Mostrando a página de detalhes

Os templates HTML já foram criados para você. Basta criar os arquivos `templates/details.html` e `templates/components/episode.html` com o conteúdo abaixo:

=== "templates/details.html"

    ```html
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>{title} | Simpliflix - Para quem gosta de assistir Netflix, não os filmes</title>
    </head>
    <body>
      <h1>{title}</h1>
      <img src="{image}" alt="{title}" />
      <ul>
        {episodes}
      </ul>
    </body>
    </html>
    ```

=== "templates/components/episode.html"

    ```html
    <li>
      <h3>{title}</h3>
      <img src="{thumbnail}" alt="{title}" />
      <p>{description}</p>
    </li>
    ```

!!! example "EXERCÍCIO"
    Implemente a função `#!python details` no arquivo `views.py`. Essa função recebe o slug de uma série como argument e devolve o HTML da página de detalhes dessa série, caso exista. Caso contrário, devolve uma sequência de bytes vazia (`#!python bytes()`).

Depois de implementar a função `#!python details` a primeira versão do Simpliflix estará completa!

Parabéns! Agora você pode pegar um pote de sorvete e mandar ver enquanto lê as descrições os episódios. Depois disso, se ainda tiver pique, é um bom momento para dar aquela relembrada em CSS para a próxima aula com essa lista de jogos:

- [Flexbox Defense](http://www.flexboxdefense.com/)
- [Flexbox Froggy](https://flexboxfroggy.com)
- [Grid Garden](https://cssgridgarden.com)
- [CSS Diner](http://flukeout.github.io/)
- Se você tem alguma curiosidade sobre CSS você vai gostar disso: https://rupl.github.io/unfold/
