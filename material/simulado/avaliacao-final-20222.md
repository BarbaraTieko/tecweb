!!! danger "Atenção"
    Para a Avaliação Final deixe o seu projeto preparado funcionando localmente. Lembrando que temos o Projeto Django REST e React.

# Questão 1

Nesta avaliação você deverá implementar uma nova funcionalidade no seu Projeto 2. A funcionalidade consiste em adicionar uma opção de buscar uma mensagem curiosa.

Para adicionar a nova funcionalidade é necessário seguir os passos a seguir:

- Obter um token de acesso para o seu usuário na API da Avaliação Final;
- Fazer uma requisição POST solicitando uma mensagem;
- Criar um formulário na página inicial capaz de fazer uma requisição para a API;
- Adicionar a mensagem devolvida pela requisição na página inicial do projeto.


## Restrições:

- As requisições devem ser feitas através do código (não utilizando alguma ferramenta externa como o Postman. Utilize somente para teste);

- Você deve implementar essa funcionalidade usando o seu Projeto 2 como base e as funcionalidades novas devem ser apresentadas na página inicial. Ou seja, você **não** pode criar uma nova página separada.

- Se você acredita que existe um motivo razoável para não seguir alguma das restrições acima, converse com a professora.

!!! danger "Importante"
    Programas que não puderem ser executados (ex: erros de sintaxe ou que impeçam o servidor de executar) receberão nota zero. O mesmo vale se você não utilizar o código do projeto 2.


## Instruções

Abaixo explicamos com mais detalhes cada um dos passos.

- **Obtendo o token**

O token pode ser obtido realizando uma requisição GET ao endpoint https://web-production-3d5a.up.railway.app/{username}/token (substituindo {username} pelo seu nome de usuário Insper). A resposta será um objeto JSON contendo o token.

- **Solicitando uma mensagem**

A funcionalidade nova consiste em enviar uma requisição POST para o endpoint https://web-production-3d5a.up.railway.app/

Essa requisição deve enviar o token obtido na etapa anterior no headers. Com a chave 'Authorization' e valor 'Token SEU_TOKEN', substituindo 'SEU_TOKEN' pelo token obtido na etapa anterior. Note que você não deve utilizar o token "hardcoded", ou seja, não vale copiar e colar o token.

Além disso, a requisição deve enviar no corpo (body) o seguinte conteúdo no formato JSON: {"username": "NOME DE USUÁRIO", "number": ALGUM_NUMERO}. Onde "NOME DE USUÁRIO" é o seu usuário Insper e ALGUM_NUMERO é um número qualquer.

Em caso de sucesso, essa requisição devolve json no seguinte formato {"message": "ALGUMA_MENSAGEM"}, onde ALGUMA_MENSAGEM é uma string com uma mensagem curiosa do número enviado na requisição.

Para esta etapa não é necessário colocar a imagem na tela, basta imprimir a mensagem no console do navegador ou no terminal do python.

- **Utilizando um formulário**

Na etapa anterior, não estávamos preocupados em pedir um número para o usuário. Agora queremos pedir um número e fazer a requisição de uma mensagem curiosa do número escolhido. Construa um formulário na página principal do seu projeto. Esse formulário deve ter um campo para o usuário inserir um número e um botão para efetuar a requisição da etapa anterior.

- **Mostrando a mensagem na página principal**

Ao fazer a requisição da mensagem, você deve disponibilizar a mensagem obtida na página principal.

# Questão 2

Nesta questão você deverá implementar uma nova rota no seu Projeto 2 Django REST.

Ao implementar a funcionalidade da questão 1, ficamos com curiosidade em saber quais números são mais populares entre os usuários. Para isso, queremos implementar uma *endpoint* no backend do Projeto 2 para registrar o número escolhido pelo usuário e contabilizar quantas vezes este número foi escolhido.

!!! danger "Atenção"
    Para esta questão só estamos interessados em implementar a *endpoint*. Não será necessário utilizar esta funcionalidade no *Frontend*.

Implemente uma nova view do Django REST Framework para a rota api/numeros/. Esta rota deve ser capaz de receber requisições GET e POST.

1. Primeiramente, precisamos criar um modelo novo chamado **Numero**. Este modelo deve ter dois campos numéricos, um para armazenar o número escolhido pelo usuário e outro para armazenar a quantidade de vezes que o número foi escolhido pelo usuário.
2. Ao receber uma requisição POST, a endpoint deve computar o número e atualizar a quantidade de vezes que este número foi escolhido pelos usuários.
Esta requisição será enviada da seguinte forma:
    - requisição: `POST`
    - endpoint: `api/numeros/`
    - body: `#!python {"number":X}` onde `X` é algum número inteiro.

    Se o número já existir no banco de dados o sistema deve somente incrementar o campo do banco de dados para a `quantidade`. Ou seja, o banco de dados não deve ter números repetidos.

3. Ao receber uma requisição GET, a endpoint deve retornar a lista de todos os números e as contagens registradas no banco de dados.
