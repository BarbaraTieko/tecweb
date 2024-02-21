
# Tarefas do Projeto 1A

As 4 tarefas a serem realizadas são:


## Estilo da página: 

- O estilo css já foi implementado na atividade **Desafio CSS**, agora é necessário adicionar este estilo no código do *handout 01*.

Para isso, será necessário:

- Adicionar os arquivos `getit.css` e `getit.js` do Desafio CSS na pasta do repositório do projeto.

- Fazer um merge manual dos arquivos `index.html` e `notes.html` do Desafio CSS + Handout 01. Esta etapa deve ser realizada com cuidado pois existem trechos de uma versão que não existem na outra.

Ao finalizar esta etapa, a página deve estar com o estilo do Desafio CSS e com as funcionalidades do Handout 01.

## Persistência de dados: 

Implementar a persistência dos dados com SQLite. Nesta etapa, você deverá utilizar o resultado obtido no Handout 03.

- Utilize o arquivo `database.py` desenvolvido no handout de persistência de dados. 

**Dica** :material-alarm-light:

- Nesta etapa, as alterações podem ser feitas no arquivo `utils.py`. Procure todos os trechos de código que realizam leitura e escrita do arquivo `notes.json` e altere para que estas operações sejam realizadas no banco de dados.

- Os códigos do arquivo `exemplo_de_uso.py` são um bom exemplo de como vocês utilizarão a classe `Database` para realizar as operações de CRUD.

- Ao finalizar esta etapa, caso não utilize mais o arquivo `notes.json`, apague o arquivo do repositório.

## Apagar anotações

Permitir que o usuário apague uma anotação;

- Adicione um botão no `card` de cada nota existente para excluir esta nota.
- Você pode utilizar o método **GET** ou **POST** para esta tarefa.
    - **GET:** Caso opte pelo método **GET** a requisição deve seguir o seguinte formato:
        ```
        GET /delete/<NOTA_ID> HTTP/1.1
        ```
        (Obs.: A rota pode variar um pouco dependendo da forma como você escolher implementar)
    - **POST:** Caso opte pelo método **POST** a requisição deve seguir o seguinte formato:
        ```
        POST /delete HTTP/1.1
        <HTTP_HEADERS>

        id=<NOTA_ID>
        ```
- **Observação:** Note que o `id` da nota não deve aparecer na tela, pois esta informação é irrelevante para o usuário.

## Editar anotações: 
Permitir a edição de anotações existentes;

- Adicione um botão na nota para a função de editar. Ao clicar no botão de edição, o usuário deve ser direcionado para uma página nova de edição.
- A página de edição deve apresentar um formulário com o `título` e `conteúdo` já preenchidos.

Você precisará de um método novo no arquivo `database.py` que dado um `id` de uma anotação retorna esta anotação no formato de um objeto do tipo `Note`. 

- Esta página deve apresentar dois botões: `Salvar` e `Cancelar`.
    - Ao clicar no botão de `Cancelar` o usuário deve ser direcionado para a página principal.
    - Ao clicar no botão de `Salvar` a aplicação deve receber uma requisição no seguinte formato:
        ```
        POST /update HTTP/1.1
        <HTTP_HEADERS>

        id=<NOTA_ID>&titulo=<NOTA_TITULO>&detalhes=<NOTA_DETALHES>
        ```
    As alterações devem ser registradas no banco de dados e em seguida o usuário deve ser direcionado para a página inicial.
