# React Router Dom

Para trabalhar com troca de tela no React, podemos utiliza a biblioteca react-router-dom.

Precisamos instalar a biblioteca com o seguinte comando:

```
npm install react-router-dom
```

## Editar nota

Adicione o código abaixo no arquivo `index.html` dentro da tag `head`.

```
<script src="https://kit.fontawesome.com/7ae3e92237.js" crossorigin="anonymous"></script>
```

import { Link } from 'react-router-dom';
return (
  <div className="card" style={style}>
    <h3 className="card-title">{props.title}</h3>
    <div className="card-content">
      {props.children}
      <Link to={`edit/${props.id}`}>Editar</Link>
    </div>
  </div>
);
