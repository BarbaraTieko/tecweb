# Parte 6: Apagando dados

A última operação que falta para completarmos as operações CRUD (<b>C</b>reate, <b>R</b>ead, <b>U</b>pdate, <b>D</b>elete) é apagar uma linha. Para isso vamos utilizar o comando `#!sql DELETE`:

```sql
DELETE FROM NOME_DA_TABELA WHERE CONDICAO;
```

Por exemplo:

```sql
DELETE FROM dados_pessoais WHERE identificador = 5
```

Note que depois dessa operação não vai mais existir uma linha com `identificador` igual a `5`. Os identificadores não são atualizados para preencher valores inexistentes.

!!! example "Exercício 06"
    Implemente o método `#!python delete(self, note_id)`, que recebe o valor de um `id` e apaga essa entrada do banco de dados. Obs: lembre-se de chamar o método `#!python commit` depois do `#!python execute`.

    Teste sua função com o `#!python test_delete_row`.

Depois que estiver com todos os testes passando você já pode juntar o código deste handout com o restante do seu [Projeto 1: parte A](../../projetos/projeto1/projeto1a.md)!
