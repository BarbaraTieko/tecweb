# Django :simple-django:

No Projeto 1A implementamos uma aplicação Web utilizando apenas a linguagem Python e sem o uso de nenhum framework. 
O objetivo do projeto foi entender conceitos e o funcionamento da comunicação cliente-servidor.

Neste handout vamos dar nossos primeiros passos no desenvolvimento web usando o framework Django. Para isso, vamos refazer o backend da parte A do projeto.

!!! question choice
    Caso você queira desenvolver uma aplicação Web para algum projeto pessoal ou proficional, você utilizaria o código desenvolvido no **Projeto 1A**?

    - [ ] **SIM** :smile::thumbsup:
    - [X] **NÃO** :smiling_face_with_tear: :thumbsdown:
    

    !!! details "Resposta"
        Caso precisemos desenvolver uma aplicação web utilizando Python, o ideal seria **NÃO** utilizar o código desenvolvido no Projet 1A, pois o objetivo do projeto foi entender o funcionamento da comunicação cliente-servidor. Desta forma, o código do projeto 1A apresenta muitas limitações

        Além disso, para este handout não vamos reutilizar nenhum trecho de código do Projeto 1A. As únicas coisas que podem ser reutilizadas são o estilo CSS.

!!! question choice "Configuração Inicial"
    Antes de começar, vamos preparar o repositório do Projeto 1B.
    
    1. Acesso o link [Github Classroom](https://classroom.github.com/a/WqLD3zMW){target=_blank} para criar o repositório do **Projeto 1B**.
    2. Clone o repositório em seu computador.
    3. Crie um arquivo `.gitignore` com o conteúdo a seguir:
        ```
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
        .DS_Store
        ```
    4. Ao longo do handout, trabalhe dentro deste repositório.
    
    - [X] **FINALIZEI** as etapas listadas acima :thumbsup:
    - [ ] **NÃO FINALIZEI** as etapas listadas acima :thumbsdown:
    

    !!! details "Resposta"
        Para continuar o Handout é esperado que conclua as etapas listadas acima.


!!! note "Indo além ..."
    O Django possui **muitas** funcionalidades. O nosso objetivo neste handout é oferecer apenas uma introdução bastante breve. Você provavelmente vai precisar ler outros tutoriais, a documentação do Django e fazer pesquisas no Google para conseguir fazer o projeto.

    Conte com o professor para te ajudar com as dúvidas, mas é esperado que você desenvolva a maturidade para pesquisar e aprender o que falta por conta própria. Essa é uma habilidade essencial na vida de qualquer desenvolvedora/desenvolvedor.

!!! note "Versão do Django"
    Em Tecnologias Web nós utilizaremos o Django 5.X. É importante levar isso em conta quando for procurar respostas no Google. O [Django 5.0](https://docs.djangoproject.com/en/5.0/releases/5.0/) foi lançado no final de 2023, então será comum você encontrar respostas desatualizadas. **Sempre** que encontrar alguma função/método que não conhece, consulte a documentação da biblioteca para verificar se essa é a forma mais atualizada de se resolver o problema (essa dica vale para qualquer biblioteca/framework que for utilizar).

!!! info "Referência"
    Este handout é baseado no [tutorial disponível na própria documentação do Django](https://docs.djangoproject.com/en/5.0/intro/tutorial01/). A intenção é desenvolvê-lo de forma mais conectada com o que já fizemos na parte A do projeto, mas a documentação é muito mais completa e é possível se aprofundar mais em diversas questões. Recomendo a leitura (a documentação do Django é muito bem feita).

## Instalando o Django

Ao desenvolver projetos em Python é comum o uso de [ambientes virtuais :link:](https://docs.python.org/pt-br/3/tutorial/venv.html#virtual-environments-and-packages){:target="_blank"} que possibilita o gerenciamento das bibliotecas que serão utilizadas em nosso projeto.

Normalmente quando executamos o comando `pip install ALGUM_PACOTE`, instalamos a última versão disponível daquele pacote de forma global em nosso computador. Ao utilizar um ambiente virtual a instalação será feita apenas no ambiente virtual. 

!!! question choice "Criando o ambiente virtual"
    Para entender melhor, leia o material a seguir e efetue os comandos necessário para a criação de um ambiente virtual dentro da pasta do repositório Github do Projeto 1B, [crie um ambiente virtual](../auxiliar/venv.md){:target="_blank"}.

    - [X] **CRIEI** o ambiente virtual :thumbsup:
    - [ ] **NÃO CRIEI** o ambiente virtual :thumbsdown:
    
    !!! details "Resposta"
        Para continuar o Handout é esperado que conclua as etapas listadas acima.

!!! example "Instalando o Django"
    Com o ambiente virtual ativo, instale o Django:

        python -m pip install Django

??? example "Entendedo melhor ambiente virtual"
    Execute o seguinte comando no terminal cujo o ambiente virtual está ativo:
    ```bash
    pip list
    ```
    Caso você tenha instalado corretamente o Django, será impresso algo similar ao texto abaixo:

    ```
    Package  Version
    -------- -------
    asgiref  3.7.2
    Django   5.0.3
    pip      23.3.1
    sqlparse 0.4.4
    ```
    Ao instalar o Django, ele acaba instalando algums outras dependência, porém, o ambiente virtual possue somente os pacotes listados acima.

    Abra uma aba nova do terminal, onde o ambiente virtual não está ativo e execute o mesmo comando `pip list` (Não é necessário entrar em nenhum diretório específico).

    Ao executar o comando `pip list` fora do ambiente virtual, iremos listar todas os pacotes instalados no computador. Mas o pacote Django não deve ser listado, pois instalamos somente no ambiente virtual.


Para verificar se a instalação foi bem sucedida, inicie o Python em sua versão interativa (digite `python` no terminal) e utilize os seguintes comandos:

```python
import django
print(django.get_version())
```

O Django deve ter sido instalado em uma versão igual ou superior à 5.0.

Quando o Django estiver instalado, siga para o [primeiro passo](04-django/parte1.md).

## Índice do handout

Este handout está dividido nos passos a seguir:

- [Parte 1: Iniciando o projeto](04-django/parte1.md)
- [Parte 2: Criando nosso primeiro app](04-django/parte2.md)
- [Parte 3: Integrando com o banco de dados](04-django/parte3.md)
- [Parte 4: O Django Admin](04-django/parte4.md)
- [Parte 5: Usando templates](04-django/parte5.md)
- [Parte 6: Trabalhando com formulários e o método POST](04-django/parte6.md)
