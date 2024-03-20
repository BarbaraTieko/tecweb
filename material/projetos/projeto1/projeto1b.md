# Projeto 1: Parte B

!!! success "Entrega"
    :date: 21/03 (quinta-feira)
    
    :clock1: Commits até as 23:59

    :material-account-group: Individual

    :simple-github: Entrega via [ :point_right: GitHub Classroom](https://classroom.github.com/a/WqLD3zMW){: target="_blank"}.

Caso não tenha criado o repositório, acesse o link [Github classroom](https://classroom.github.com/a/WqLD3zMW){:target="_blank"} para criar o repositório para este projeto.

Na [parte A](projeto1a.md) você implementou o servidor em Python sem a ajuda de nenhum framework. Nesta segunda parte, o objetivo é reimplementar as funcionalidades da parte A utilizando o Django. Além disso, vamos expandir as funcionalidades do sistema, utilizar um banco de dados mais robusto do que o SQLite e finalmente publicar o nosso sistema. Dependendo de quando você estiver lendo este enunciado, você ainda não saberá como fazer todas essas coisas, mas nós teremos alguns handouts para te auxiliar nesse processo.

## Rubrica

As tarefas a serem realizadas são:

1. Reimplementar o CRUD da parte A em Django, ou seja, implementar as funcionalidades de criação, listagem, edição e remoção de anotações aplicando o mesmo estilo (css); [Para mais detalhes acesse aqui :link:](projeto1b/tarefa01.md)
2. Implementar o sistema de tags para as anotações; [Para mais detalhes acesse aqui :link:](projeto1b/tarefa02.md)
3. Utilizar o PostgreSQL (em um container Docker) ao invés do SQLite;
4. Publicar a página. Ao realizar o deploy do seu projeto 1B, adicione o link para acessar a aplicação no README.md do seu repositório.

A rubrica a seguir será utilizada na correção do Projeto 1B:

| Conceito | Descrição |
| :------: | :-------- |
|    I     | Não entregou ou o código não executa |
|    D     | O código funciona, mas a tarefa 1 não está completa |
|    C     | Tarefa 1 completa |
|    C+    | Tarefas 1 e tarefa 2 parcial|
|    B     | Tarefas 1 e 2 completas |
|    B+    | Tarefas 1, 2 e 3 completas |
|    A     | Tarefas 1, 2, 3 e 4 completas |
|    A+    | Tarefas 1, 2, 3 e 4 completas e implementou o sistema de tags Many-to-many [acesse aqui :link:](projeto1b/tags-many-to-many.md)|

## Sugestão de Cronograma

Segue abaixo uma sugestão de cronograma para auxialiar o desenvolvimento do Projeto 1B. 

**Obs.:** Esse cronograma foi pensando para atingir o conceito A+.

<figure markdown="span">
    ![Calendário com o cronograma](projeto1b/projeto1b-calendario-241.png){ width="80%" }
    <figcaption>Calendário com o cronograma</figcaption>
</figure>

## Cronograma

- [X] **05/03 (terça-feira)**
    - [X] Realizar Handout de Django
    - [X] Adicionar estilo CSS do Desafio CSS
- [X] **07/03 (quinta-feira)**
    - [X] Implementar a funcionalidade de deletar uma anotação.
    - [X] Implementar a funcionalidade de atualizar uma anotação.
    - [X] Atingiu o **Conceito C**
- [X] **12/03 (terça-feira)**
    - Implementar o sistema de tags
    - [X] Atingiu o **Conceito B**
- [X] **14/03 (quinta-feira)**
    - [X] Utilizar o banco de dados relacionas PostgreSQL
    - [X] Atingiu o **Conceito B+**
- [X] **19/03 (terça-feira)**
    - [X] Realizar o Deploy do Projeto
    - [X] Atingiu o **Conceito A**
- [ ] **21/03 (quinta-feira)**
    - [ ] Aula Studio para finalizar o projeto
    - [ ] Efetuar a entrega
    - [ ] Atingiu o **Conceito A+**
