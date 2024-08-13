# 03 - Persistência de Dados

!!! danger "Rodando os testes"
    Acesse o link a seguir para rodar os testes [https://us.prairielearn.com/pl/course_instance/157660/assessment/2438387](https://us.prairielearn.com/pl/course_instance/157660/assessment/2438387)

Depois das duas últimas aulas, a nossa página já está minimamente utilizável. O usuário consegue fazer uma requisição, o servidor carrega ou salva os novos dados em arquivos e depois devolve a resposta para o navegador.

Opa! Espere um pouco. Arquivos?!

É, arquivos. Por quê? Tem algum problema com isso?

Vamos pensar um pouco sobre isso. :thinking:

## Qual o problema de usar arquivos para armazenar os dados da nossa aplicação? 

### Cenário 1

Imagine que a sua aplicação já está sendo utilizada há um tempo e o arquivo que contém os dados é razoavelmente grande. Seu servidor recebe uma requisição pedindo para atualizar uma informação que está armazenada no arquivo. O arquivo é aberto, o elemento a ser modificado é identificado e, enquanto o arquivo é salvo, ocorre um erro no computador, interrompendo a gravação do arquivo. Ao tentar acessar novamente o arquivo você descobre que ele está corrompido e todos os dados foram perdidos.

### Cenário 2

Sua página fica muito popular e passa a receber milhares de acessos por segundo. O arquivo contendo os dados demora 1 milissegundo para ser aberto e lido e ele pode ser aberto por apenas um processo por vez. Como apenas uma requisição pode ter o arquivo aberto de cada vez, em poucos segundos a sua aplicação para de responder. Você está recebendo mais requisições do que dá conta de responder.

Você decide armazenar os dados na memória e apenas abrir o arquivo para salvar novas modificações. Duas requisições de modificação são enviadas simultaneamente e uma sobrescreve o que a outra acabou de escrever. Os dados da primeira requisição são perdidos.

### Cenário 3

Seu arquivo de dados já ocupa alguns gigabytes. Toda vez que algum usuário pede uma informação você precisa ler todo o arquivo em busca dela.

### A solução

Você decide que para resolver todos esses problemas vai criar um módulo responsável por lidar com escritas simultâneas (concorrentes) de dados, armazenamento de backups em caso de falhas, indexação dos dados para acelerar buscas, realizar o controle do acesso aos dados e tratar de diversos outros detalhes relacionados ao armazenamento. Parabéns, você acabou de implementar um sistema de gerenciamento de bancos de dados!

## Bancos de Dados

Nosso objetivo em Tecnologias Web não é entrar em detalhes sobre bancos de dados. Deixamos isso para vocês trabalharem em Megadados. Aqui nós teremos apenas um primeiro contato, possibilitando o armazenamento e recuperação dos dados de forma mais robusta do que utilizando apenas arquivos.

Um dos tipos mais tradicionais de bancos de dados são os **bancos de dados relacionais**. A ideia é que cada "tipo de dado" é armazenado separadamente em uma tabela e as relações entre os objetos (chamados de **entidades**) são indicadas por identificadores únicos que permitem a localização do objeto relacionado na outra tabela. Ou seja, é um modelo que depende fortemente da representação dos dados como um conjunto de tabelas. Para interagir (criar, modificar, recuperar, deletar) com esse conjunto de tabelas foi criada uma linguagem chamada *Structured Query Language* (SQL).

Como comentamos anteriormente, o nosso objetivo é começar a utilizar SQL em nossas aplicações. Não temos a intenção de desenvolver nenhum estudo aprofundado sobre SQL ou bancos de dados **ainda**. Neste handout teremos nosso primeiro contato com o SQL através de um banco de dados chamado [SQLite](https://www.sqlite.org/index.html).

!!! danger "Importante"
    Você não deve utilizar o SQLite em um servidor web real. [Ele não foi feito para isso](https://sqlite.org/whentouse.html). Para ambientes de produção utilize sistemas mais robustos como o PostgreSQL, MySQL, ou SQL Server. Dito isso, os conceitos de SQL que veremos neste handout são os mesmos utilizados nesses outros sistemas. Optamos pelo SQLite por ele ser mais fácil de instalar e configurar.

## Próximos passos

O handout é divido nos seguintes passos:

- [Parte 1: Instalando o SQLite](03-persistencia-de-dados/parte1.md)
- [Parte 2: Criando a tabela](03-persistencia-de-dados/parte2.md)
- [Parte 3: Inserindo dados na tabela](03-persistencia-de-dados/parte3.md)
- [Parte 4: Consultando e selecionando dados](03-persistencia-de-dados/parte4.md)
- [Parte 5: Atualizando os dados](03-persistencia-de-dados/parte5.md)
- [Parte 6: Apagando dados](03-persistencia-de-dados/parte6.md)
