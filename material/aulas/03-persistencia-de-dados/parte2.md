# Parte 2: Criando a tabela


<figure markdown="span">
  ![Acessando dados](img/acessando-dados.png){ width="70%" }
  <figcaption>Acessando dados</figcaption>
</figure>


De modo geral, sistemas de bancos de dados são programas que ficam executando infinitamente. Um programa externo pode se conectar a esse programa para interagir com o banco de dados. Esse vai ser o nosso primeiro passo. Como queremos realizar múltiplas operações no banco de dados, vamos encapsular (lembra desse termo de Desenvolvimento Colaborativo Ágil?) a responsabilidade de se comunicar com o banco de dados em uma classe chamada `#!python Database`. A função para se conectar ao banco de dados é:

```python
conexao = sqlite3.connect(NOME_DO_ARQUIVO_DO_BANCO)
```

Para mais detalhes, acesse :point_right: [Documentação SQLite3](https://docs.python.org/3/library/sqlite3.html?highlight=sqlite#tutorial){: target="_blank"}.

!!! info "Repositório Github"
    Para esta atividade, continue trabalhando no repositório Github utilizado no handout 01.

!!! example "Exercício 01"
    1. **Criando arquivo:** Crie um arquivo chamado `database.py`. 
    1. **Importe:** Importe o pacote `#!python sqlite3`.
    1. **Criando a Classe** Nesse arquivo, crie uma classe chamada `#!python Database`. 
        
        1. O construtor da classe receberá o nome do banco de dados. 
        2. Na construção, o objeto deve guardar a conexão com o banco (resultado da chamada da função `#!python sqlite3.connect` mostrada acima) em um atributo chamado `#!python conn`.

        **Atenção:** Note que o arquivo do banco de dados deve possui a extensão `.db` (exemplo: NOME_DO_ARQUIVO + '.db').

        Se não se lembrar a sintaxe de classes em Python, procure no Google ou acesse a :point_right:  [documentação](https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables){: target="_blank"}. 


    1. **Testando a solução:** Para testar o seu código, faça o download <a href="../test_database.py" download="test_database.py">deste arquivo :arrow_down:</a> e salve na mesma pasta do arquivo `database.py`. 
        - Executar o comando abaixo no terminal para rodar todos os testes. 
        === "Windows :material-microsoft-windows:/Linux :simple-linux:"
            ```bash
            python test_database.py
            ```
        === "MacOS :material-apple:"
            ```bash
            python3 test_database.py
            ```

    !!! success "Exercício passando com sucesso" 
        Caso nenhuma mensagem de erro começando com `EXERCÍCIO01` apareça, sua solução está passando com sucesso nos testes.
        
        As outras mensagens são referentes aos próximos exercícios.

!!! danger "Erro de permissão"
    Caso se depara com o seguinte erro:
    ```bash
    PermissionError: [WinError 32] O arquivo já está sendo usado por outro processo
    ```

    Abra o arquivo `test_database.py` e comente as linhas 42 a 52:
    ```python hl_lines="4-7"
    class DatabaseTestCase(unittest.TestCase):
    def setUp(self):
        db_file = Path.cwd() / DB_FILENAME
        try:
            db_file.unlink()  
        except FileNotFoundError:
            pass
    ```

    Antes de rodar os testes apague o arquivo `banco-teste.db` que foi criado na pasta.


## Criando a tabela

Para o nosso projeto vamos precisar de apenas uma tabela. Essa tabela vai representar as anotações. 


<figure markdown="span">
  ![Tabela Note](img/table-note.png){ width="80%" }
  <figcaption>Tabela Note</figcaption>
</figure>

Para criar uma tabela com SQL utilizamos o comando:

```sql
CREATE TABLE NOME_DA_TABELA COLUNAS_DA_TABELA;
```

Uma tabela só pode ser criada uma única vez. Você deveria encontrar um lugar para colocar o código de criação da tabela que só fosse executado uma única vez. Se você tentar criar a tabela mais de uma vez ocorrerá um erro.

Para não precisar se preocupar com isso você pode usar adicionar `#!sql IF NOT EXISTS` para a tabela ser criada apenas se ainda não existir. Assim, você pode executar o comando múltiplas vezes sem se preocupar. O comando ficaria então:

```sql
CREATE TABLE IF NOT EXISTS NOME_DA_TABELA (COLUNAS_DA_TABELA);
```

As colunas da tabela são separadas por vírgula e são indicadas como `#!sql NOME_DA_COLUNA TIPO_DA_COLUNA RESTRICOES_ADICIONAIS`. Alguns exemplos:

- `#!sql nome_da_rua TEXT NOT NULL` define uma coluna chamada `nome_da_rua`, na qual podem ser inseridos apenas valores do tipo texto e ela não pode ser vazia;
- `#!sql cpf TEXT NOT NULL UNIQUE` define uma coluna chamada `cpf`, na qual podem ser inseridos apenas valores do tipo texto e os valores devem ser únicos, ou seja, não pode haver dois CPFs iguais;
- `#!sql identificador INTEGER PRIMARY KEY` define uma coluna chamada `identificador`, na qual podem ser inseridos apenas valores do tipo inteiro e ela será utilizada como **chave primária** (explicaremos abaixo o que isso significa).

Você poderia então, por exemplo, criar a tabela `dados_pessoais` com o comando (note os parênteses e o ponto e vírgula):

```sql
CREATE TABLE IF NOT EXISTS dados_pessoais ( nome_da_rua TEXT NOT NULL,
                                            cpf TEXT NOT NULL UNIQUE,
                                            identificador INTEGER PRIMARY KEY);
```


!!! info "Chave primária"
    Uma das características de bancos de dados é a possibilidade de encontrar dados rapidamente. Para isso é comum o uso de identificadores únicos. Identificadores do tipo inteiro, além de facilitarem a busca, podem ser utilizados em diversas otimizações.

### Enviando um comando SQL para o banco de dados

Ok, já sei qual é o comando para criar uma tabela, mas como eu o envio para o banco de dados? Agora é a hora de utilizarmos a conexão que criamos no exercício anterior. O objeto armazenado no atributo `#!python conn` possui um método chamado `#!python execute`, que recebe uma string contendo um comando SQL e envia para o banco de dados.

Caso queira, procure um exemplo do uso do método `#!python execute` no link a seguir: :point_right: [Documentação SQLite3](https://docs.python.org/3/library/sqlite3.html?highlight=sqlite#tutorial){: target="_blank"}.


!!! example "Exercício 02"
    Modifique o código do exercício anterior para que ele crie uma tabela no construtor da classe `#!python Database`. 
    
    Altere o exemplo abaixo, para criar uma tabela que deve se chamar `note` e deve ter as colunas `id` (chave primária do tipo inteiro), `title` (do tipo string), `content` (do tipo string e não pode ser vazia).

    ```sql
    CREATE TABLE IF NOT EXISTS dados_pessoais ( identificador INTEGER PRIMARY KEY,
                                                nome_da_rua TEXT NOT NULL,
                                                cpf TEXT NOT NULL UNIQUE );
    ```

   
    Normalmente, utilizamos o comando acima no sistema de banco de dados. Porém, neste exercício queremos utilizar o Python para enviar o comando para o banco de dados. 

    Veja um exemplo de como fazer isso: [Documentação SQLite3](https://docs.python.org/3/library/sqlite3.html?highlight=sqlite#tutorial){: target="_blank"}

    **Importante!** Antes de rodar os testes apague o arquivo `banco-teste.db`, caso exista.

    Como no exercício anterior, rode os testes no arquivo `test_database.py` para verificar se a sua implementação está correta. Se tudo der certo, nenhuma mesangem de erro começando com `EXERCÍCIO02` deve aparecer.


### Validando o resultado com o DB Browser for SQLite

Crie um arquivo chamado `exemplo_de_uso.py` na mesma pasta com o seguinte conteúdo:

```python
from database import Database

db = Database('banco')
```

Após executar este programa, um arquivo chamado `banco.db` deve ter aparecido na sua pasta. Esse arquivo contém todo o seu banco de dados. Na maioria dos bancos de dados os arquivos não ficam tão acessíveis, mas como o SQLite é uma opção mais simples e direta, se quiser apagar o banco, basta apagar esse arquivo (e na verdade é o que fazemos no `test_database.py`).

#### Visualizando o banco de dados (Opção 1 - DB Brower for SQLite)
Abra o arquivo `banco.db` no DB Browser for SQLite (clique no botão `Open Database` e selecione o arquivo). Você deve ver uma tela parecida com esta:

![](tela1.png)

<!-- #### Visualizando o banco de dados (Opção 2 - Extensão VS Code SQLite3 Viewer) -->


Veja que a tabela foi criada e as colunas estão listadas corretamente.

Agora que a tabela foi criada, podemos ir para a [próxima parte](parte3.md).
