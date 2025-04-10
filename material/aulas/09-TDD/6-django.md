# Testando APIs Django REST com pytest e Mocks

Assim como qualquer outro código, APIs Django REST precisam ser testadas para garantir que funcionem corretamente. No entanto, testar APIs que dependem de um banco de dados real pode ser complicado. Felizmente, já temos todas as ferramentas necessárias!


Para esse exemplo, vamos considerar o resultado do handout anterior.

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Note
from .serializers import NoteSerializer

@api_view(['GET'])
def api_note(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        raise Http404()
    
    serialized_note = NoteSerializer(aluno)
    return Response(serialized_note.data)

```

Neste exemplo, temos uma API Django REST que se conecta a um banco de dados SQlite3 para obter informações sobre notes. A rota `/alunos` retorna uma lista de alunos do banco de dados.

## 📌 **Introdução**
Testar APIs Django REST é essencial para garantir que as rotas funcionam corretamente e retornam as respostas esperadas. No entanto, como essa API depende de um **banco de dados SQlite3**, precisamos garantir que os testes **não dependam de um banco real**.

## 🧪 Objetivo dos testes

- Simular uma requisição `GET /notes/<id>/`
- Testar dois cenários:
    - Quando o aluno existe
    - Quando o aluno não existe (erro 404)

## **1️⃣ Configuração do Ambiente de Teste**
- No projeto que você criou no handout anterior, instale o **pytest** e o **pytest-django**:
```sh
pip install pytest pytest-django
```
- Crie um arquivo `notes/test/unit/test_views.py` para armazenar os testes.
- Crie um arquivo de configuração do pytest chamado **`pytest.ini`** na raiz do projeto com o seguinte conteúdo:
```ini
[pytest]
DJANGO_SETTINGS_MODULE = getit.settings
python_files = tests.py test_*.py
```


## **2️⃣ Criando o Teste de Unidade para a Rota `/notes/ID`**
O objetivo do teste é:

- Simular uma requisição **GET** para `/notes/ID`.
- Garantir que a API retorna os dados esperados.
- Substituir a conexão com o banco de dados por um **Mock** para que o teste rode sem um banco real.

```python
from unittest.mock import patch, MagicMock
from rest_framework.test import APIRequestFactory
from notes.views import api_note


@patch("notes.views.Note")
@patch("notes.views.NoteSerializer")
def test_api_note_unit(mock_serializer_class, mock_note_model):
    # Simula o objeto Note retornado por Note.objects.get
    mock_note = MagicMock()
    mock_note_model.objects.get.return_value = mock_note

    # Simula o serializer retornando um dicionário de dados
    mock_serializer = MagicMock()
    mock_serializer.data = {
        "id": 1,
        "title": "Receita de miojo",
        "content": "Bata com um martelo antes de abrir o pacote."
    }
    mock_serializer_class.return_value = mock_serializer

    # Cria uma requisição simulada
    factory = APIRequestFactory()
    request = factory.get("/notes/1/")

    # Chama a view diretamente
    response = api_note(request, note_id=1)

    # Verificações
    assert response.status_code == 200
    assert response.data["id"] == 1
    assert response.data["title"] == "Receita de miojo"
    assert response.data["content"] == "Bata com um martelo antes de abrir o pacote."
```

### **📌 Explicando o Teste**

- **`@patch("notes.views.Note")`**: Substitui a classe `Note` pelo Mock, evitando a conexão com o banco de dados.
- **`@patch("notes.views.NoteSerializer")`**: Substitui o `NoteSerializer` pelo Mock, evitando a necessidade de serializar o objeto real.
- **`mock_note_model.objects.get.return_value = mock_note`**: Simula o retorno do método `get` da classe `Note`, retornando um objeto Mock.
- **`mock_serializer.data = {...}`**: Simula os dados que o serializer retornaria.
- **`factory = APIRequestFactory()`**: Cria uma instância do `APIRequestFactory`, que permite criar requisições simuladas.
- **`request = factory.get("/notes/1/")`**: Cria uma requisição GET simulada para a rota `/notes/1/`.
- **`response = api_note(request, note_id=1)`**: Chama a view `api_note` diretamente, passando a requisição simulada e o ID do aluno.
- **`assert response.status_code == 200`**: Verifica se o código de status da resposta é `200 OK`.
- **`assert response.data["id"] == 1`**: Verifica se o ID retornado na resposta é `1`.
- **`assert response.data["title"] == "Receita de miojo"`**: Verifica se o título retornado na resposta é `"Receita de miojo"`.
- **`assert response.data["content"] == "Bata com um martelo antes de abrir o pacote."`**: Verifica se o conteúdo retornado na resposta é `"Bata com um martelo antes de abrir o pacote."`.

## **📌 Rodando o Teste**

## Rodando o teste

Para rodar o teste, execute o seguinte comando no terminal:

```sh
pytest
```

Se tudo der certo, você verá uma saída semelhante a esta:

```
================================================= test session starts ==================================================
platform darwin -- Python 3.12.1, pytest-8.3.5, pluggy-1.5.0
django: version: 5.2, settings: getit.settings (from ini)
rootdir: /Users/barbaraagena/Desktop/2025.1/tecweb/handouts/django-rest
configfile: pytest.ini
plugins: django-4.11.1
collected 1 item                                                                                                       

notes/tests/test_views.py .                                                                                      [100%]

================================================== 1 passed in 0.14s ===================================================
```

Isso significa que o teste passou com sucesso! 🎉


## **2️⃣ Testando o Caso de Erro (Note Não Encontrado)**

```python
def test_api_note_404_unit():
    factory = APIRequestFactory()
    request = factory.get("/notes/999/")

    with patch("notes.views.Note.objects.get") as mock_get:
        # Simula que Note.objects.get lança a exceção de "não encontrado"
        mock_get.side_effect = Note.DoesNotExist
       
        response = api_note(request, note_id=999)
        assert response.status_code == 404
```

### **📌 Explicando o Teste**

- **`factory = APIRequestFactory()`**: Cria uma instância do `APIRequestFactory`, que permite criar requisições simuladas.
- **`request = factory.get("/notes/999/")`**: Cria uma requisição GET simulada para a rota `/notes/999/`.
- **`with patch("notes.views.Note.objects.get") as mock_get:`**: Substitui o método `get` da classe `Note` por um Mock.
- **`mock_get.side_effect = Exception("Note matching query does not exist.")`**: Simula que o método `get` lança uma exceção quando o aluno não é encontrado.
- **`response = api_note(request, note_id=999)`**: Chama a view `api_note` diretamente, passando a requisição simulada e o ID do aluno.
- **`assert response.status_code == 404`**: Verifica se o código de status da resposta é `404 Not Found`.



## **Criando Teste de Integração com pytest e Django REST**

Agora que já temos os testes de unidade, vamos criar um teste de integração para a rota `/notes/<id>/`. Esse teste vai utilizar o banco de dados real, testando a API como um todo.

Vamos realizar os mesmos testes que fizemos antes, mas agora com o banco de dados real. Para isso, vamos usar o `pytest-django`, que já vem configurado para rodar os testes com um banco de dados temporário.

Crie um arquivo `notes/test/integration/test_api_note.py` e adicione o seguinte código:




### **📌 Código do Teste**
```python
import pytest
from rest_framework.test import APIClient
from notes.models import Note


@pytest.mark.django_db
def test_api_note_200():
    note = Note.objects.create(title="Receita de miojo", content="Bata com um martelo antes de abrir o pacote. Misture o tempero, coloque em uma vasilha e aproveite seu snack :)")
    client = APIClient()
    response = client.get(f"/notes/{note.id}/")
    assert response.status_code == 200
    assert response.data['id'] == note.id
    assert response.data['title'] == note.title
    assert response.data['content'] == note.content


@pytest.mark.django_db
def test_api_note_404():
    client = APIClient()
    response = client.get("/notes/999/")
    assert response.status_code == 404

```


### **3️⃣ Explicando o Teste**

- **`@pytest.mark.django_db`**: Essa marcação indica que o teste pode acessar o banco de dados. Isso é necessário para criar e manipular objetos do modelo `Note`.
- **`client = APIClient()`**: Cria um cliente de teste que simula requisições HTTP para a API.
- **`response = client.get(f"/notes/{note.id}/")`**: Faz uma requisição GET para a rota `/notes/<id>/`, onde `<id>` é o ID do aluno criado.
- **`assert response.status_code == 200`**: Verifica se o código de status da resposta é `200 OK`.
- **`assert response.data['id'] == note.id`**: Verifica se o ID retornado na resposta é o mesmo que o ID do aluno criado.
- **`assert response.data['title'] == note.title`**: Verifica se o título retornado na resposta é o mesmo que o título do aluno criado.
- **`assert response.data['content'] == note.content`**: Verifica se o conteúdo retornado na resposta é o mesmo que o conteúdo do aluno criado.



## **📌 Conclusão**
✅ Aprendemos a criar testes de unidade e de integração para APIs Django REST.
✅ Aprendemos que os testes de unidade não utilizam um banco de dados real, enquanto os testes de integração utilizam um banco de dados temporário.
✅ Usamos **Mocks** nos testes de unidade para simular conexões com o banco e diferentes cenários.  
✅ Agora temos testes que garantem que a API funciona corretamente! 🚀  

Isso facilita a **manutenção do código**, garantindo que a API continue funcionando conforme esperado, mesmo com futuras mudanças. 🚀

## 📊 Diferença entre Teste de Integração e Teste Unitário

| Característica                 | Teste de Integração                              | Teste Unitário                                 |
|-------------------------------|--------------------------------------------------|------------------------------------------------|
| Usa banco de dados real       | ✅ Sim                                           | ❌ Não (usa mocks)                             |
| Acessa a API via HTTP         | ✅ Sim (com `APIClient`)                         | ❌ Não (chama a view diretamente)              |
| Testa múltiplos componentes   | ✅ Sim (view, modelo, serializer, URL, etc.)     | ❌ Não (isola apenas um componente)            |
| Velocidade                    | 🐢 Mais lento                                    | ⚡ Mais rápido                                 |
| Complexidade do teste         | ✅ Mais realista e completo                      | ✅ Mais isolado e específico                   |
| Ideal para                    | Validar o comportamento final da aplicação      | Verificar lógica interna de funções/classe     |
| Quando usar                   | Antes do deploy, para testar o sistema todo     | Durante o desenvolvimento, para checar lógica |



Agora que você já aprendeu tudo sobre testes automáticos, que tal praticar um pouco mais? Vamos para os [**Exercícios no Prairie Learn**](https://us.prairielearn.com/pl/course_instance/177857/assessment/2509997){:target="_blank"}!


## Os outros testes de integração

No arquivo `notes/test/integration/test_api_note.py`, adicione os seguintes testes para testar os outros métodos da API:

```python


@pytest.mark.django_db
def test_api_note_put():
    note = Note.objects.create(
        title="Antigo título", content="Antigo conteúdo"
    )
    client = APIClient()
    updated_data = {
        "title": "Novo título",
        "content": "Novo conteúdo"
    }

    response = client.put(f"/notes/{note.id}/",
                          data=updated_data, format='json')
    assert response.status_code == 200
    assert response.data['title'] == updated_data['title']
    assert response.data['content'] == updated_data['content']

    note.refresh_from_db()
    assert note.title == updated_data['title']
    assert note.content == updated_data['content']


@pytest.mark.django_db
def test_api_note_delete():
    note = Note.objects.create(
        title="Título qualquer", content="Conteúdo qualquer"
    )
    client = APIClient()
    response = client.delete(f"/notes/{note.id}/")
    assert response.status_code == 204
    # Verifica se a nota foi realmente deletada
    assert Note.objects.filter(id=note.id).count() == 0


@pytest.mark.django_db
def test_api_notes_get():
    note1 = Note.objects.create(title="Nota 1", content="Conteúdo 1")
    note2 = Note.objects.create(title="Nota 2", content="Conteúdo 2")

    client = APIClient()
    response = client.get("/notes/")

    assert response.status_code == 200
    assert isinstance(response.data, list)
    assert len(response.data) == 2

    titles = [note['title'] for note in response.data]
    contents = [note['content'] for note in response.data]

    assert note1.title in titles
    assert note2.title in titles
    assert note1.content in contents
    assert note2.content in contents


@pytest.mark.django_db
def test_api_notes_post():
    # Cria uma nota inicial
    Note.objects.create(title="Nota Antiga", content="Conteúdo Antigo")

    client = APIClient()
    new_note_data = {
        "title": "Nova Nota",
        "content": "Este é o conteúdo da nova nota"
    }

    response = client.post("/notes/", data=new_note_data, format='json')

    assert response.status_code == 201
    assert isinstance(response.data, list)
    assert len(response.data) == 2  # uma existente + uma nova

    titles = [note['title'] for note in response.data]
    contents = [note['content'] for note in response.data]

    assert "Nova Nota" in titles
    assert "Este é o conteúdo da nova nota" in contents
```

Rode os testes e veja se você implementou as rotas corretamente. 