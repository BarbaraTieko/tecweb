# Projeto 1: Parte A

**Trabalho individual**

**Prazo: 06/09/2022**

**Entrega via GitHub Classroom**

Acesse o link [Github classroom](https://classroom.github.com/a/2Hd7WLd-).

Durante o primeiro handout nós desenvolvemos o [Get-it](../../aulas/01-getit.md) com as funcionalidades de listagem e criação de anotações. No [Desafio CSS](../../aulas/02-desafio-css.md) você implementou um possível estilo para a página. No segundo handout, você aprendeu a armazenar e recuperar dados de um banco de dados SQLite. Agora, no Projeto 1A, o seu objetivo é aplicar o que aprendeu nos handouts e no desafio para adicionar as seguintes funcionalidades ao sistema:

1. Estilo da página (utilizando o CSS que você já fez ou adicionando um novo estilo);
2. Editar anotações
3. Apagar anotações
4. Armazenamento em banco de dados SQLite ao invés de um arquivo texto

Ao final do Projeto 1A será possível **criar uma anotação**, **ler os dados de anotações armazenadas no arquivo (que simula o banco de dados)**, **atualizar uma anotação** e **apagar uma anotação**. Esse é um conjunto de operações bastante comum em sistemas e é conhecido como **CRUD** (<b>C</b>reate, <b>R</b>ead, <b>U</b>pdate, <b>D</b>elete).

É comum ouvirmos no ambiente de trabalho que será necessário montar um CRUD. E agora você sabe o que isso quer dizer! Ao final deste semestre você deve ser capaz de montar CRUDs sem que isso seja um grande trauma. Esse conhecimento será necessário antes mesmo de se formarem: nas disciplinas de Computação em Nuvem e Megadados, ambas no 6o semestre, os professores assumirão que vocês são capazes de colocar um CRUD no ar sem muito esforço. Por isso, é importante que vocês se empenhem nas atividades de Tecnologias Web.

## Rubrica

As 4 tarefas a serem realizadas são:

1. Implementar o estilo da página (de todas, caso sejam feitas páginas adicionais);
2. Permitir a edição de anotações existentes (você pode escolher se vai fazer uma nova página para isso ou fazer tudo na mesma página - já aviso que é mais difícil);
3. Permitir que o usuário apague uma anotação (o comentário do item anterior também vale aqui);
4. Implementar a persistência dos dados com SQLite (você deve escrever o SQL na mão, ou seja, não pode utilizar bibliotecas de ORM ou similares).

A rubrica a seguir será utilizada na correção do Projeto 1A:

| Conceito | Descrição |
| :------: | :-------- |
|    A     | Atingiu o conceito B+ e implementou todas as funcionalidades na mesma página |
|    B+    | Entregou o handout e as 4 tarefas funcionando    |
|    B     | Entregou o handout e 3 das 4 tarefas funcionando |
|    C+    | Entregou o handout e 2 das 4 tarefas funcionando |
|    C     | Entregou o handout e 1 das 4 tarefas funcionando |
|    D     | Entregou apenas o resultado do handout funcionando e nada mais |
|    I     | Não entregou ou o código não executa |

O conceito A+ será dado aos trabalhos que superarem as expectativas do conceito A. Ou seja, implementarem alguma funcionalidade adicional (ex: realizar requisições assíncronas em JavaScript para não precisar recarregar a página inteira), apresentarem o estilo da página com qualidade acima do esperado (o que foi pedido no Desafio CSS é considerado o esperado).

É importante que você deixe claro no README.md do seu repositório o que foi feito no projeto para alcançar o conceito A+.
