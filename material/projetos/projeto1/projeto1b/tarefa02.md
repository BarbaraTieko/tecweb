# Implementando Sistema de Tags

Na parte B você deve implementar um sistema de tags para as anotações. Cada anotação pode ter no máximo uma tag (pode não ter nenhuma).

No formulário de criação/edição de anotações deve haver um campo de texto adicional para o usuário digitar o nome da tag. No backend (no `view.py`), se essa tag já existir, você deve associar a anotação a ela, senão, crie uma nova tag no banco de dados e associe à anotação.

Você também precisa criar mais duas páginas: uma com a lista com todas as tags existentes e outra com as anotações de uma determinada tag. A lista das tags deve mostrar apenas os nomes das tags com um link para a sua respectiva página de detalhes. A página de detalhes de uma tag deve mostrar o nome da tag e todas as anotações com aquela tag específica.

Para mais informações veja: [Relação Um para Muitos](https://docs.djangoproject.com/en/4.2/topics/db/examples/many_to_one/)
**Obs.:** O sistema de tags deve utilizar a relação de um para muitos.

Caso queira, veja o seguinte material para auxiliar o desenvolvimento desta etapa.
[Clique aqui](../../aulas/guia-many-to-one.md)