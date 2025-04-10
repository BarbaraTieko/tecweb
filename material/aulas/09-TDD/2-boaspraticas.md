# Boas práticas

Uma maneira eficaz de garantir a qualidade dos testes é seguir a metodologia Given-When-Then (Dado-Quando-Então). Ela ajuda a estruturar os testes de forma clara e objetiva, facilitando a compreensão e manutenção do código. Você pode ler mais sobre esse padrão [aqui](https://martinfowler.com/bliki/GivenWhenThen.html){:target="_blank"}.

### 📝 **Padrão Given-When-Then**

1. **Dado** um cenário específico
    - Inicialize os dados necessários para o teste.

2. **Quando** uma ação é executada

3. **Então** um resultado é esperado
    - Verifique se o resultado da ação corresponde ao esperado.

#### 📌 **Exemplo de teste com Given-When-Then**

Utilizando esse padrão, podemos reescrever o teste da função `calcula_media` de uma maneira mais estruturada, isolando o que é dado, a execução da função e o resultado esperado:

```python
def test_calcula_media():
    # Given
    lista = [2, 4, 6]
    # When
    resultado = calcula_media(lista)
    # Then
    assert resultado == 4
```

A primeira vista, pode parecer que essa abordagem torna o código mais verboso, mas ela traz benefícios significativos em termos de organização e legibilidade, principalmente conforme os testes forem ficando mais complexos. Além disso, facilita a identificação de possíveis falhas e a manutenção dos testes no futuro.

### 📝 **Nomes dos testes**

Outro ponto importante é a nomenclatura dos testes. É recomendado seguir um padrão que descreva claramente o comportamento testado, como no exemplo acima (`test_calcula_media`). Isso ajuda a identificar rapidamente o propósito de cada teste e a localizar possíveis problemas. Poderíamos até mesmo ser mais específicos, como `test_calcula_media_lista_com_tres_elementos_positivos`.

### 📝**Repetição**

Como vimos em DesSoft, sabemos que para realmente saber se uma função está correta, precisamos testá-la em diferentes cenários. Portanto, é importante criar testes que cubram vários casos possíveis, incluindo casos extremos e limites. Isso garante que a função se comporte corretamente em todas as situações.

Vamos pensar agora qual a melhor maneira de testar nossa função com outras listas. Uma possibilidade seria adicionar vários blocos Given-When-Then no nosso teste:

```python
def test_calcula_media():
    # Given
    lista = [2, 4, 6]
    # When
    resultado = calcula_media(lista)
    # Then
    assert resultado == 4

    # Given
    lista = [1, 2, 3]
    # When
    resultado = calcula_media(lista)
    # Then
    assert resultado == 2
```

No entanto, essa abordagem pode se tornar repetitiva e difícil de manter conforme adicionamos mais casos de teste, além de não ser muito legível. Uma segunda possibilidade seria utilizar um teste para cada cenário, o que pode ser mais organizado:

```python
def test_calcula_media_lista_com_tres_elementos_positivos():
    # Given
    lista = [2, 4, 6]
    # When
    resultado = calcula_media(lista)
    # Then
    assert resultado == 4

def test_calcula_media_lista_com_tres_elementos_crescentes():
    # Given
    lista = [1, 2, 3]
    # When
    resultado = calcula_media(lista)
    # Then
    assert resultado == 2
```

Essa abordagem é mais clara e facilita a identificação de falhas em cenários específicos. No entanto, pode gerar uma grande quantidade de testes, o que pode ser difícil de gerenciar. É por esse motivo, que o pytest oferece uma maneira mais eficiente de lidar com esses casos, chamada de testes parametrizados.

#### 📌 **Testes parametrizados**

Os testes parametrizados permitem que você execute o mesmo teste com diferentes conjuntos de dados, evitando a repetição de código e facilitando a manutenção. Vamos ver como isso funciona:

```python
import pytest

@pytest.mark.parametrize("lista, esperado", [
    ([2, 4, 6], 4),
    ([1, 2, 3], 2), 
])
def test_calcula_media_lista_com_tres_elementos_positivos(lista, esperado):
    # Given
    # Nesse caso, o "Given" é passado como parâmetro
    # When
    resultado = calcula_media(lista)
    # Then
    assert resultado == esperado
```

Nesse exemplo, utilizamos o `@pytest.mark.parametrize` para definir diferentes conjuntos de dados e resultados esperados. A função de teste será executada para cada combinação, verificando se a função `calcula_media` se comporta corretamente em todos os cenários.

Se estiver gostando do assunto, você pode ler um pouquinho mais sobre boas práticas de testes [aqui](https://emimartin.me/pytest_best_practices){:target="_blank"}.

A seguir, vamos ver como [lidar com exceções](3-exceptions.md).