# Instalação WLS

Todo o passo a passo a seguir foi retirado de: https://learn.microsoft.com/pt-br/windows/wsl/install-manual

- Na busca do windows, busque por: `Turn Windows features on or off` (Pt: `Ativar ou desativar recursos do Windows`)
  - Marque as opções:
      - `Virtual Machine Plataform` (Pt: `Plataforma de Máquina Virtual`)
      - `Windows subsystem for Linux` (Pt: `Subsistema do Windows para Linux`)
  - Reinicie o computador

- Instale alguma distribuição Linux de sua preferência;
- Inicialize o SO Linux que você acabou de instalar e configure um usuário;
- No terminal PowerShell, teste o comando `wsl --help`. Se tudo der certo, será listado algumas informações.
- Acesse o [link](https://learn.microsoft.com/pt-br/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package) e baixe a atualização do kernel do Linux.
    - Execute a atualização
- Execute o comando `wsl --list` no PowerShell para verificar quais distribuições estão disponíveis.
- Execute o comando a seguir no PowerShell. Substitua `<DISTRIBUICAO>` pelo nome da distribuição que você baixou:

        wsl --set-default-version <DISTRIBUICAO> 2

## Docker

- Faça a instalação do Docker, caso ainda não tenha feito;
- Abra o Docker Desktop;
    - Clique em configuração

    - Resources > WSL Integration
      - Enable integration with additional distros
