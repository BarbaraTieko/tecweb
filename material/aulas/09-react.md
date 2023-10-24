# React

O objetivo deste handout é que você tenha um primeiro contato com o React. Ao final do handout você terá alguma ideia de qual é a "cara" de um app React. Para saber mais sobre React veja o [tutorial oficial do React](https://react.dev/learn).

!!! danger "Importante"
    Nem todo código deste handout é JavaScript puro. Algumas (muitas) coisas são específicas do React e não funcionarão fora desse contexto.

!!! danger "Importante 2"
    Quando você for pesquisar no Google sobre React, você vai encontrar muito material utilizando classes. Essa é a uma maneira alternativa de se utilizar o React. O uso de componentes funcionais (que veremos neste handout) tem se tornado cada vez mais utilizado, mas é importante saber que existem essas duas alternativas para não utilizar soluções que não funcionarão para o seu caso.

## Setup do React

1. Garanta que você possui uma versão recente do [Node.js](https://nodejs.org/en/). Se você fez o servidor de exercícios JS você já deve ter uma versão recente do Node.js.
2. Crie um novo projeto React com o comando (o último argumento é o nome do projeto, você pode escolher o nome que quiser):
    ```
    npx create-react-app notes-frontend
    ```
3. Depois que o processo de instalação for concluído você já pode executar o app:

    ```
    $ cd notes-frontend
    $ npm start
    ```

    O app estará disponível em [`localhost:3000`](http://localhost:3000).

## Criando o primeiro componente

1. Crie o arquivo `src/components/Note/index.js` (você vai precisar criar algumas pastas) no seu projeto com o seguinte conteúdo:

    ```js linenums="1"
    import React from "react";

    export default function Note() {
      return <div>Olá mundo!</div>;
    }
    ```

2. Modifique o código do arquivo `src/App.js`:

    ```js linenums="1"
    import Note from "./components/Note";
    import "./App.css";

    function App() {
      return (
        <div className="App">
          <Note />
        </div>
      );
    }

    export default App;
    ```

3. Recarregue a página para ver o resultado.

Vamos entender o que aconteceu no código acima. Começando pelo `src/components/Note/index.js`:

- **Linha 1:** importa o React. É semelhante ao que fazemos ao importar módulos em Python;
- **Linha 3:** o `#!js export default` indica que, ao ser importar esse arquivo, o valor a seguir deve ser devolvido (no caso a `#!js function Note()`). Um exemplo disso pode ser visto na linha 2 do arquivo `src/App.js` no qual `#!js Note` guarda o valor default devolvido pela importação de `./components/Note` (como é uma pasta, ele importa por padrão o arquivo `src/components/Note/index.js`);
- **Linha 4:** o valor de retorno da função é uma tag HTML??? Pois é, na verdade esse arquivo não é JavaScript puro e sim uma sintaxe chamada JSX na qual é possível misturar tags e código JS.

Agora, no arquivo `src/App.js` temos:

- **Linha 1:** importação do componente `Note`;
- **Linha 2:** quando é necessário adicionar algum estilo ao componente nós podemos importar arquivos `.css` para que o estilo definido no arquivo seja aplicado;
- **Linha 4:** definindo uma função que será o componente da nossa aplicação. Note que ele é exportado na linha 12. Isso é equivalente ao que fizemos em uma linha no arquivo anterior;
- **Linha 5:** o valor de retorno é um componente mais complexo;
- **Linha 6:** o `className` será traduzido diretamente para o atributo `class` no HTML;
- **Linha 7:** utilizamos o componente criado no outro arquivo. Note como o código é **encapsulado**. Não precisamos saber **como** uma anotação é representada. Basta sabermos **o que** esse componente faz, ou seja, ele mostra os dados de uma anotação.

!!! info "Programação Orientada a Objetos?"
    Lembra do POO? Uma das grandes vantagens do uso de componentes no React é bastante semelhante às vantagens de usar classes. Podemos encapsular comportamentos de forma a facilitar modificações, debug e testes de unidade. E já que tocamos no assunto, sim, dá pra fazer [testes de unidade de componentes React](https://reactjs.org/docs/testing.html)!

!!! info "O `src/App.js`"
    O arquivo `src/App.js` também define um componente! A única diferença é que esse componente será pai de todos os outros componentes. Ou seja, todos os componentes que fazer parte da aplicação serão criados a partir do componente `App`.

## Aprimorando o componente: mostrando uma anotação

Modifique o `src/components/Note/index.js`:

```js hl_lines="2 6-14"
import React from "react";
import "./index.css";

export default function Note() {
  return (
    <div className="card">
      <h3 className="card-title">Receita de miojo</h3>
      <div className="card-content">
        <p>
          Bata com um martelo antes de abrir o pacote. Misture o tempero,
          coloque em uma vasilha e aproveite seu snack :)
        </p>
      </div>
    </div>
  );
}
```

Crie também o arquivo `src/components/Note/index.css` com o seguinte conteúdo:

```css
.card {
  width: 200px;
  display: flex;
  flex-direction: column;
  min-height: 100px;
  margin: 10px 5px;
  padding: 10px;
  box-shadow: 0 10px 20px rgb(0 0 0 / 19%), 0 6px 6px rgb(0 0 0 / 23%);
  border-radius: 5px;
  font-family: "Permanent Marker", cursive;
}

.card-title {
  font-weight: bold;
  line-height: 1.2;
  margin-bottom: 1rem;
  font-size: 1.2rem;
}

.card-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  flex-grow: 1;
  color: #4c4c4c;
}
```

Recarregue a página para ver o resultado.

!!! info "Encapsulamento (de novo)"
    Você se lembra que comentamos lá em cima que os componentes ajudam a encapsular o código? O `index.css` e o `index.js`, que definem o estilo e a lógica do componente estão ambos na mesma pasta. Assim, se eu quiser reaproveitar esse componente em outra aplicação, basta copiar essa pasta. Da mesma forma, se eu não for mais precisar desse componente, basta apagar a pasta.

    Existem diversas bibliotecas de componentes prontos para serem utilizados. O seu uso facilita muito o desenvolvimento de interfaces, mas é importante tomar cuidado ao decidir usar uma biblioteca. Verifique se ela está ativamente em desenvolvimento, se possui suporte, boa documentação, uma comunidade ativa.

## Importando as fontes

Precisamos importar os arquivos de fonte de texto. Para isso, abra o arquivo `public/index.html` e adicione as seguintes tags dentro do `#!html <head>`, antes do `#!html <title>`, por exemplo:

```html
<link
  rel="stylesheet"
  href="https://cdnjs.cloudflare.com/ajax/libs/meyer-reset/2.0/reset.min.css"
  integrity="sha512-NmLkDIU1C/C88wi324HBc+S2kLhi08PN5GDeUVVVC/BVt/9Izdsc9SVeVfA1UZbY3sHUlDSyRXhCzHfr6hmPPw=="
  crossorigin="anonymous"
/>
<link rel="preconnect" href="https://fonts.gstatic.com" />
<link
  href="https://fonts.googleapis.com/css2?family=Roboto&family=Permanent+Marker&display=swap"
  rel="stylesheet"
/>
```

## Customizando o componente

O nosso componente não é muito útil. Se utilizarmos múltiplos `<Note>` teremos o mesmo cartão, com o mesmo conteúdo, repetido várias vezes. Para definir parâmetros para o nosso componente utilizaremos as **props**.

Queremos utilizar o componente da seguinte maneira. Modifique o seu `src/Apps.js`:

```js hl_lines="7-13"
import Note from "./components/Note";
import "./App.css";

function App() {
  return (
    <div className="App">
      <Note title="Receita de miojo">
        Bata com um martelo antes de abrir o pacote. Misture o tempero, coloque
        em uma vasilha e aproveite seu snack :)
      </Note>
      <Note title="Sorvete de banana">
        Coloque a banana no congelador e espere.
      </Note>
    </div>
  );
}

export default App;
```

Ou seja, queremos definir atributos, como no HTML, para o título e adicionar o conteúdo como filho desse componente. Chamamos de filho todos os componentes colocados entre a abertura e fechamento da tag.

O React passa todas essas informações para o seu componente em um único argumento chamado **props**. Ele é um objeto JavaScript a partir do qual podemos acessar cada propriedade separadamente (lembrando que objetos podem ser utilizados como dicionários). Modifique o `src/components/Note/index.js`:

```js hl_lines="4 7-8"
import React from "react";
import "./index.css";

export default function Note(props) {
  return (
    <div className="card">
      <h3 className="card-title">{props.title}</h3>
      <div className="card-content">{props.children}</div>
    </div>
  );
}
```

Note que `title` é o nome do atributo que utilizamos no componente no outro arquivo. Já o `children` é sempre enviado com esse mesmo nome para o componente e é uma lista dos seus filhos.

Outro detalhe importante é que o `props.title` e `props.children` estão entre chaves. Esse é um recurso do JSX que permite que adicionemos valores do JavaScript nas tags.

!!! example "Exercício"
    Remove as chaves do `props.title` e `props.children` e recarregue a página. É esperado que apareça o texto "props.title" e "props.children" na tela.

## Renderizando múltiplos componentes a partir de um array

Vamos avançar mais um passo na nossa interface. Atualmente temos duas anotações, mas sabemos que essa quantidade é variável. Vamos assumir que temos os dados das anotações em um array. Para renderizar múltiplos componentes podemos utilizar o método `map`:

```js hl_lines="5-15 17-23"
import Note from "./components/Note";
import "./App.css";

function App() {
  const notes = [
    {
      title: "Receita de miojo",
      content:
        "Bata com um martelo antes de abrir o pacote. Misture o tempero, coloque em uma vasilha e aproveite seu snack :)",
    },
    {
      title: "Sorvete de banana",
      content: "Coloque a banana no congelador e espere.",
    },
  ];

  return (
    <div className="App">
      {notes.map((note) => (
        <Note title={note.title}>{note.content}</Note>
      ))}
    </div>
  );
}

export default App;
```

A versão acima deve funcionar, mas o console do navegador vai apresentar uma mensagem parecida com essa: `index.js:1 Warning: Each child in a list should have a unique "key" prop.`

Quando utilizamos o map, o resultado devolvido é um array contendo os resultados de cada execução da função. Para o React realizar as otimizações de renderização é necessário que cada elemento desse array possua um atributo `key` com um valor único. Adicione então o `key` no componente `Note`:

```js hl_lines="7 13 22"
import Note from "./components/Note";
import "./App.css";

function App() {
  const notes = [
    {
      id: 1,
      title: "Receita de miojo",
      content:
        "Bata com um martelo antes de abrir o pacote. Misture o tempero, coloque em uma vasilha e aproveite seu snack :)",
    },
    {
      id: 2,
      title: "Sorvete de banana",
      content: "Coloque a banana no congelador e espere.",
    },
  ];

  return (
    <div className="App">
      {notes.map((note) => (
        <Note key={`note__${note.id}`} title={note.title}>
          {note.content}
        </Note>
      ))}
    </div>
  );
}

export default App;
```

Você poderia utilizar qualquer string, desde que fosse única. Vamos utilizar o padrão `#!js "note__1"`, `#!js "note__2"`, `#!js "note__3"`, etc.

## Recebendo dados

Os dados ainda estão fixos. Queremos obter a lista de anotações de algum servidor. Ainda bem que já implementamos o servidor REST na aula anterior! Agora só precisamos implementar o cliente. Para isso, vamos utilizar o axios. Comece instalando o axios no nosso projeto:

    npm i axios

Agora modifique o seu código do `src/App.js` para utilizar o axios para realizar uma requisição GET para o servidor REST desenvolvido na última aula:

```js hl_lines="1 6-9"
import axios from "axios";
import Note from "./components/Note";
import "./App.css";

function App() {
  // O array de notes continua aqui
  axios
    .get("http://localhost:8000/api/notes/")
    .then((res) => console.log(res));

  return (
    // O resto do código deve continuar aqui
  );
}

export default App;
```

!!! danger "Importante!"
    Antes de testar, lembre-se de colocar o servidor da aula passada para rodar.

!!! danger "Importante!"
    Ao tentar executar o código acima, o seguinte erro deve aparecer no console do navegador:

    ```
    Access to XMLHttpRequest at 'http://localhost:8000/api/' from origin
    'http://localhost:3000' has been blocked by CORS policy: No
    'Access-Control-Allow-Origin' header is present on the requested resource.
    ```

    Esse erro ocorre porque o navegador está tentando te proteger. Ele não fará requisições para servidores que não aceitam explicitamente requisições de outros endereços. O nosso frontend está rodando em `localhost:3000` e o backend em `localhost:8000`. Eles são endereços diferentes, então a requisição é bloqueada.

    Para esse tipo de requisição ser bloqueada, precisamos adicionar o header CORS, indicando que [aceitamos essa requisição](https://drawings.jvns.ca/cors/):

    **No projeto Django,** adicione o módulo `django-cors-headers`:

    ```
    pip install django-cors-headers
    ```

    Adicione o app no `#!python INSTALLED_APPS` no arquivo `getit/settings.py`:

    ```python
    INSTALLED_APPS = [
        ...
        'corsheaders',
        ...
    ]
    ```

    Adicione também o `#!python MIDDLEWARE` como o primeiro elemento da lista, no mesmo arquivo:

    ```python
    MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',
        ...
    ]
    ```

    Finalmente, no final do mesmo arquivo de configuração, adicione:

    ```python
    CORS_ORIGIN_ALLOW_ALL = True
    ```

Depois de realizar as adaptações no servidor, seu código deve funcionar e a requisição devolve a lista de anotações do servidor.

## Guardando os dados

O app já é capaz de fazer a requisição e receber os dados, mas ainda não mostra nada na tela. O problema é que a requisição é feita em uma chamada assíncrona, assim, não sabemos **quando** o resultado será obtido. Como o componente é uma função, ele não pode armazenar estado como um objeto. Ela é executada para gerar a tela e termina a execução.

Por isso foram criados os chamados [**hooks**](https://react.dev/reference/react), que permitem o armazenamento de estado em componentes funcionais. Vamos utilizar o `#!js useState` para armazenar estado. Modifique o arquivo `src/App.js`:

```js hl_lines="1 7-11"
import { useState } from "react";
import axios from "axios";
import Note from "./components/Note";
import "./App.css";

function App() {
  const [notes, setNotes] = useState([]); // Remova o array de notes que existia na versão anterior

  axios.get("http://localhost:8000/api/notes/").then((res) => setNotes(res.data));

  console.log(notes);

  return (
    // O resto do código deve continuar aqui
  );
}

export default App;
```

O `useState` devolve o valor do estado atual e uma função que permite modificar o estado. Ele também recebe o valor inicial do estado, no caso um array vazio.

Ao executar o código acima, o console do navegador deve mostrar o JSON de anotações diversas vezes (recomendo que você feche a aba até implementar o resto do código). O que acontece é que toda vez que o estado muda, o componente é renderizado novamente, ou seja, a função é re-executada. Assim, quando a requisição é finalizada, os dados são utilizados para atualizar a variável `notes` do estado. Quando isso ocorre, o componente é renderizado novamente. Isso faz com que uma nova requisição ocorra, que por sua vez realizará outra atualização do estado, que  fará com que uma nova requisição ocorra, que por sua vez... enfim, você acabou de implementar a versão de componentes React de um loop infinito!

Queremos realizar a requisição apenas uma vez. Para isso, existe um outro **hook** chamado `useEffect`, que permite definir algumas condições para quando ele deve ser re-executado. Modifique novamente o arquivo `src/App.js`:

```js hl_lines="1 9-13"
import { useEffect, useState } from "react";
import axios from "axios";
import Note from "./components/Note";
import "./App.css";

function App() {
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/notes/")
      .then((res) => setNotes(res.data));
  }, []);

  console.log(notes);

  return (
    // Resto do código aqui
  );
}

export default App;
```

O primeiro argumento do `useEffect` é uma função. Essa função será executada quando o conteúdo do segundo argumento (um array) mudar. Como o array está vazio, a função será executada apenas uma vez.

## Carregando imagens e outros arquivos estáticos

Além de JavaScript e CSS, a nossa interface também precisa de algumas imagens. Elas podem ser adicionadas à pasta `public`. Faça o download da imagem do [logo do Get-it](https://raw.githubusercontent.com/toshikurauchi/tecweb-2021-1-desafio-css/main/docs/img/logo-getit.png) e salve-o na pasta `public`. Agora a imagem estará disponível na rota `/logo-geti.png`. Agora você pode adicioná-lo em `src/App.js`:

```js hl_lines="8"
// Imports

function App() {
  // Resto do código aqui

  return (
    <div className="App">
      <img src="/logo-getit.png" />
      {notes.map((note) => (
        <Note key={`note__${note.id}`} title={note.title}>
          {note.content}
        </Note>
      ))}
    </div>
  );
}

export default App;
```

Esta é uma forma mais direta de adicionar a imagem, mas você poderia criar um novo componente para mostrar a imagem com o estilo correto.

!!! example "Exercício"
    Agora é com você! É possível implementar todas as outras funcionalidades do frontend do Get-it utilizando componentes funcionais, os hooks `useEffect` e `useState` e o axios.

    Tente implementar a criação de anotações, a edição e a exclusão.

## Implementando a Criação de Anotações

Vamos criar um componente para o formulário de criação.

1. Crie o arquivo `src/components/Formulario/index.js` com o seguinte conteúdo:

```js
import axios from "axios";
import React, { useState } from "react";

export default function Formulario(props) {

    return (
        <form className="form-card" method="post">
            <input
                className="form-card-title"
                type="text"
                name="titulo"
                placeholder="Título"
            />
            <textarea
                className="autoresize"
                name="detalhes"
                placeholder="Digite o conteúdo..."
            ></textarea>
            <input
                className="form-card-tag"
                type="text"
                name="tag"
                placeholder="Adicione uma tag"
            />
            <button className="btn" type="submit">Criar</button>
        </form>
    );
}
```


Crie o arquivo `src/components/Formulario/index.css` e coloque o estilo CSS das classes `form-card`, `form-card-tag` e `btn` utilizado nos projetos anteriores.

## Adicionando componente Formulario no App

Precisamos adicionar o componente `Formulario` no `src/App.js`. Podemos pensar no componente como uma função javascript que retorna html. Para utilizar um componente, basta colocar o nome dele entre tags, como se fosse uma tag HTML. Veja o exemplo abaixo:

```js hl_lines="5 18"
import axios from "axios";
import React, { useEffect, useState } from "react";
import "./App.css";
import Note from "./components/Note";
import Formulario from "./components/Formulario";

function App() {
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/notes/")
      .then((res) => setNotes(res.data));
  }, []);

  return (
    <div className="App">
      <Formulario />
      {notes.map((note) => (
        <Note key={`note__${note.id}`} title={note.title}>
          {note.content}
        </Note>
      ))}
    </div>
  );
}

export default App;
```

## Armazenado valor digitado pelo usuário nos Inputs

Vamos armazenar os valores digitados pelo usuário nas variáveis `titulo` e `conteudo`. Para isso, vamos criar duas variáveis utilizando `useState` do React;

```js hl_lines="5-6"
import axios from "axios";
import React, { useState } from "react";

export default function Formulario(props) {
    const [titulo, setTitulo] = useState("");
    const [content, setContent] = useState("");

    return (
        <form className="form-card" method="post">
            <input
                className="form-card-title"
                type="text"
                name="titulo"
                placeholder="Título"
            />
            <textarea
                className="autoresize"
                name="detalhes"
                placeholder="Digite o conteúdo..."
            ></textarea>
            <input
                className="form-card-tag"
                type="text"
                name="tag"
                placeholder="Adicione uma tag"
            />
            <button className="btn" type="submit">Criar</button>
        </form>
    );
}
```

As variáveis inicialmente começam como `strings` vazias `#!python ""`. Conforme o usuário digita, o valor das variáveis é atualizado. Para isso podemos utilizar o atributo `onChange` do HTML, veja o exemplo abaixo:

```js hl_lines="8-10 19"
import axios from "axios";
import React, { useState } from "react";

export default function Formulario(props) {
    const [titulo, setTitulo] = useState("");
    const [content, setContent] = useState("");

    const tituloOnChange = (event) => {
        setTitulo(event.target.value);
    }

    return (
        <form className="form-card" method="post">
            <input
                className="form-card-title"
                type="text"
                name="titulo"
                placeholder="Título"
                onChange={tituloOnChange}
            />
            <textarea
                className="autoresize"
                name="detalhes"
                placeholder="Digite o conteúdo..."
            ></textarea>
            <input
                className="form-card-tag"
                type="text"
                name="tag"
                placeholder="Adicione uma tag"
            />
            <button className="btn" type="submit">Criar</button>
        </form>
    );
}
```
Sempre que o usuário interagir com o campo `input` o evento `onChange` chamará a função passada, neste caso, a função `tituloOnChange` será chamada. A função atualiza o valor da variável `titulo` com o valor digitado pelo usuário utilizando a função `setTitulo`.

Outra forma de realizar a mesma coisa é utilizando uma função anônima, veja o exemplo abaixo para o campo `content`:


```js hl_lines="25"
import axios from "axios";
import React, { useState } from "react";

export default function Formulario(props) {
    const [titulo, setTitulo] = useState("");
    const [content, setContent] = useState("");

    const tituloOnChange = (event) => {
        setTitulo(event.target.value);
    }

    return (
        <form className="form-card" method="post">
            <input
                className="form-card-title"
                type="text"
                name="titulo"
                placeholder="Título"
                onChange={tituloOnChange}
            />
            <textarea
                className="autoresize"
                name="detalhes"
                placeholder="Digite o conteúdo..."
                onChange={ (event)=>{setContent(event.target.value)} }
            ></textarea>
            <input
                className="form-card-tag"
                type="text"
                name="tag"
                placeholder="Adicione uma tag"
            />
            <button className="btn" type="submit">Criar</button>
        </form>
    );
}
```

## Enviar os dados para o servidor
Agora vamos enviar os dados para o servidor. Para isso, vamos utilizar o atributo `onSubmit` do HTML. Veja o exemplo abaixo:

O comando [event.preventDefault()](https://developer.mozilla.org/en-US/docs/Web/API/Event/preventDefault) previne que o formulário seja enviado para o servidor. Assim, podemos enviar os dados utilizando o axios.

```js hl_lines="12-21 24"
import axios from "axios";
import React, { useState } from "react";

export default function Formulario(props) {
    const [titulo, setTitulo] = useState("");
    const [content, setContent] = useState("");

    const tituloOnChange = (event) => {
        setTitulo(event.target.value);
    }

    const criarNote = (event) => {
        event.preventDefault();
        
        const data = {
            "title" : titulo,
            "content": content
        }

        axios.post("http://localhost:8000/api/notes/", data)
    }

    return (
        <form className="form-card" method="post" onSubmit={criarNote}>
            <input
                className="form-card-title"
                type="text"
                name="titulo"
                placeholder="Título"
                onChange={tituloOnChange}
            />
            <textarea
                className="autoresize"
                name="detalhes"
                placeholder="Digite o conteúdo..."
                onChange={ (event)=>{setContent(event.target.value)} }
            ></textarea>
            <input
                className="form-card-tag"
                type="text"
                name="tag"
                placeholder="Adicione uma tag"
            />
            <button className="btn" type="submit">Criar</button>
        </form>
    );
}
```

## Atualizando a lista de anotações
Agora que já enviamos os dados para o servidor, precisamos atualizar a lista de anotações. Se olharmos o código do arquivo `src/App.js` queremos executar o código contido nas linhas marcadas abaixo, pois queremos atualizar a lista de anotações.

```js hl_lines="11-13"
import axios from "axios";
import React, { useEffect, useState } from "react";
import "./App.css";
import Note from "./components/Note";
import Formulario from "./components/Formulario";

function App() {
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/notes/")
      .then((res) => setNotes(res.data));
  }, []);

  return (
    <div className="App">
      <Formulario />
      {notes.map((note) => (
        <Note key={`note__${note.id}`} title={note.title}>
          {note.content}
        </Note>
      ))}
    </div>
  );
}

export default App;
```

Para isso, vamos mover esse trecho de código para dentro de uma função, para que possamos enviar essa função para o componente `Formulario`.

Os componentes são função, desta forma, podemos enviar argumentos para as funções. No caso, vamos enviar a função `carregaNotas` para o componente `Formulario` utilizando o nome `funcao` (pode ser qualquer nome que desejar).


```js hl_lines="10-14 17 22"
import axios from "axios";
import React, { useEffect, useState } from "react";
import "./App.css";
import Note from "./components/Note";
import Formulario from "./components/Formulario";

function App() {
  const [notes, setNotes] = useState([]);

  const carregaNotas = () => {
      axios
        .get("http://localhost:8000/api/notes/")
        .then((res) => setNotes(res.data));
    }

  useEffect(() => {
    carregaNotas();
  }, []);

  return (
    <div className="App">
      <Formulario funcao={carregaNotas}/>
      {notes.map((note) => (
        <Note key={`note__${note.id}`} title={note.title}>
          {note.content}
        </Note>
      ))}
    </div>
  );
}

export default App;
```

## Chamando a função `carregaNotas` no componente `Formulario`

O componente `Formulario` recebe o argumento `props` que contém todas as informações enviadas para o componente.
Como enviamos a função `carregaNotas` com o nome de `funcao`, para chamar a função `carregaNotas` dentro do componente `Formulario` utilizamos o comando `#!js props.funcao()`.

```js hl_lines="23"
import axios from "axios";
import React, { useState } from "react";

export default function Formulario(props) {
    const [titulo, setTitulo] = useState("");
    const [content, setContent] = useState("");

    const tituloOnChange = (event) => {
        setTitulo(event.target.value);
    }

    const criarNote = (event) => {
        event.preventDefault();
        
        const data = {
            "title" : titulo,
            "content": content
        }

        axios
          .post("http://localhost:8000/api/notes/", data)
          .then(() => {
            props.funcao();
          })
    }

    return (
        <form className="form-card" method="post" onSubmit={criarNote}>
            <input
                className="form-card-title"
                type="text"
                name="titulo"
                placeholder="Título"
                onChange={tituloOnChange}
            />
            <textarea
                className="autoresize"
                name="detalhes"
                placeholder="Digite o conteúdo..."
                onChange={ (event)=>{setContent(event.target.value)} }
            ></textarea>
            <input
                className="form-card-tag"
                type="text"
                name="tag"
                placeholder="Adicione uma tag"
            />
            <button className="btn" type="submit">Criar</button>
        </form>
    );
}
```

## Limpando os valores dos campos do Formulário

Basta atualizar as variáveis `titulo` e `content` com o valor `#!python ""` (string vazia). Além disso, é necessário utilizar essas variáveis para definir o valor dos campos do formulário. Veja o exemplo abaixo:

```js hl_lines="24-25 37 44"
import axios from "axios";
import React, { useState } from "react";

export default function Formulario(props) {
    const [titulo, setTitulo] = useState("");
    const [content, setContent] = useState("");

    const tituloOnChange = (event) => {
        setTitulo(event.target.value);
    }

    const criarNote = (event) => {
        event.preventDefault();
        
        const data = {
            "title" : titulo,
            "content": content
        }

        axios
          .post("http://localhost:8000/api/notes/", data)
          .then(() => {
            props.funcao();
            setTitulo("");
            setContent("");
          })
    }

    return (
        <form className="form-card" method="post" onSubmit={criarNote}>
            <input
                className="form-card-title"
                type="text"
                name="titulo"
                placeholder="Título"
                onChange={tituloOnChange}
                value={titulo}
            />
            <textarea
                className="autoresize"
                name="detalhes"
                placeholder="Digite o conteúdo..."
                onChange={ (event)=>{setContent(event.target.value)} }
                value={content}
            ></textarea>
            <input
                className="form-card-tag"
                type="text"
                name="tag"
                placeholder="Adicione uma tag"
            />
            <button className="btn" type="submit">Criar</button>
        </form>
    );
}
```

## Bônus: implementando a rotação dos cartões

Para implementar a rotação dos cartões vamos utilizar novamente o `useEffect` e o `useState`. Modifique o `src/componentes/Note/index.js`:

```js
import React, { useEffect, useState } from "react";
import "./index.css";

function randomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

export default function Note(props) {
  const [rotation, setRotation] = useState(0);
  useEffect(() => {
    setRotation(randomInt(-5, 5));
  }, []);

  const style = { transform: `rotate(${rotation}deg)` };

  return (
    <div className="card" style={style}>
      <h3 className="card-title">{props.title}</h3>
      <div className="card-content">{props.children}</div>
    </div>
  );
}
```
