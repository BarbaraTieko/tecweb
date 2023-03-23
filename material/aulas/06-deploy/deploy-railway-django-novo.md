# Deploy da Aplicação

Até agora você desenvolveu as suas aplicações e testou o servidor localmente. Neste handout vamos aprender como publicar a nossa aplicação para que qualquer pessoa com acesso à internet possa acessá-la. Existem diversas opções de hospedagem disponíveis. Alguns exemplos são a [Amazon AWS](https://aws.amazon.com/), [DigitalOcean](https://www.digitalocean.com/), [PythonAnywhere](https://www.pythonanywhere.com/), [Linode](https://www.linode.com/), [Heroku](https://www.heroku.com/) ...

Para o projeto 1B vamos ver uma outra opções para fazer deploy. Lembrando que não há restrição para qual serviço devem utilizar. Estejam livres para utilizar o que preferirem.

!!! tip "Vídeo"
    Vídeo com algumas instruções para fazer o deploy: [https://www.youtube.com/watch?v=D58ug70Em8g](https://www.youtube.com/watch?v=D58ug70Em8g){:target="_blank"}

# Crie uma conta

Vamos utilizar o serviço [Railway](https://railway.app) que oferece um valor de $5 dólares para que possamos testar o serviço e o que é suficiente para o nosso projeto.

### Aplicações com Postgres

Caso sua aplicação utilize postgres, você deve seguir os passos abaixo.

Vamos instalar o `dj-database-url`:

    pip install dj-database-url

Sempre que você adiciona (ou remove) uma dependência é necessário atualizar o `requirements.txt`:

    pip freeze > requirements.txt

Adicione o `#!python import` no `settings.py`:

```python
import dj_database_url
```

Depois substitua o dicionário `#!python DATABASES` pelo código abaixo:

```python
DATABASES = {
    'default': dj_database_url.config(
        default='',
        conn_max_age=600,
        ssl_require=not DEBUG
    )
}
```

No campo **default** adicione a informação que apresentada no Postgres do Railway, campo **Postgres Connection URL**. Para mais detalhes veja o seguinte trecho do vídeo a seguir: [Vídeo](https://youtu.be/D58ug70Em8g?t=131){:target="_blank"}

Será necessário alterar um pouco a string obtida.
O padrão obtido no site do railway é `PGPASSWORD=<SENHA> psql -h containers-us-west-102.railway.app -U postgres -p 6025 -d railway`

Altere a sua string da seguinte forma: `postgresql://postgres:<SENHA>@containers-us-west-102.railway.app:6025/railway`

!!! tip "Vídeo"
    O vídeo também pode ser acessado em: [https://www.youtube.com/watch?v=D58ug70Em8g](https://www.youtube.com/watch?v=D58ug70Em8g){:target="_blank"}

## Configurando o projeto

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

!!! danger "Importante 2"
    O projeto Django deve estar na raiz do repositório github.
    ```
    > REPOSITÓRIO GIT
        > getit
        > notes
        manage.py
        requirements.txt
    ```

Até o momento, nós utilizamos o `python manage.py runserver` para executar o nosso servidor localmente. Esse comando é apropriado apenas para testes no ambiente de desenvolvimento. Ele não é otimizado para uma aplicação real. Para isso precisamos de um servidor de **Web Server Gateway Interface (WSGI)**, que basicamente é um intermediário entre as requisições que chegam no servidor e o código Python. No nosso projeto nós utilizaremos o [Gunicorn (Green Unicorn)](https://gunicorn.org/). Você pode instalá-lo com (**importante:** lembre-se de ativar o ambiente virtual):

    pip install gunicorn

!!! info "O arquivo `wsgi.py`"
    O comando acima executou o Gunicorn com o arquivo de configuração `getit/wsgi.py`. Normalmente não é necessário alterar esse arquivo, então não vamos entrar em detalhes. O que você precisa saber é que todo projeto Django possui um arquivo `wsgi.py` dentro da pasta do projeto.

Agora vamos definir o arquivo de configuração. Crie um arquivo chamado `Procfile` (o nome do arquivo não deve ter extensão nenhuma - cuidado se for criar o arquivo em algum editor de texto, pois alguns colocam o `.txt` automaticamente) na raiz do projeto com o seguinte conteúdo:

```
release: python manage.py migrate
web: gunicorn getit.wsgi
```

A primeira linha faz com que o comando de migração do Django seja executado quando o servidor for carregado. A segunda linha especifica como a aplicação deve ser executada.

!!! danger
    Provavelmente o seu projeto Django possui outro nome, então você deve alterar a linha **web: gunicorn getit.wsgi** por **web: gunicorn NOME_DO_SEU_PROJETO.wsgi**

### Outras modificações nas configurações

Aproveite que está com o `settings.py` aberto e modifique o valor da constante `DEBUG` para `False`. Além disso, procure pela lista `ALLOWED_HOSTS`. Ela deve ser uma lista vazia.

```python
ALLOWED_HOSTS = ['*']
```

Quando tivermos o host gerado vamos alterar o *ALLOWED_HOSTS*  para adicionar o nome do host gerado, `#!python 'localhost'` e o `#!python '127.0.0.1'`.

```python
ALLOWED_HOSTS = ['NOME_DO_HOST_GERADO', 'localhost', '127.0.0.1']
```

### Criando o arquivo `requirements.txt`

Vamos gerar o `requirements.txt`

    pip freeze > requirements.txt

!!! danger "Importante"
    Note que você deverá executar o comando `pip install -r requirements.txt` com o ambiente virtual ativado. Após rodar o comando verifique o arquivo `requirements.txt` que foi criado. Este arquivo deve possuir no máximo 10 linhas. Se esse arquivo possuir muito mais linhas é possível que você não rodou com ambiente virtual ativo.

Faça o commit das mudanças do seu projeto.

### Último passo

Vá no site do Railway para escolher o repositório github do projeto para fazer o deploy. Para mais detalhes veja o [vídeo](https://youtu.be/D58ug70Em8g?t=249){:target="_blank"}.

## Referências

- Deploying to Heroku Server | Django (3.0) Crash Course Tutorials (pt 23): https://www.youtube.com/watch?v=kBwhtEIXGII
- Deploy a Django App to Heroku: https://www.youtube.com/watch?v=GMbVzl_aLxM
- Heroku Postgres - connecting with Django: https://devcenter.heroku.com/articles/heroku-postgresql#connecting-with-django
- Heroku - Django migrations: https://help.heroku.com/GDQ74SU2/django-migrations
- Heroku - Working with Django: https://devcenter.heroku.com/categories/working-with-django
