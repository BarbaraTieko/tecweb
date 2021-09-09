# Django

Neste handout vamos dar nossos primeiros passos no desenvolvimento web usando Django. Para isso, vamos refazer o backend da parte A do projeto.

!!! danger "Importante"
    O Django possui **muitas** funcionalidades. O nosso objetivo neste handout é oferecer apenas uma introdução bastante breve. Você provavelmente vai precisar ler outros tutoriais, a documentação do Django e fazer pesquisas no Google para conseguir fazer o projeto.

    Conte com o professor para te ajudar com as dúvidas, mas é esperado que você desenvolva a maturidade para pesquisar e aprender o que falta por conta própria. Essa é uma habilidade essencial na vida de qualquer desenvolvedora/desenvolvedor.

!!! danger "Importante"
    Em Tecnologias Web nós utilizaremos o Django 3.X. É importante levar isso em conta quando for procurar respostas no Google. O [Django 3.0](https://docs.djangoproject.com/en/3.1/releases/3.0/) foi lançado no final de 2019, então será comum você encontrar respostas desatualizadas. **Sempre** que encontrar alguma função/método que não conhece, consulte a documentação da biblioteca para verificar se essa é a forma mais atualizada de se resolver o problema (essa dica vale para qualquer biblioteca/framework que for utilizar).

!!! info "Referência"
    Este handout é baseado no [tutorial disponível na própria documentação do Django](https://docs.djangoproject.com/en/3.0/intro/tutorial01/). A intenção é desenvolvê-lo de forma mais conectada com o que já fizemos na parte A do projeto, mas a documentação é muito mais completa e é possível se aprofundar mais em diversas questões. Recomendo a leitura (a documentação do Django é muito bem feita).

## Instalando o Django

!!! example "Exercício 01"
    Crie uma pasta para a nova versão do projeto e, dentro dela, [crie um ambiente virtual](../auxiliar/venv.md) (`venv`) chamado `env` para o seu projeto. **Lembre-se de ativar o ambiente antes de seguir para o próximo exercício.**

!!! example "Exercício 02"
    Agora sim, instale o Django:

        python -m pip install Django

Para verificar se a instalação foi bem sucedida, inicie o Python em sua versão interativa (digite `python` no terminal) e utilize os seguintes comandos:

```python
import django
print(django.get_version())
```

O Django deve ter sido instalado em uma versão igual ou superior à 3.0.

Quando o Django estiver instalado, siga para o [primeiro passo](04-django/parte1.md).

## Índice do handout

Este handout está dividido nos passos a seguir:

- [Parte 1: Iniciando o projeto](04-django/parte1.md)
- [Parte 2: Criando nosso primeiro app](04-django/parte2.md)
- [Parte 3: Integrando com o banco de dados](04-django/parte3.md)
- [Parte 4: O Django Admin](04-django/parte4.md)
- [Parte 5: Usando templates](04-django/parte5.md)
- [Parte 6: Trabalhando com formulários e o método POST](04-django/parte6.md)
