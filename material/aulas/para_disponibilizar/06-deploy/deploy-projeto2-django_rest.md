# Deploy - Projeto 2 (Django REST)

## Primeiros passos

Para começar o processo de deploy, crie uma conta no [Heroku](https://www.heroku.com/).

Instale a interface de linha de comando (CLI) do Heroku: [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).

Faça o login na sua conta do Heroku pelo terminal com o comando (você será redirecionado para a página do Heroku para completar o login):

    heroku login

Agora você pode criar uma aplicação utilizando o comando (a documentação dos comandos está [disponível aqui](https://devcenter.heroku.com/articles/heroku-cli-commands)):

    heroku create

Esse comando vai criar uma aplicação com nome aleatório e vai imprimir no terminal algo parecido com isso:

```
Creating app... done, ⬢ still-cove-69163
https://still-cove-69163.herokuapp.com/ | https://git.heroku.com/still-cove-69163.git
```

No exemplo acima, a aplicação se chama `still-cove-69163`. Guarde o nome da sua aplicação.

??? info "Criando uma aplicação com nome específico"
    Você pode escolher o nome da sua aplicação com o comando `heroku create nome-da-aplicacao`, mas ele precisa ser único **em todo o Heroku**, ou seja, ninguém pode ter criado um projeto com o mesmo nome.

Entre na pasta do seu projeto pelo terminal.


!!! danger "Importante"
    Seu projeto deve estar no git. Se não estiver, crie um repositório antes de seguir para os próximos passos deste handout.

    Quando for criar o repositório, adicione um arquivo chamado `.gitignore` com o seguinte conteúdo:

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
    ```

O deploy da aplicação é iniciado automaticamente a partir de atualizações em um repositório git do Heroku. Para configurar esse repositório no seu projeto, utilize o comando (**importante 1:** execute este comando na pasta raiz do seu projeto; **importante 2:** troque o `still-cove-69163` pelo nome do seu app gerado pelo Heroku):

    heroku git:remote -a <nome do app>

Para confirmar se está tudo certo, utilize o comando:

    git remote -v

Ele deve listar (além de outros) os seguintes repositórios (claro, com o nome do seu app):

```
heroku	https://git.heroku.com/still-cove-69163.git (fetch)
heroku	https://git.heroku.com/still-cove-69163.git (push)
```

## Preparando o projeto

Até o momento, nós utilizamos o `python manage.py runserver` para executar o nosso servidor localmente. Esse comando é apropriado apenas para testes no ambiente de desenvolvimento. Ele não é otimizado para uma aplicação real. Para isso precisamos de um servidor de **Web Server Gateway Interface (WSGI)**, que basicamente é um intermediário entre as requisições que chegam no servidor e o código Python. No nosso projeto nós utilizaremos o [Gunicorn (Green Unicorn)](https://gunicorn.org/). Você pode instalá-lo com (**importante:** lembre-se de ativar o ambiente virtual):

    pip install gunicorn


Agora vamos definir o arquivo de configuração do Heroku. Crie um arquivo chamado `Procfile` (o nome do arquivo não deve ter extensão nenhuma - cuidado se for criar o arquivo em algum editor de texto, pois alguns colocam o `.txt` automaticamente) na raiz do projeto com o seguinte conteúdo:

```
release: python manage.py migrate
web: gunicorn <NOME DO SEU PROJETO>.wsgi
```

A primeira linha faz com que o comando de migração do Django seja executado quando o servidor for carregado. A segunda linha especifica como a aplicação deve ser executada.


### Configurando os arquivos estáticos

Como estamos dando deploy em uma API REST, não estamos trabalhando arquivos estáticos. No handout de Deploy da aplicação Django utilizávamos o pacote `whitenoise`, agora queremos dizer para o heroku que não vamos utilizar arquivos estáticos.

Para isso, basta executar o comando a seguir:

```
heroku config:set DISABLE_COLLECTSTATIC=1
```
### Outras modificações nas configurações

Aproveite que está com o `settings.py` aberto e modifique o valor da constante `DEBUG` para `False`. Além disso, procure pela lista `ALLOWED_HOSTS`. Ela deve ser uma lista vazia. Por questões de segurança, o servidor Django aceita apenas requisições vindas de domínios previamente identificados. Para isso, descubra qual é o domínio do seu app Heroku. A URL do app será parecida com essa: `https://still-cove-69163.herokuapp.com/` (lembrando que `still-cove-69163` é o nome da minha aplicação, então você terá que trocar o começo pelo nome gerado para a sua aplicação). Adicione o domínio (o que está entre o `https://` e a última `/`) na lista `ALLOWED_HOSTS`:

```python
ALLOWED_HOSTS = ['still-cove-69163.herokuapp.com', 'localhost', '127.0.0.1']
```

Note que também adicionamos o `#!python 'localhost'` e o `#!python '127.0.0.1'`. Eles serão necessários para você testar a aplicação no seu computador.

### Configurando o Postgres
Lembre-se de configura o dicionário `#!python DATABASES` nas configurações.
Lembre de instalar o `dj-database-url`:

    pip install dj-database-url

Sempre que você adiciona (ou remove) uma dependência é necessário atualizar o `requirements.txt`:

    pip freeze > requirements.txt

Adicione o `#!python import` no `getit/settings.py`:

```python
import dj_database_url
```

Depois substitua o dicionário `#!python DATABASES` por (lembre-se de utilizar as configurações do seu projeto):

```python
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://localhost/<NAME>?user=<USER>&password=<PASSWORD>',
        conn_max_age=600,
        ssl_require=not DEBUG
    )
}
```

### Criando o arquivo `requirements.txt`

Cada projeto Python possui dependências diferentes. Quando outra pessoa (ou você mesmo em outro computador) vai executar o seu projeto é necessário executar uma série de `pip install` com cada uma das dependências. Para simplificar esse processo podemos criar o arquivo `requirements.txt`. Com esse arquivo basta executar `pip install -r requirements.txt` para instalar todas as dependências do projeto. O Heroku também utiliza esse mesmo arquivo para configurar o seu projeto no servidor deles. O `requirements.txt` é basicamente um arquivo texto com a lista das dependências. Ele pode ser criado com o comando:

    pip freeze > requirements.txt

## Fazendo o deploy

Agora estamos prontos para fazer o deploy! **Faça um commit com todas essas modificações** e depois faça o push com o comando a seguir:

    git push heroku master

!!! danger "Se o comando acima não funcionar"
    Tente rodar o comando:
    ```
    git push heroku main
    ```

Esse processo é um pouco demorado, pois o Heroku vai baixar o código da sua aplicação, aplicar as configurações e executar o servidor.
