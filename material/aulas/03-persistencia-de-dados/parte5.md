# Parte 5: Atualizando os dados

Você também pode atualizar os dados armazenados no banco com o comando `#!sql UPDATE`. Para a atualização você precisa definir:

1. Quais colunas serão modificadas;
2. Quais serão os novos valores armazenados nessas colunas;
3. Quais linhas você quer modificar.

A sintaxe do comando é:

```sql
UPDATE NOME_DA_TABELA SET NOME_DA_COLUNA = NOVO_VALOR_DA_COLUNA WHERE CONDICAO
```

Por exemplo, o código a seguir modifica o valor da coluna `cpf` para `555.555.555-55` da linha cujo valor da coluna `identificador` é igual a 2:

```sql
UPDATE dados_pessoais SET cpf = '555.555.555-55' WHERE identificador = 2
```

A condição do `#!sql WHERE` pode ser bastante complexa. Você pode, por exemplo, selecionar todas as linhas cujo `cpf` começa com a string `00`, por exemplo. Nesse caso, todas as linhas que se encaixarem nessa condição serão atualizadas.

!!! example "Exercício 05"
    Implemente o método `#!python update(self, entry)`, que recebe objeto do tipo `#!python Note` (assuma que todos os atributos, inclusive o `#!python id`, estão preenchidos) e atualiza essa entrada no banco de dados. 

    Altere o comando abaixo para atualizar o `title` e `content` da anotação onde o `id` presente no objeto recebido como argumento.

    ```sql
    UPDATE dados_pessoais SET cpf = '555.555.555-55' WHERE identificador = 2
    ``` 

    Novamente você terá que usar o método `execute`. Não se esqueça de chamar o método `commit`, assim como feito no exercício da [inserção de dados](parte3.md).

    Se tudo der certo, nenhuma mensagem de erro começando com `EXERCÍCIO05` deve aparecer.


Você pode modificar o arquivo `exemplo_de_uso.py` para atualizar alguma das entradas utilizando o seu novo método.

Estamos acabando! A [próxima parte](parte6.md) é a última!
