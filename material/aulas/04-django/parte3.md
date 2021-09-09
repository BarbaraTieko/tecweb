# Parte 3: Integrando com o banco de dados

No handout 2 nós começamos a utilizar o SQLite para armazenar os dados do sistema. Para interagir com o banco foi necessário construir as strings com os comandos SQL, misturando a sintaxe do Python com a do SQL. A boa notícia é que o Django já possui uma integração com o banco de dados pronta. Melhor ainda, é muito simples trocar o banco de dados utilizado (SQLite, PostgreSQL, MySQL, etc.).

Abra o arquivo `getit/settings.py`. Procure o seguinte trecho de código:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Esse dicionário está configurando o SQLite como o banco de dados da aplicação (será criado um banco de dados no arquivo `db.sqlite3` dentro da pasta principal do seu projeto). Se você quiser utilizar outro banco de dados, basta instalar as bibliotecas necessárias (em geral disponíveis para ser instaladas via `pip install`) e modificar os itens desse dicionário. Se quiser saber mais, consulte a [documentação do Django](https://docs.djangoproject.com/en/3.0/intro/tutorial02/#database-setup).

Já que estamos no arquivo de configuração, aproveite para procurar pela lista `#!python INSTALLED_APPS`. Ela deve ser parecida com essa:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Na [parte 2](parte2.md) comentamos que um projeto é composto por múltiplos apps, que são partes de um sistema. A lista `#!python INSTALLED_APPS` define os nomes dos apps utilizados pelo seu projeto. Por exemplo, há um app que é responsável por gerenciar arquivos estáticos (imagens, css, javascript, etc.), outro responsável pela autenticação (usuário, senha, mudança de senha) e assim por diante.

Nós já criamos um app para o nosso projeto, o `notes`. Vamos adicioná-lo na lista de apps nas configurações.

!!! example "Exercício"
    Adicione o `#!python 'notes.apps.NotesConfig'` como o primeiro elemento da lista `#!python INSTALLED_APPS`.

    ??? info "O que raios é `#!python 'notes.apps.NotesConfig'`?"
        Esse é o nome completo da classe de configuração. Ela foi criada automaticamente para você. Se tiver curiosidade, abra o arquivo `notes/apps.py`.

Como vimos, o nosso projeto já tem diversos apps instalados. Vários desses apps utilizam o banco de dados para armazenar pelo menos uma tabela. Para que essas tabelas sejam criadas vamos utilizar o comando (no terminal):

    python manage.py migrate

## Criando seus próprios modelos

Começamos esta parte do handout comentando que o Django já tem uma integração com o banco de dados. Para isso nós precisamos criar classes do Python para representar os nossos modelos, cujos dados serão armazenados em tabelas nos bancos de dados relacionais. Vamos criar o nosso primeiro modelo.

!!! example "Exercício"
    Substitua o conteúdo do arquivo `notes/models.py` por:

    ```python
    from django.db import models


    class Note(models.Model):
        title = models.CharField(max_length=200)
    ```

    Nesse código nós criamos um modelo chamado `#!python Note` que possui um atributo `#!python title`, que será mapeado no banco de dados em uma coluna cujos valores são strings de no máximo 200 caracteres.

!!! example "Exercício"
    Leia a [documentação do `#!python CharField`](https://docs.djangoproject.com/en/3.1/ref/models/fields/#charfield). Ele não é recomendável para textos grandes. Crie na classe `#!python Note` um atributo `#!python content` com o tipo apropriado.

    Existem diversos tipos de colunas que podem ser utilizados nos modelos. Por exemplo, relacionamentos entre entidades (tabelas) podem ser representados com o `models.ForeignKey` ou o `models.ManyToManyField`.

!!! danger "E o ID?"
    Como todas as tabelas precisarão de uma coluna para armazenar o identificador, o próprio Django se responsabiliza por criar essa coluna.

Nós acabamos de executar o comando `python manage.py migrate` para criar as tabelas dos apps no banco de dados. Como o nosso app `notes` também está entre os `#!python INSTALLED_APPS`, esse mesmo comando também vai criar a tabela do modelo `#!python Note`.

Antes disso, precisamos pedir para o Django criar as migrações. Uma migração é a forma do Django armazenar modificações no banco de dados (criação de novas tabelas, por exemplo). Para isso, execute o comando

    python manage.py makemigrations

Seguido por

    python manage.py migrate

O primeiro comando criou o script de criação da tabela que armazenará as anotações. O segundo comando aplicou esse script, efetivamente criando a tabela no banco de dados.

!!! info "Migrações"
    Imagine que ao longo do desenvolvimento do projeto você descobre que precisa armazenar uma informação adicional nas anotações. Ao modificar o modelo `#!python Note` será necessário adicionar essa coluna no banco de dados. O problema é que o banco de dados pode já possuir valores armazenados. O que fazer com eles? Como atualizá-los? Qual deve ser o valor padrão utilizado nessa nova coluna para as linhas já existentes no banco? As migrações se responsabilizam por esse processo, facilitando a evolução do banco de dados em produção.

Ok, nós criamos o banco de dados, mas como eu adiciono dados nele e vejo o que está armazenado? Boa pergunta! Siga para a [parte 4](parte4.md)!
