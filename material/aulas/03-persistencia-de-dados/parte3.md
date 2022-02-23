# Parte 3: Inserindo dados na tabela

Nossa tabela foi criada, mas ainda não possui nenhum dado. Para inserir dados na tabela utilizamos o comando SQL:

```sql
INSERT INTO NOME_DA_TABELA (NOMES_DAS_COLUNAS) VALUES (VALORES_DAS_COLUNAS)`
```

Por exemplo, na tabela `dados_pessoais`, que usamos de exemplo na parte 2, poderíamos adicionar uma nova linha com o comando

```sql
INSERT INTO dados_pessoais (nome_da_rua,cpf) VALUES ('R. Quatá','123.456.789-00');
```

!!! danger "Importante"
    Note que a coluna definida como chave primária não está entre os valores. O próprio SQLite atribui o valor da coluna como o próximo número disponível.

Para executar os comandos no banco de dados através do Python, utilizaremos novamente o método `execute` do atributo `conn`.

!!! danger "Importante 1"
    Quando for adicionar strings no banco de dados, lembre-se de colocar as aspas ao redor dos valores.

!!! danger "Importante 2"
    Depois de chamar o `execute` com o comando de inserção você precisa chamar o método `commit()` do atributo `conn` para que a inserção seja executada. Isso é necessário porque as modificações na conexão atual só são efetivamente enviadas todas de uma vez para o banco de dados após o `commit`.

!!! example "Exercício 03"
    Crie um método `#!python add(self, note)` na classe `#!python Database`, que recebe um objeto do tipo `#!python Note` e insere seus dados no banco de dados. Adicione a definição da classe `#!python Note` no arquivo `database.py`:

    ```python
    from dataclasses import dataclass

    @dataclass
    class Note:
        id: int = None
        title: str = None
        content: str = ''
    ```

    **Observação:** o código acima só é válido a partir do Python 3.7. Se você está usando uma versão mais antiga do Python, substitua esse código pelo código abaixo:

    ```python
    class Note:
        def __init__(self, id=None, title=None, content=''):
            self.id = id
            self.title = title
            self.content = content
    ```

    Depois de implementar o método `#!python add(self, note)`, teste-o com o arquivo `test_database.py`. O teste `test_add_rows` deve passar com sucesso.

Para testar as novas funcionalidades no banco de dados, adicione as linhas a seguir no arquivo `exemplo_de_uso.py` e depois visualize o resultado no DB Browser clicando na aba `Browse Data` (observação: você vai precisar importar a classe `#!python Note` nesse arquivo):

```python
db.add(Note(title='Pão doce', content='Abra o pão e coloque o seu suco em pó favorito.'))
db.add(Note(title=None, content='Lembrar de tomar água'))
```

!!! question choice
    O que o trecho de código a seguir faz?

    ```python
    db.add(Note(title='Pão doce', content='Abra o pão e coloque o seu suco em pó favorito.'))
    ```

    - [ ] Cria uma tabela nova no banco de dados.
    - [ ] Cria somente um objeto do tipo `Note`.
    - [x] Cria um objeto do tipo `Note` e inseri os dados no banco de dados.
    - [ ] Nenhuma das opções anteriores.

    !!! details "Resposta"
        Um objeto do tipo `Note` é criado com o seguinte código:
        `#!python Note(title='Pão doce', content='Abra o pão e coloque o seu suco em pó favorito.')`

        Esse objeto criado é passado como argumento para o método `add` da classe `Database` que criamos no exercício anterior.

        Esse método é responsável por inserir os dados da nota no banco de dados. 

!!! danger "Importante"
    Toda vez que você executar o arquivo `exemplo_de_uso.py` esses dados serão adicionados novamente ao banco. Para começar um novo banco, basta apagar o arquivo `banco.db` e executar o arquivo novamente.

Quando tiver terminado, siga para a [próxima parte do handout](parte4.md).
