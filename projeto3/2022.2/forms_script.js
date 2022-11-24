function createQuestions() {
  let alunos = [
    {group: 1, username: "andrecs11", fullname: "ANDRÉ CORRÊA SANTOS"},
    {group: 1, username: "pedropmc1", fullname: "PEDRO PAULO MORENO CAMARGO"},
    {group: 1, username: "rafaelmal", fullname: "RAFAEL MELHADO ARAUJO LIMA"},
    {group: 1, username: "andrebbm", fullname: "ANDRÉ BARBOZA BRAGA DE MELO"},
    {group: 2, username: "caiorp", fullname: "CAIO RIBEIRO DE PAULA"},
    {group: 2, username: "rodrigoap8", fullname: "RODRIGO ANCIÃES PATELLI"},
    {group: 2, username: "enzolpsb", fullname: "ENZO BOZELLI"},
    {group: 3, username: "antonioaem", fullname: "ANTÔNIO AMARAL EGYDIO MARTINS"},
    {group: 3, username: "arthurmsb", fullname: "ARTHUR MARTINS DE SOUZA BARRETO"},
    {group: 3, username: "arieltl", fullname: "ARIEL TAMEZGUI LEVENTHAL"},
    {group: 3, username: "murilopw", fullname: "MURILO PRADO WEYNE"},
    {group: 4, username: "ericalp", fullname: "ERIC ANDREI LIMA POSSATO"},
    {group: 4, username: "pedrobb", fullname: "PEDRO BITTAR BARÃO"},
    {group: 4, username: "enriccog", fullname: "ENRICCO GEMHA"},
    {group: 5, username: "joaogvr", fullname: "JOÃO GABRIEL VALENTIM ROCHA"},
    {group: 5, username: "hudsonma", fullname: "HUDSON MONTEIRO"},
    {group: 5, username: "domrsfs", fullname: "DOM RUAN SUZANO FIGUEIRA DA SILVA"},
    {group: 6, username: "giovanaca1", fullname: "GIOVANA CASSONI ANDRADE"},
    {group: 6, username: "fernandaop", fullname: "FERNANDA DE OLIVEIRA PEREIRA"},
    {group: 6, username: "marlonsp", fullname: "MARLON SILVA PEREIRA"},
    {group: 6, username: "guilhermesm9", fullname: "GUILHERME DOS SANTOS MARTINS"},
    {group: 7, username: "albertom2", fullname: "ALBERTO MANSUR"},
    {group: 7, username: "felipec13", fullname: "FELIPE CATAPANO"},
    {group: 7, username: "rafaelek2", fullname: "RAFAEL ELI KATRI"},
    {group: 7, username: "fernandogab", fullname: "FERNANDO GIUSEPPE AVILA BELTRAMO"},
    {group: 8, username: "andreb10", fullname: "ANDRÉ BRITO"},
    {group: 8, username: "arthurcm5", fullname: "ARTHUR CISOTTO MACHADO"},
    {group: 8, username: "lucasg3", fullname: "LUCAS GURGEL"},
    {group: 8, username: "victorlga", fullname: "VICTOR LUIS GAMA DE ASSIS"},
    {group: 9, username: "pedroca8", fullname: "PEDRO CLIQUET DO AMARAL"},
    {group: 9, username: "viniciusmm7", fullname: "VINICIUS MATHEUS MORALES"},
    {group: 9, username: "lincolnrpm", fullname: "LINCOLN RODRIGO PEREIRA MELO"},
    {group: 10, username: "josephkn", fullname: "JOSEPH KALLAS NETO"},
    {group: 10, username: "caiobt1", fullname: "CAIO TRAVAIN"},
    {group: 10, username: "leonardofma", fullname: "LEONARDO DA FRANÇA MOURA DE ANDRADE"},
    {group: 10, username: "arthurbf3", fullname: "ARTHUR BOSCHINI DA FONSECA"},
    {group: 11, username: "thomascc", fullname: "THOMAS CHABRO"},
    {group: 11, username: "rafaelcl", fullname: "RAFAEL COCA LEVENTHAL"},
    {group: 11, username: "caiocat", fullname: "CAIO DE CAMARGO ARANHA TIERI"},
    {group: 11, username: "felipemt3", fullname: "FELIPE TRINTIM"}]

  let groups = [...new Set(alunos.map((aluno)=>{return aluno.group}))]

  var choices = []
  var form = FormApp.openById('1xNn1b0yv0dz6yVuYTEShRb-mNumjKZtSt9DOP7XtkL0');
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
