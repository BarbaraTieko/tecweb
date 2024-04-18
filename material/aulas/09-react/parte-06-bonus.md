## Bônus: implementando a rotação dos cartões

Para implementar a rotação dos cartões vamos utilizar novamente o `useEffect` e o `useState`. Modifique o `src/componentes/Note/index.jsx`:

```jsx
import { Link } from "react-router-dom";
import { useEffect, useState } from "react";
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
      <div className="card">
          <h3 className="card-title">{props.title}</h3>
          <Link to={`edit/${props.id}`}>✏️</Link>
          <div className="card-content">{props.children}</div>
      </div>
    );
}
```
