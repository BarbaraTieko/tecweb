Para implementar a funcionalidade de edição de anotações, vamos precisar simular a navegação entre páginas. Para isso, vamos utilizar o [`react-router-dom`](https://reactrouter.com/en/main/start/tutorial){:target="_blank"}.

## Configuração Inicial

Para começar, instale o `react-router-dom` com o comando a seguir no terminal, dentro das pasta do projeto (notes-frontend):

```bash
npm install react-router-dom
```

- Abra o arquivo `src/main.jsx` e adicione as seguintes linhas de código:

```jsx hl_lines="3-6 10-15 19"
import React from 'react'
import ReactDOM from 'react-dom/client'
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import App from './App.jsx'
import './index.css'

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
  },
]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
```

A princípio, estamos definindo que ao acessar a rota `/`, queremos renderizar o componente `App`.
Nossa aplicação deve estar funcionando normalmente, sem alterações visíveis.

## Criando uma nova rota e componente para editar anotações




## Bônus: implementando a rotação dos cartões

Para continuar, avance para a próxima etapa.

[Bônus: implementando a rotação dos cartões](parte-06-bonus.md){ .md-button .md-button--primary }