!!! danger "Atenção"
    Como o Projeto 2 está sendo avaliado, não faça o commit da resolução deste exercício na branch principal (main/master).

    Para isto, crie uma branch nova.

# Questão 1

Nesta avaliação você deverá implementar uma nova funcionalidade no seu Projeto 2. A funcionalidade consiste em mostrar uma mensagem na página inicial.

Para obter a mensagem é necessário seguir os passos a seguir:

- Obter um token de acesso para o seu usuário na API da AF;
- Fazer uma requisição POST solicitando uma mensagem para a API;
- Adicionar a mensagem na página principal.

## Restrições:

Os 3 passos devem ser repetidos para cada nova requisição, ou seja, uma nova mensagem será gerada a cada vez que o usuário recarregar a página;
As requisições devem ser feitas através do código (não utilizando alguma ferramenta externa como o Postman);
Você deve implementar essa funcionalidade usando o seu Projeto 2 como base e a mensagem deve ser apresentada na página inicial. Ou seja, você não pode criar uma nova página separada para mostrar essa mensagem.

Abaixo explicamos com mais detalhes cada um dos passos.

- **Obtendo o token**

    O token pode ser obtido realizando uma requisição GET ao endpoint https://enigmatic-bayou-56424.herokuapp.com/{username}/token (substituindo {username} pelo seu nome de usuário Insper). A resposta será um objeto JSON contendo o token.

- **Solicitando uma mensagem**

    Faça uma requisição POST para o endpoint https://enigmatic-bayou-56424.herokuapp.com/{username}/message (substituindo {username} pelo seu nome de usuário Insper). Você deve obrigatoriamente enviar o token obtido na etapa anterior no corpo da requisição. O JSON enviado no POST deve seguir o formato {"token": "SEUTOKEN"} (substituindo SEUTOKEN pelo token obtido na etapa anterior).

    Em caso de sucesso, essa requisição devolve um objeto JSON contendo uma mensagem.

- **Mostrando a mensagem**

    A mensagem deve estar disponível na página principal do projeto 2. Você pode disponibilizar a mensagem da forma que preferir.
