# Parte 2: Criando a tabela

De modo geral, sistemas de bancos de dados são programas que ficam executando infinitamente. Um programa externo pode se conectar a esse programa para interagir com o banco de dados. Esse vai ser o nosso primeiro passo. Como queremos realizar múltiplas operações no banco de dados, vamos encapsular (lembra desse termo de Desenvolvimento Colaborativo Ágil?) a responsabilidade de se comunicar com o banco de dados em uma classe chamada `#!python Database`. A função para se conectar ao banco de dados é:

```python
conexao = sqlite3.connect(NOME_DO_ARQUIVO_DO_BANCO)
```

!!! example "Exercício"
    Crie um arquivo chamado `database.py`. Nesse arquivo, crie uma classe chamada `#!python Database`. O construtor da classe receberá o nome do banco de dados. Na construção, o objeto deve guardar a conexão com o banco (resultado da chamada da função `#!python sqlite3.connect`) em um atributo chamado `#!python conn`. Note que o arquivo do banco de dados possui a extensão `.db`.

    Lembre-se de importar o pacote: `#!python import sqlite3`.

    Para testar o seu código, faça o download [deste arquivo](test_database.py) e salve na mesma pasta do arquivo `database.py`. Basta executar `python test_database.py` no terminal para rodar todos os testes.

    Se não se lembrar a sintaxe de classes em Python, procure no Google. Se não conseguir entender, chame o professor.

## Criando a tabela

Para o nosso projeto vamos precisar de apenas uma tabela. Essa tabela vai representar as anotações. Para criar uma tabela com SQL utilizamos o comando `#!sql CREATE TABLE NOME_DA_TABELA COLUNAS_DA_TABELA;`. Uma tabela só pode ser criada uma única vez. Você deveria encontrar um lugar para colocar o código de criação da tabela que só fosse executado uma única vez. Se você tentar criar a tabela mais de uma vez ocorrerá um erro.

Para não precisar se preocupar com isso você pode usar adicionar `#!sql IF NOT EXISTS` para a tabela ser criada apenas se ainda não existir. Assim, você pode executar o comando múltiplas vezes sem se preocupar. O comando ficaria então: `#!sql CREATE TABLE IF NOT EXISTS NOME_DA_TABELA COLUNAS_DA_TABELA;`.

As colunas da tabela são separadas por vírgula e são indicadas como `#!sql NOME_DA_COLUNA TIPO_DA_COLUNA RESTRICOES_ADICIONAIS`. Alguns exemplos:

- `#!sql nome_da_rua TEXT NOT NULL` define uma coluna chamada `nome_da_rua`, na qual podem ser inseridos apenas valores do tipo texto e ela não pode ser vazia;
- `#!sql cpf TEXT NOT NULL UNIQUE` define uma coluna chamada `cpf`, na qual podem ser inseridos apenas valores do tipo texto e os valores devem ser únicos, ou seja, não pode haver dois CPFs iguais;
- `#!sql identificador INTEGER PRIMARY KEY` define uma coluna chamada `identificador`, na qual podem ser inseridos apenas valores do tipo inteiro e ela será utilizada como **chave primária** (explicaremos abaixo o que isso significa).

Você poderia então, por exemplo, criar a tabela `dados_pessoais` com o comando `#!sql CREATE TABLE IF NOT EXISTS dados_pessoais (nome_da_rua TEXT NOT NULL, cpf TEXT NOT NULL UNIQUE, identificador INTEGER PRIMARY KEY);` (note os parênteses e o ponto e vírgula).

!!! info "Chave primária"
    Uma das características de bancos de dados é a possibilidade de encontrar dados rapidamente. Para isso é comum o uso de identificadores únicos. Identificadores do tipo inteiro, além de facilitarem a busca, podem ser utilizados em diversas otimizações.

### Enviando um comando SQL para o banco de dados

Ok, já sei qual é o comando para criar uma tabela, mas como eu o envio para o banco de dados? Agora é a hora de utilizarmos a conexão que criamos no exercício anterior. O objeto armazenado no atributo `#!python conn` possui um método chamado `#!python execute`, que recebe uma string contendo um comando SQL e envia para o banco de dados.

!!! example "Exercício"
    Modifique o código do exercício anterior para que ele crie uma tabela no construtor da classe `#!python Database`. A tabela deve se chamar `note` e deve ter as colunas `id` (chave primária do tipo inteiro), `title` (do tipo string), `content` (do tipo string e não pode ser vazia).

    Como no exercício anterior, rode os testes no arquivo `test_database.py` para verificar se a sua implementação está correta.

### Validando o resultado com o DB Browser for SQLite

Crie um arquivo chamado `exemplo_de_uso.py` na mesma pasta com o seguinte conteúdo:

```python
from database import Database

db = Database('banco')
```

Após executar este programa, um arquivo chamado `banco.db` deve ter aparecido na sua pasta. Esse arquivo contém todo o seu banco de dados. Na maioria dos bancos de dados os arquivos não ficam tão acessíveis, mas como o SQLite é uma opção mais simples e direta, se quiser apagar o banco, basta apagar esse arquivo (e na verdade é o que fazemos no `test_database.py`).

Abra o arquivo `banco.db` no DB Browser for SQLite (clique no botão `Open Database` e selecione o arquivo). Você deve ver uma tela parecida com esta:

![](tela1.png)

Veja que a tabela foi criada e as colunas estão listadas corretamente.

Agora que a tabela foi criada, podemos ir para a [próxima parte](parte3.md).
