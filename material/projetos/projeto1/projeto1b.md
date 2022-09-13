# Projeto 1: Parte B

**Trabalho individual**

**Prazo: 27/09/2022 (terça-feira)**

**Entrega via GitHub Classroom**

Acesse o link [Github classroom](https://classroom.github.com/a/KDIr3h7A) para criar o repositório para este projeto.

Na [parte A](projeto1a.md) você implementou o servidor em Python sem a ajuda de nenhum framework. Nesta segunda parte, o objetivo é reimplementar as funcionalidades da parte A utilizando o Django. Além disso, vamos expandir as funcionalidades do sistema, utilizar um banco de dados mais robusto do que o SQLite e finalmente publicar o nosso sistema. Dependendo de quando você estiver lendo este enunciado, você ainda não saberá como fazer todas essas coisas, mas nós teremos alguns handouts para te auxiliar nesse processo.

## Reimplementando Projeto 1A usando Django
Reimplementar o CRUD da parte A em Django, ou seja, implementar as funcionalidades de criação, listagem, edição e remoção de anotações. Agora você deve fazer a edição das notas em uma página separa.

Para esta etapa o ideal é utilizar a estrutura que o framework dispõe.
Como discutido na aula anterior, utilize mais de uma rota para mapear as diferentes requisições que o cliente pode enviar ao servidor.

Para mais informações veja: [URL Dispatcher](https://docs.djangoproject.com/en/4.0/topics/http/urls/)

## Sistema de tags

Na parte B você deve implementar um sistema de tags para as anotações. Cada anotação pode ter no máximo uma tag (pode não ter nenhuma).

No formulário de criação/edição de anotações deve haver um campo de texto adicional para o usuário digitar o nome da tag. No backend (no `view.py`), se essa tag já existir, você deve associar a anotação a ela, senão, crie uma nova tag no banco de dados e associe à anotação.

Você também precisa criar mais duas páginas: uma com a lista com todas as tags existentes e outra com as anotações de uma determinada tag. A lista das tags deve mostrar apenas os nomes das tags com um link para a sua respectiva página de detalhes. A página de detalhes de uma tag deve mostrar o nome da tag e todas as anotações com aquela tag específica.

Para mais informações veja: [Relação Um para Muitos](https://docs.djangoproject.com/en/4.0/topics/db/examples/many_to_one/)
**Obs.:** O sistema de tags deve utilizar a relação de um para muitos.
## Rubrica

As tarefas a serem realizadas são:

1. Reimplementar o CRUD da parte A em Django, ou seja, implementar as funcionalidades de criação, listagem, edição e remoção de anotações aplicando o mesmo estilo (css);
2. Utilizar o PostgreSQL (em um container Docker) ao invés do SQLite;
3. Implementar o sistema de tags para as anotações;
4. Publicar a página.

A rubrica a seguir será utilizada na correção do Projeto 1B:

| Conceito | Descrição |
| :------: | :-------- |
|    A+    | Tarefas 1, 2, 3 e 4 completas e superou as expectativas (a combinar) |
|    A     | Tarefas 1, 2, 3 e 4 completas |
|    B+    | Tarefas 1, 2 e 3 completas |
|    B     | Tarefas 1 e 2 completas e uma das páginas da tarefa 3 |
|    C+    | Tarefas 1 e 2 completas |
|    C     | Tarefa 1 completa |
|    D     | O código funciona, mas a tarefa 1 não está completa |
|    I     | Não entregou ou o código não executa |

O conceito A+ será dado aos trabalhos que superarem as expectativas do conceito A. Ou seja, implementarem alguma funcionalidade adicional de complexidade acima do esperado para esta parte do projeto. Note que qualquer funcionalidade adicional só será considerada para o A+ e não pode aumentar nenhum dos outros conceitos.

É importante que você valide com a professora e deixe claro no README.md do seu repositório o que foi feito no projeto para alcançar o conceito A+.
