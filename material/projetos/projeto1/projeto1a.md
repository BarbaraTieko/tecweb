# Projeto 1: Parte A

**Trabalho individual**

**Prazo: 02/09/2023**

**Entrega via GitHub**

Indique o repositório Github no Blackboard.

Durante o primeiro handout nós desenvolvemos o [Get-it](../../aulas/01-getit.md) com as funcionalidades de listagem e criação de anotações. No [Desafio CSS](../../aulas/02-desafio-css.md) você implementou um possível estilo para a página. No segundo handout, você aprendeu a armazenar e recuperar dados de um banco de dados SQLite. Agora, no Projeto 1A, o seu objetivo é aplicar o que aprendeu nos handouts e no desafio para adicionar as seguintes funcionalidades ao sistema:

1. Estilo da página (utilizando o CSS que você já fez ou adicionando um novo estilo);
2. Armazenamento em banco de dados SQLite ao invés de um arquivo texto
3. Apagar anotações
4. Editar anotações

## Rubrica

As 4 tarefas a serem realizadas são:

1. **Estilo da página:** Implementar o estilo da página;
    - O estilo css já foi implementado na atividade **Desafio CSS**, agora é necessário utilizar este estilo no código do *handout 01*.
    - Caso queira, você pode fazer alterações no estilo da página.
2. **Persistência de dados:** Implementar a persistência dos dados com SQLite (você deve escrever o SQL na mão, ou seja, não pode utilizar bibliotecas de ORM ou similares).
    - Utilize o arquivo `database.py` desenvolvido no handout de persistência de dados. Note que o arquivo `database.py` não deverá ser alterado.
    - **Dica:** Nesta etapa, as alterações podem ser feitas no arquivo `utils.py`. Você poderá utilizar os códigos utilizados no arquivo `exemplo_de_uso.py`. Além disso, talvez seja interessante alterar a função `load_data` do arquivo `utils.py` para carregar os dados do banco de dados, ao invés do arquivo `notes.json`. Mude também a função que você criou para salvar as notas no banco de dados.
3. **Apagar anotações** Permitir que o usuário apague uma anotação;
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

4. **Editar anotações:** Permitir a edição de anotações existentes;
    - Adicione um botão na nota para a função de editar. Ao clicar no botão de edição, o usuário deve ser direcionado para uma página nova de edição.
    - A página de edição deve apresentar um formulário com o `título` e `conteúdo` já preenchidos.

    Você precisará de um método novo no arquivo `database.py` que dado um `id` de uma anotação retorna esta anotação no formato de um objeto do tipo `Note`. Caso precise, você pode encontrar o método feito em: [`database.py` (clique aqui para baixar)](database.py)

    - Esta página deve apresentar dois botões: `Salvar` e `Cancelar`.
        - Ao clicar no botão de `Cancelar` o usuário deve ser direcionado para a página principal.
        - Ao clicar no botão de `Salvar` a aplicação deve receber uma requisição no seguinte formato:
            ```
            POST /update HTTP/1.1
            <HTTP_HEADERS>

            id=<NOTA_ID>&titulo=<NOTA_TITULO>&detalhes=<NOTA_DETALHES>
            ```
        As alterações devem ser registradas no banco de dados e em seguida o usuário deve ser direcionado para a página inicial.


A rubrica a seguir será utilizada na correção do Projeto 1A:

| Conceito | Descrição |
| :------: | :-------- |
|    A     | Atingiu o conceito B+ e o repositório está organizado sem arquivos e códigos desnecessários. Além disso, implementou o uma página HTML para o código 404. (**Obs.:** Deve ter implementado a etapa do Desafio presente no final do Handout 01)|
|    B+    | Entregou o handout 01 e as 4 tarefas funcionando    |
|    B     | Entregou o handout 01 e 3 das 4 tarefas funcionando |
|    C+    | Entregou o handout 01 e 2 das 4 tarefas funcionando |
|    C     | Entregou o handout 01 e 1 das 4 tarefas funcionando |
|    D     | Entregou apenas o resultado do handout 01 funcionando e nada mais |
|    I     | Não entregou ou o código não executa |

O conceito A+ será dado aos trabalhos que superarem as expectativas do conceito A. Ou seja, implementarem alguma funcionalidade adicional (ex: realizar requisições assíncronas em JavaScript para não precisar recarregar a página inteira), apresentarem o estilo da página com qualidade acima do esperado (o que foi pedido no Desafio CSS é considerado o esperado).

É importante que você discuta com a professora e deixe claro no README.md do seu repositório o que foi feito no projeto para alcançar o conceito A+.
