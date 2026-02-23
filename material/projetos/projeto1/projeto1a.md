# Projeto 1: Parte A

!!! success "Entrega"
    :date: 05/03 (quinta-feira)
    
    :clock1: Commits até as 23:59

    :material-account-group: Individual

    :simple-github: Entrega via [ :point_right: GitHub Classroom](https://classroom.github.com/a/oj8U22BD){: target="_blank"}.
 
## Objetivos :octicons-goal-16:

Durante o primeiro handout nós desenvolvemos o [Get-it](../../aulas/01-getit.md) com as funcionalidades de listagem e criação de anotações. No [Desafio CSS](../../aulas/02-desafio-css.md) você implementou um possível estilo para a página. No segundo handout, você aprendeu a armazenar e recuperar dados de um banco de dados SQLite. Agora, no Projeto 1A, o seu objetivo é aplicar o que aprendeu nos handouts e no desafio para adicionar as seguintes funcionalidades ao sistema:

1. Estilo da página (utilizando o CSS que você já fez ou adicionando um novo estilo);
2. Armazenamento em banco de dados SQLite ao invés de um arquivo texto
3. Apagar anotações
4. Editar anotações

## Rubrica :material-check:

A rubrica a seguir será utilizada na correção do Projeto 1A:

| Conceito | Descrição |
| :------: | :-------- |
|    I     | Não entregou ou o código não executa |
|    D     | Entregou apenas o resultado do handout 01 funcionando e nada mais |
|    C     | Entregou o handout 01 e 1 das 4 tarefas funcionando |
|    C+    | Entregou o handout 01 e 2 das 4 tarefas funcionando |
|    B     | Entregou o handout 01 e 3 das 4 tarefas funcionando |
|    B+    | Entregou o handout 01 e as 4 tarefas funcionando    |
|    A     | Veja mais detalhes abaixo.|
|    A+    | Veja mais detalhes abaixo.|

## Conceito A

- Atingiu o conceito B+ e o repositório está organizado sem arquivos e códigos desnecessários. 
- Repositório possui commits contínuos e possui mensagens de commit claras e objetivas;
  - Ha pelo menos um commit por aula studio e um commit por funcionalidade; 
- Todos os itens do Handout 1 foram implementados;
- Implementou uma página HTML para o código 404;

## Conceito A+

- Lógica de deletar, editar e favoritar foram implementadas no arquivo `views.py`;
- Arquivo `servidor.py` possui a responsabilidade apenas de direcionar as requisições para o arquivo `views.py` de acordo com as rotas.
- Implementou a funcionalidade de favoritar anotações;
- Ordenou as anotações por favorito, ou seja, as anotações favoritas devem aparecer primeiro;


## Detalhes das Tarefas :material-magnify-plus-outline:

1. Veja mais descrições das tarefas que devem ser entregues no projeto [:point_right: Clique aqui](projeto1a/tarefas-projeto1a.md) para ver os detalhes das tarefas.