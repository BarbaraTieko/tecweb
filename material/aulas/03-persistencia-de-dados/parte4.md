# Parte 4: Consultando e selecionando dados

Muito bem, nós já conseguimos adicionar informações no nosso banco de dados, mas ele ainda não serve para muita coisa. Queremos que o nosso programa seja capaz de recuperar/consultar esses dados quando necessário. E é isso o que vamos fazer nesta parte do handout.

Bom, o próprio nome da linguagem (Structured **Query** Language - `query = consulta`) já indica que o SQL nos permite consultar esses dados de alguma forma. Para este fim existe o comando `#!sql SELECT`. Esse é um comando bastante flexível, que permite definir condições para a seleção (usando o operador `#!sql WHERE`), combinar dados de tabelas diferentes (operação `#!sql JOIN`), selecionar apenas um subconjunto das colunas disponíveis, etc. Nosso objetivo não é entrar nesse nível de detalhe, mas existem muitos recursos gratuitos de boa qualidade disponíveis na internet para quem se interessar. Um exemplo é o [conteúdo da w3schools](https://www.w3schools.com/sql/).

Para o propósito deste handout vamos usar o comando `#!sql SELECT` da seguinte maneira:

```sql
SELECT NOME_DAS_COLUNAS FROM NOME_DA_TABELA
```

No exemplo da tabela de dados pessoais, o comando para selecionar todas as linhas da tabela seria: `#!sql SELECT identificador, nome_da_rua, cpf FROM dados_pessoais`

Ao executar esse comando com o método `conn.execute`, o valor devolvido será um `sqlite3.Cursor`. Ele contém as linhas obtidas no banco de dados a partir da consulta e pode ser percorrida de forma parecida com o que fazemos com listas:

```python
cursor = conn.execute("SELECT identificador, nome_da_rua, cpf FROM dados_pessoais")
for linha in cursor:
   identificador = linha[0]
   nome_da_rua = linha[1]
   cpf = linha[2]
```

!!! example "Exercício 04"
    Implemente o método `#!python get_all(self)` na classe `#!python Database`. Ele não recebe nenhum argumento e devolve uma lista de objetos do tipo `Note`, com os valores obtidos do banco de dados.

    O teste `#!python test_select_rows` do `test_database.py` verifica se esse método está correto.

Para testar a nova funcionalidade no banco de dados, adicione as linhas a seguir no arquivo `exemplo_de_uso.py`:

```python
notes = db.get_all()
for note in notes:
    print(f'Anotação {note.id}:\n  Título: {note.title}\n  Conteúdo: {note.content}\n')
```

Quando terminar, siga para a [parte 5 do handout](parte5.md).
