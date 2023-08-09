function createQuestions() {
  let alunos = [
  {group:4, username: "albertompc", fullname: "ALBERTO MARTINS PEREIRA CARRERA"},
  {group:6, username: "alexandrers3", fullname: "ALEXANDRE RODRIGUES SANTAROSSA"},
  {group:7, username: "analnf", fullname: "ANA LAIZ NOVAIS DE FARIAS"},
  {group:8, username: "arthurmt", fullname: "ARTHUR MOREIRA TAMM"},
  {group:9, username: "brunalm2", fullname: "BRUNA LIMA MEINBERG"},
  {group:2, username: "brunomlvf", fullname: "BRUNO MARQUES LI VOLSI FALCAO"},
  {group:8, username: "caioob", fullname: "CAIO ORTEGA BÔA"},
  {group:7, username: "diogopl1", fullname: "DIOGO PEREIRA LOBO"},
  {group:4, username: "douglaspbc", fullname: "DOUGLAS PABLO"},
  {group:8, username: "gabrielmmh", fullname: "GABRIEL MENDONÇA DE MELLO HERMIDA"},
  {group:1, username: "gabrielakk", fullname: "GABRIELA KATSURAYAMA"},
  {group:2, username: "gustavoeso", fullname: "Gustavo Eliziario Stevenson de Oliveira"},
  {group:1, username: "gustavoms7", fullname: "GUSTAVO MENDES DA SILVA"},
  {group:7, username: "isabellasa", fullname: "ISABELLA DOS SANTOS DE AMORIM"},
  {group:3, username: "joaoagg", fullname: "JOÃO ANTÔNIO GOMES GARCIA"},
  {group:5, username: "joaoprs3", fullname: "JOÃO PEDRO RODRIGUES SANTOS"},
  {group:3, username: "juliaf1", fullname: "JULIA FIGUEIREDO"},
  {group:1, username: "kevinns", fullname: "KEVIN NAGAYUKI SHINOHARA"},
  {group:9, username: "luanawa", fullname: "LUANA WILNER ABRAMOFF"},
  {group:2, username: "lucam1", fullname: "LUCA MIZRAHI"},
  {group:10, username: "lucash", fullname: "LUCAS HIX"},
  {group:6, username: "lucasno", fullname: "LUCAS NOVAIS DE OLIVEIRA"},
  {group:5, username: "matheusc1", fullname: "MATHEUS RAFFAELLE NERY CASTELLUCCI"},
  {group:1, username: "nicolasey", fullname: "NICOLAS ENZO YASSUDA"},
  {group:3, username: "pedroagml", fullname: "PEDRO AUGUSTO GEVE DE MORAES LACERDA"},
  {group:10, username: "pedrobp1", fullname: "PEDRO BALBO PORTELLA"},
  {group:3, username: "pedrolfa", fullname: "PEDRO FRACASSI"},
  {group:4, username: "pedrogsd", fullname: "PEDRO GOMES DE SÁ DRUMOND"},
  {group:6, username: "pedrohrc1", fullname: "PEDRO HENRIQUE RIZO COLPAS"},
  {group:4, username: "pedroial", fullname: "PEDRO IVO AMARAL LIMA"},
  {group:8, username: "pedrotpc", fullname: "PEDRO TOLEDO PIZA CIVITA"},
  {group:10, username: "rafaelpn1", fullname: "RAFAEL PASCARELLI NICCHERI"},
  {group:5, username: "rodrigopm6", fullname: "RODRIGO PAOLIELLO DE MEDEIROS"},
  {group:10, username: "talesitf", fullname: "TALES IVALQUE TAVEIRA DE FREITAS"},
  ]

  let groups = [...new Set(alunos.map((aluno)=>{return aluno.group}))]

  var choices = []
  var form = FormApp.openById('1cgx06_Br705ATWAIaXKjCoq8HKZrwahmoQLjXGHm02w');
  var item = form.addListItem();
  item.setTitle('Selecione o seu Nome')
  item.setRequired(true);


  groups.map((group)=>{
    let nomes_do_grupo = alunos.filter(aluno => aluno.group == group).map(aluno => aluno.fullname);

    //Criando seção para cada grupo
    let secao_item = form.addPageBreakItem()
      .setTitle(`GRUPO ${group}`)
      .setGoToPage(FormApp.PageNavigationType.SUBMIT)
      .setHelpText(`Perguntas referêntes ao grupo \n\n- ${nomes_do_grupo.join("\n- ")}\n\nNa linha com o seu nome, faça a sua autoavaliação`);
    
    // Criando grid para PRODUTIVIDADE
    var grid_produtividade = form.addGridItem();
    grid_produtividade
      .setTitle('Qual nível de PRODUTIVIDADE cada membro teve na sprint anterior? (LEIA A RUBRICA, POIS ISSO NÃO É SIMPLESMENTE UMA NOTA)\n\nNa linha com o seu nome, faça a sua autoavaliação')
      .setRequired(true)
      .setRows(nomes_do_grupo)
      .setColumns(['1', '2', '3', '4', '5']);

        // Criando grid para PROATIVIDADE
      var grid_proatividade = form.addGridItem();
      grid_proatividade
      .setTitle('Qual nível de PROATIVIDADE cada membro teve na sprint anterior? (LEIA A RUBRICA, POIS ISSO NÃO É SIMPLESMENTE UMA NOTA)\n\nNa linha com o seu nome, faça a sua autoavaliação')
      .setRequired(true)
      .setRows(nomes_do_grupo)
      .setColumns(['1', '2', '3', '4', '5']);

      // Criando grid para TRANSPARÊNCIA
      var grid_transparencia = form.addGridItem();
      grid_transparencia
      .setTitle('Qual nível de TRANSPARÊNCIA cada membro teve na sprint anterior? (LEIA A RUBRICA, POIS ISSO NÃO É SIMPLESMENTE UMA NOTA)\n\nNa linha com o seu nome, faça a sua autoavaliação')
      .setRequired(true)
      .setRows(nomes_do_grupo)
      .setColumns(['1', '2', '3', '4', '5']);


    //Vinculando seção com opção
    nomes_do_grupo.map((aluno)=>{
      choices.push(item.createChoice(aluno, secao_item));
    });

  });
  item.setChoices(choices);


}

