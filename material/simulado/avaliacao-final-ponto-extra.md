# Preparação Avaliação Final

Para ganhar 1 ponto na prova da avaliação final você deve seguir os passos abaixo:

- Crie o repositório do github classroom para a prova no link: [https://classroom.github.com/a/qQ7c8wvV](https://classroom.github.com/a/qQ7c8wvV){:target="_blank"}

- Clone o repositório em seu computador;

- Crie uma pasta chamada `frontend` e cole dentro desta pasta os arquivos do projeto React entregues no Projeto 2;

- Crie uma pasta chamada `backend` e cole dentro desta pasta os arquivos do projeto Django entregues no Projeto 2;

- Crie um arquivo `.gitignore` na raíz do repositório com o seguinte conteúdo:

        env/
        *.egg-info
        *.pot
        *.py[co]
        .tox/
        __pycache__
        MANIFEST
        dist/
        docs/_build/
        docs/locale/
        node_modules/
        tests/coverage_html/
        tests/.coverage
        build/
        tests/report/

        # MacOS files
        .DS_Store

        # Dependency directories
        node_modules/


- Caso o projeto Django esteja com configurações para deploy, faça as alterações necessárias para rodar localmente;

- Caso o projeto React esteja fazendo requisições para o projeto backend Django, altere as rotas o `localhost`;

- Crie um ambiente virtual para o projeto backend;

- Teste o projeto para verificar se tudo está funcionando corretamente;

- Feitas as alterações acima, mostre para a professora para validar o ponto;


Note que a nota máxima da prova são 10 pontos;