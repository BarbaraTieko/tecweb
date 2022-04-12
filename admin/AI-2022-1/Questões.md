
PROCTORIO:
Esse teste deve ficar aberto durante TODA a realização da sua avaliação.

Caso SEM QUERER você interrompa o PROCTORIO, mas continue a fazer a prova, sua prova será corrigida até momento que Proctorio ficou ativo gravando sua tela de prova.

Não considere o cronômetro do Proctorio como referência de tempo de prova. Use o tempo de 120 minutos de prova a partir das 10h.

PONTUAÇÃO:

A nota da AI será a média ponderada das duas questões. A questão 1 vale 40% e a questão 2 vale 60%.



# Pontuação

A nota da AI será a média ponderada das duas questões. A questão 1 vale 40% e a questão 2 vale 60%.

# Questão 1

Para essa questão utilize o código entregue no Projeto 1A.

Implemente uma página nova para o seu **Projeto 1A**. Essa página deverá estar disponível ao acessar a rota "insper".

Ou seja, essa nova página estará disponível no endereço: http://0.0.0.0:8080/insper ou http://localhost:8080/insper

Essa página deve obrigatoriamente conter uma imagem. Você pode utilizar o HTML e a imagem disponíveis aqui. Mas se preferir tem liberdade para colocar outra imagem e modificar o HTML.

Faça o envio da pasta compactada (formato .zip ou .rar) com o seu código.

(Obs.: Este teste não aceitará vários envios. Desta forma, só envie quando tiver finalizado a questão.)

A seguinte rubrica será utilizada para corrigir esta questão:

- I: Não entregou;
- D: Entregou, mas o código não pode ser executado (ocorre algum erro que não permite que seja realizado nenhum teste);
- C: É possível acessar a página na rota definida, mas a imagem não carrega ou não é apresentada corretamente;
- B: É possível acessar a página na rota definida e a imagem é apresentada corretamente;
- A: É possível acessar a página na rota definida, a imagem é apresentada corretamente e o texto e a imagem estão centralizados horizontalmente na tela.
- A+: Existe algum botão/link na página principal do projeto 1A que leva a nova página. Além disso, o botão/link possui algum estilo css para que não pareça algo perdido na página inicial.



# Questão 2

Baseado no que você aprendeu com o Projeto 1B, crie um novo projeto em Django chamado funfacts. O funfacts é um sistema simples de cadastro de fatos interessantes, neste cadastro o sistema armazena um texto contendo algum fato interessante sobre qualquer assunto.

Além disso, o sistema deve mostrar a quantidade total de fatos interessantes cadastrados no sistema e se existir algum fato interessante cadastrado no sistema ele mostra um fato interessante aleatório.  Segue um exemplo da tela inicial do sitema:

Utilize o método .count() disponibilizado pelo Django.
Documentação: https://docs.djangoproject.com/en/4.0/ref/models/querysets/#django.db.models.query.QuerySet.count

Você pode se basear no código do Projeto 1B se preferir, mas pode ser mais fácil criar um projeto do zero.

Faça o envio da pasta compactada (formato .zip ou .rar) com o seu código. Não envie a pasta env do ambiente virtual.

(Obs.: Este teste não aceitará vários envios. Desta forma, só envie quando tiver finalizado a questão.)

A seguinte rubrica será utilizada para corrigir esta questão:

- I: Não entregou;
- D: Entregou, mas o código não pode ser executado (ocorre algum erro que não permite que seja realizado nenhum teste);
- C: É possível acessar uma página que mostra um formulário, mas a implementação de criação **ou** apresentação da quantidade de funfacts cadastradas não funciona **ou** não utiliza o método .count() pedido pelo enunciado;
- B: É possível acessar uma página que mostra um formulário **e** a quantidade de funfacts cadastradas. Além disso, é possível criar novos funfacts;
- A: Atingiu o conceito B e apresenta um funfact aleatório.
- A+: Tratou o cenário em que o sistema não possui nenhum Fun Fact cadastrado e a página inicial mostra a mensagem 'Nenhum Fun fact cadastrado'. Utilize a tag {% if %} do Django (https://docs.djangoproject.com/en/4.0/ref/templates/builtins/#if)
