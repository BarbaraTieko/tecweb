# Django REST Framework

Já conversamos um pouco sobre REST na introdução da aula, mas para se aprofundar mais você pode encontrar [excelentes documentações na internet](https://restfulapi.net/){:target="_blank"}.

O objetivo deste handout é disponibilizarmos uma API REST utilizando o [Django REST Framework (DRF)](https://www.django-rest-framework.org/){:target="_blank"}. 

Vamos criar um projeto Django novo para isso. A estrutura inicial do projeto será bem parecida com a do projeto 1B, pois vamos utilizar o mesmo modelo de anotações. O que muda é que não vamos utilizar o Django para renderizar páginas HTML, mas sim para disponibilizar uma API REST.

## Criando o projeto

Crie uma pasta com o nome que desejar e no terminal entre dentro desta pasta que você acabou de criar. 

- Crie um ambiente virtual
- Ative o ambiente virtual
- Instale o Django

```bash
pip install django
```

- Crie um projeto Django com o nome `getit`:

```bash
django-admin startproject getit .
```

- Crie um app Django:

```bash
python manage.py startapp notes
```

- Atualize o arquivo `settings.py` do projeto para adicionar o app `notes` na lista de `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'notes',
]
```

- Reutilize o modelo `Note` do projeto 1B. Ou seja, copie o modelo `Note` do projeto 1B e cole no arquivo `notes/models.py` do projeto que você acabou de criar.

- Rode os comandos para criar o banco de dados e aplicar as migrações
- Crie um superusuário para acessar o admin do Django:

```bash
python manage.py createsuperuser
```
- Cadastre o modelo `Note` no admin do Django. Você precisará editar o arquivo `notes/admin.py`.
- Acesse a página do admin e crie algumas anotações. 

- Crie um arquivo chamado `urls.py` dentro do app `notes` e adicione o seguinte conteúdo:

```python
from django.urls import path

from . import views

urlpatterns = [
]
```

- Atualize o arquivo `urls.py` do projeto `getit` para incluir as URLs do app `notes`:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes.urls')),
]
```

Até aqui refizemos a parte inicial do projeto 1B. Agora vamos adicionar o Django REST Framework.


## Instalando o Django REST Framework

Instale o DRF e suas dependências:

```
pip install djangorestframework
pip install markdown
pip install django-filter
```

Precisamos indicar para o Django que queremos utilizar o DRF. Para isso, abra o `settings.py` do seu projeto e adicione `#!python 'rest_framework'` aos `#!python INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

## Criando nosso serializador

O objetivo do serviço RESTful é disponibilizar recursos para o cliente. No nosso caso vamos trabalhar com o formato JSON, então o serviço deve saber como representar objetos do modelo (no caso as anotações) no formato JSON. Esse é o papel dos serializadores. Crie um arquivo `notes/serializers.py` com o seguinte conteúdo:

```python
from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content']
```

A classe acima será utilizada pelo DRF para serializar objetos do tipo `#!python Note`. O JSON gerado conterá os atributos `'id'`, `'title'` e `'content'`.

!!! tip "O que é serialização?"
    Serialização é o processo de transformar um objeto em um formato que pode ser armazenado ou transmitido. No nosso caso, estamos transformando um objeto do tipo `Note` em um JSON. Poderiamos fazer a conversão manualmente, mas o DRF nos fornece uma forma mais fácil e padronizada de fazer isso.

## Criando as views da API

O projeto 1B possui rotas e views para renderizar páginas HTML e interagir com o usuário. Agora vamos criar rotas e views para interagir com outras aplicações, como um aplicativo mobile ou um projeto Frontend. 

O DRF disponibiliza uma forma bastante [enxuta de criação de views para APIs REST](https://www.django-rest-framework.org/api-guide/viewsets/){:target="_blank"}. Você pode (e até deve?) utilizá-la nos seus projetos, mas ela já encapsula alguns passos importantes. Como o nosso objetivo também é entender o que está acontecendo por baixo dos panos, vamos seguir pelo caminho mais longo.

Adicione ao arquivo `notes/views.py` as linhas a seguir:

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Note
from .serializers import NoteSerializer

@api_view(['GET', 'PUT'])
def api_note(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        raise Http404()
    serialized_note = NoteSerializer(note)
    return Response(serialized_note.data)
```

O código acima cria uma view do DRF que aceita GET e POST (vamos deixar o POST para depois). Quando uma requisição GET é recebida, a anotação é carregada do banco de dados, serializada utilizando a classe que criamos anteriormente e então o resultado é devolvido. Agora só falta criarmos a rota no `notes/urls.py`:

```python hl_lines="6"
from django.urls import path

from . import views

urlpatterns = [
    path('notes/<int:note_id>/', views.api_note),
]
```

Muito bem, agora execute o servidor e acesse a página na rota `notes/1` (assumindo que existe pelo menos uma anotação no banco de dados). Troque o número ´1´ por um id existente em seu banco de dados. O resultado deve ser parecido com este:

![](view.png)

O próprio DRF gera a página de visualização, mas você poderia fazer a requisição através de um código JavaScript, por exemplo, e a resposta seria o JSON apresentado.

### Implementando o POST

Deixamos o POST para depois, mas agora precisamos implementá-lo. Modifique a sua view adicionando as seguintes linhas:

```python hl_lines="10-14"
# O resto do código continua aqui pra cima

@api_view(['GET', 'PUT'])
def api_note(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        raise Http404()

    if request.method == 'PUT':
        new_note_data = request.data
        note.title = new_note_data['title']
        note.content = new_note_data['content']
        note.save()

    serialized_note = NoteSerializer(note)
    return Response(serialized_note.data)
```

A única diferença é que no caso do POST queremos editar o conteúdo de uma anotação. O `#!python request.data` possui os dados enviados pelo POST em um dicionário. Portanto, utilizamos esses dados para atualizar a anotação, salvamos e depois voltamos ao fluxo normal da função, devolvendo a anotação atualizada. Note que a única diferença com o caso do GET é que não passamos pelo passo de modificar o banco de dados.

Você pode testar o POST entrando na mesma página, preenchendo um dicionário (JSON) com algumas alterações e clicando em POST:

![](post.png)

## Agora é com você!

!!! example "Exercício 1"

    Implemente a funcionalidade de deletar uma anotação. 

    Agora que podemos utilizar outros métodos HTTP, implemente a funcionalidade de deletar uma anotação. Para isso, implemente a funcionalidade de deletar na função `api_note` (não é preciso criar outra função) e adicione a opção DELETE na lista de métodos aceitos pela função `api_note`.
    
    Neste caso, como deletamos a nota, não faz sentido retornar um json com as informações desta nota. Desta forma, tente descobrir como retornor um response com o código 204 (Código indica que o servidor realizou com sucesso a requisição, mas que não há nenhum conteúdo para retornar na resposta).

!!! example "Exercício 2"
    Implemente uma nova view do DRF para a rota `#!python notes/`. Ao receber uma requisição GET ela deve devolver a lista de todas as anotações. Ao receber um POST ela deve criar uma nova anotação e devolver a lista de todas as anotações incluindo a nova.

    **Dica:** você pode passar um argumento adicional ao serializador `#!python many=True` quando o primeiro argumento é uma lista de objetos ao invés de um único objeto. O serializador do DRF usa essa informação para criar o JSON corretamente. Para saber mais [leia a documentação](https://www.django-rest-framework.org/api-guide/serializers/#serializing-multiple-objects){:target="_blank"}.

O resultado esperado é algo semelhante a:

![](get_list.png)

## POSTMAN

Apesar de termos a visualização criada pelo DRF, pode ser útil usarmos ferramentas externas para nos auxiliar no desenvolvimento de APIs. O POSTMAN é uma ferramenta bastante utilizada para testes de APIs, portanto é interessante que você o conheca e saiba utilizá-lo minimamente.

Você pode instalar o POSTMAN a partir deste link: https://www.postman.com/downloads/

Depois de instalar, faça seu cadastro gratuitamente.

Depois de fazer o login, clique em "Create New":

![](postman1.png)

Digite a sua URL e clique em "GET":

![](postman2.png)

Os dados devem ser apresentados no quadro inferior. Você pode fazer requisições POST, salvar requisições para automatizar ou simplificar testes, entre muitas outras coisas. O nosso objetivo neste handout não é entrar nesses detalhes, mas recomendo que você [aprenda a utilizar esta ferramenta](https://learning.postman.com/){:target="_blank"}. Ela será uma adição valiosa ao seu kit de ferramentas de desenvolvimento.
