# Deploy - Projeto 2 Backend

No Projeto 1B fizemos o deploy utilizando o Heroku por oferecer a opção gratuita para projetos pequenos. Porém, a partir do dia 28 de novembro de 2022 a opção gratuita será descontinuada. Para o Projeto 2 você ainda conseguirá utilizar o Heroku, mas caso queira, este handout oferece uma outra alternativa.

Além disso, existem outros serviços que oferecem este tipo de serviço. Desta forma, para o projeto 2 você pode utilizar qualquer alternativa que desejar.

# Deploy da Aplicação - Python Django REST

Neste handout vamos fazer o deploy da aplicação Django REST utilizando a [Fly.io](https://fly.io/) que ofereço uma opção gratuita para pequenos projetos.

## Preparando o projeto

Lembre de instalar o Gunicorn [Green Unicorn](https://gunicorn.org/) para utilizarmos no projeto.

      pip install gunicorn

### Outras modificações nas configurações

Aproveite que está com o `settings.py` aberto e modifique o valor da constante `DEBUG` para `False`. Além disso, procure pela lista `ALLOWED_HOSTS`. Ela deve ser uma lista vazia. Por questões de segurança, o servidor Django aceita apenas requisições vindas de domínios previamente identificados.

Escolha o nome da sua aplicação. Lembre de utilizar um nome sem espaços, esse nome você informará posteriormente.
Para este exemplo, será utilizado o nome `django-rest-2022`. Desta forma, o `ALLOWED_HOSTS` ficará da seguinte forma:


```python
ALLOWED_HOSTS = ['django-rest-2022.fly.dev', 'localhost', '127.0.0.1']
```

Note que também adicionamos o `#!python 'localhost'` e o `#!python '127.0.0.1'`. Eles serão necessários para você testar a aplicação no seu computador.

### Criando o arquivo `requirements.txt`

Atualize as dependências do projeto com o comando abaixo:

    pip freeze > requirements.txt

!!! danger "Importante"
    Note que você deverá executar o comando `pip install -r requirements.txt` com o ambiente virtual ativado.

### Postgres


Instale o `dj-database-url`:

    pip install dj-database-url

Sempre que você adiciona (ou remove) uma dependência é necessário atualizar o `requirements.txt`:

    pip freeze > requirements.txt

Adicione o `#!python import` no `getit/settings.py`:

```python
import dj_database_url
```

Depois substitua o dicionário `#!python DATABASES` por (assumindo que você utilizou a configuração do Postgres apresentada no handout anterior - caso contrário, adapte a URL):

```python
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://localhost/getit?user=getituser&password=getitsenha',
        conn_max_age=600,
        ssl_require=not DEBUG
    )
}
```

## Fazendo o deploy

1. Para começar o processo de deploy, crie uma conta no [Fly.io](https://fly.io/).

2. Instale a interface de linha de comando (CLI) do Fly.io: [Fly.io CLI](https://fly.io/docs/hands-on/install-flyctl/).


    === "Windows PowerShell"

        `iwr https://fly.io/install.ps1 -useb | iex`

    === "MacOS"

        `brew install flyctl`

    === "Linux"

        `curl -L https://fly.io/install.sh | sh`


3. Faça o login na sua conta do Fly.io pelo terminal com o comando:

    fly auth login

4. Crie um arquivo chamado `Dockerfile` com o conteúdo abaixo. **Importante:** Modifique o valor `getit` em `getit.wsgi` pelo nome do projeto Django. Caso não saiba o nome do seu projeto, o nome é o mesmo que foi utilizado no comando `django-admin startproject getit .`, por exemplo.

    ```terminal hl_lines="23"
    ARG PYTHON_VERSION=3.10-slim-buster

    FROM python:${PYTHON_VERSION}

    ENV PYTHONDONTWRITEBYTECODE 1
    ENV PYTHONUNBUFFERED 1

    RUN mkdir -p /app

    WORKDIR /app

    COPY requirements.txt /tmp/requirements.txt

    RUN set -ex && \
        pip install --upgrade pip && \
        pip install -r /tmp/requirements.txt && \
        rm -rf /root/.cache/

    COPY . /app/

    EXPOSE 8000

    CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "getit.wsgi"]
    ```

      O arquivo [Dockerfile](https://docs.docker.com/engine/reference/builder/) é utilizado para construir Docker image que são utilizados para construir containers.
      Note que o arquivo Dockerfile possui instruções que serão executadas para construir um container.
      Este método é muito utilizado para fazer deploy de aplicações.

      Mas não precisa se preocupar caso não entenda os comandos contidos no arquivo acima.
      Esta etapa será melhor abordada em outras disciplinas.

5. Utilize o comando `fly launch`.
    Será preciso responder algumas perguntas.

    ```
    ? Overwrite "../Dockerfile"? No

    ? Create .dockerignore from 1 .gitignore files? Yes

    ? App Name (leave blank to use an auto-generated name): NOME_DO_SEU_APP

    ? Select region: gru (São Paulo)

    ? Would you like to set up a Postgresql database now? Yes

    ? Select configuration: Development - Single node, 1x shared CPU, 256MB RAM, 1GB disk
    ```

6. Agora rode o comando `fly deploy`
7. E para abrir o endereço da aplicação rode: `fly open`

## Referências

- Django Hello, World + Fly.io Deployment: https://learndjango.com/tutorials/django-hello-world-flyio-deployment
