# 02 - Desafio CSS

## Desafio CSS

!!! success "Entrega"
    :date: 19/08 (segunda-feira)
    
    :clock1: Commits até as 23:59

    :material-account-group: Trios, duplas ou individual

    :simple-github: Entrega via GitHub. 

    Um integrante do grupo deve criar um repositório no GitHub para efetuar a entrega da atividade.

    **Importante:** Todos os integrantes do grupo devem possuir contribuições no código.

    :fontawesome-solid-clipboard-question: [Responda o formulário com as informações do repositório](https://forms.gle/ydGYrVF2AFp8vGqJ9){ :target="_blank"}.
    
## Objetivo

<figure markdown="span">
  ![Resultado do Handout 01](02-desafio-css/img/original.png){ width="80%" }
  <figcaption>Resultado do Handout 01 - Versão inicial</figcaption>
</figure>


Na aula passada nós desenvolvemos a primeira versão do nosso primeiro site, o Get-it. Na aula de hoje nós vamos focar no estilo da página para relembrar e aprender alguns conceitos de CSS.

O seu objetivo :octicons-goal-24: é se aproximar o máximo possível da página a seguir utilizando apenas CSS puro.

<figure markdown="span">
  ![Referência do resultado esperado](02-desafio-css/img/referencia.png){ width="80%" }
  <figcaption>Referência do resultado esperado</figcaption>
</figure>

!!! example "Referência"
    Se precisar de uma imagem com resolução melhor clique no botão abaixo.

    [Clique aqui :material-download:](02-desafio-css/img/referencia.png){ .md-button download}

### Cores dos Cards

<figure markdown="span">
  ![Cores dos Cards](02-desafio-css/img/Get-it.gif){ width="80%" }
  <figcaption>O <strong>gif</strong> acima mostra a página sendo recarregada manualmente diversas vezes.</figcaption>
</figure>

!!! danger "ATENÇÃO!" 
    O **gif** acima mostra a página sendo recarregada manualmente diversas vezes. 
    
    A animação é apenas para mostrar que a cada vez que a página é carregada, os elementos mudam de cor e rotação aleatoriamente. Não se preocupe, o javascript responsável pela aleatorização já está pronto.

!!! example "Exercício"
    Inspecione um card no navegador e veja procure pela classe CSS que está sendo aplicada para a cor de fundo. 

## Instruções

Baixe os arquivos base no botão abaixo.

[Download :material-download:](02-desafio-css/desafio-css.zip){ .md-button download}

- [X] Você deve modificar apenas o arquivo **getit.css**.
- [X] Todos os integrantes do grupo devem possuir contribuições no código.
- [ ] :no_entry_sign: Não é permitido editar os arquivos `index.html` e `getit.js`.
- [ ] :no_entry_sign: Não é permitido o uso de frameworks CSS (Bootstrap, Materialize, etc).

!!! tip "Dica"
    É possível visualizar a página HTML em desenvolvimento no seu navegador utilizando o comando abaixo:
    
    === "Windows :material-microsoft-windows:/Linux :simple-linux:"
        ```bash
        python -m http.server
        ```
    === "MacOS :material-apple:"
        ```bash
        python3 -m http.server
        ```
    

    Este comando deve ser executado no terminal dentro da pasta `docs` do projeto. Após executar o comando, abra o navegador e acesse o endereço `http://localhost:8000`.

!!! danger "Atenção"
    Acesse a página HTML em uma aba anônima ou utilize o **Hard Refresh/Hard Reload** (1) para garantir que o cache do navegador não está atrapalhando a visualização das alterações. 
    { .annotate }

    1. Hard Refresh/Hard Reload são atalhos para forçar o navegador a carregar a versão mais recente de uma página. No Windows :material-microsoft-windows: e Linux :simple-linux:, pressione `Ctrl + F5`. No MacOS :material-apple:, pressione `Cmd + Shift + R`. Caso esses atalhos não funcionem, você pode pesquisar o atalho específico para o seu navegador.


## Entrega :material-truck-delivery:

- A entrega deve ser feita via github. O grupo deve criar um repositório contendo os arquivos necessários.

- A sua página deve **obrigatoriamente** estar disponível no GitHub pages seguindo [:point_right: estes passos](https://docs.github.com/en/github/working-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site){:target="_blank"}

- Será considerado o último commit enviado antes do prazo. 
- O link do repositório deve ser informado em [ :point_right: Formulário](https://forms.gle/ydGYrVF2AFp8vGqJ9){ :target="_blank"}.


## Rubrica

A nota deste trabalho é a soma dos pontos abaixo. Será feita uma inspeção visual, ou seja, os tamanhos, distâncias e cores não precisam ser **exatamente** iguais, mas devem ser visualmente bastante parecidos:

- Textos:
    - [1 pt] Posição, fonte e cores dos textos corretas

- App bar:
    - [1 pt] Tamanho do logo correto
    - [1 pt] Aparência correta (cor e sombra)

- Formulário:
    - [1 pt] Aparência dos campos de texto e do botão correta (fonte, cores, ausência de bordas, etc)
    - [1 pt] Aparência do formulário correta (sombra, proporções, distâncias, cantos arredondados, etc)
    - [1 pt] Posição do formulário correta (centralizado e com a distância correta com relação aos outros elementos principais)

- Cartões:

    - [1 pt] Espaçamentos corretos
    - [1 pt] Cores de fundo corretas
    - [1 pt] Aparência do cartão correta (sombra, proporções, distâncias, cantos arredondados, etc)
    - [1 pt] Rotação dos cartões

## Observações importantes

- No caso de entrega com atraso, a nota será a metade da soma dos pontos obtidos.
- **Trabalhos não identificados (não respondeu ao formulário) serão considerados atrasados (veja o item acima).** 
- A nota de trabalhos com modificações em outros arquivos além do README.md e do `docs/getit.css` será limitada a no máximo 7 (equivalente ao conceito B). Modificações em outros arquivos devem ser explicitamente aprovadas pelo professor.
- Para este trabalho você não precisa se preocupar com a versão mobile da página. Ela será testada apenas em um monitor.


