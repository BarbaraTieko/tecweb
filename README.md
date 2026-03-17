# Documentação do Projeto com MkDocs

Este projeto utiliza [MkDocs](https://www.mkdocs.org/) para geração de documentação estática em Python.

## Criando o ambiente virtual

teste
# Crie o ambiente virtual
    
    python -m venv .venv

# Ative o ambiente virtual
# No Windows:
    
    .venv\Scripts\activate

# No macOS/Linux:
    
    source .venv/bin/activate


## Instalando as dependências

    pip install -r requirements.txt

## Visualizar localmente

    mkdocs serve

## Publicar no GitHub Pages

    mkdocs gh-deploy
