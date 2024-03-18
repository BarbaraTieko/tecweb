# Guia de instalação do Docker para Windows

Para instalar o Docker no Windows será necessário utilizar a ferramenta WSL 2 (Windows Subsystem for Linux).
O guia que você vai encontrar abaixo foi baseada na seguinte fonte: [https://learn.microsoft.com/en-us/windows/wsl/install](https://learn.microsoft.com/en-us/windows/wsl/install){:target="_blank"}

Caso tenha dúvidas, sugiro que acesse o link acima para mais informações.

## Habilitando opção de Subsistema do Windows para Linux

1. Abra o PowerShell como administrador e execute o seguinte comando:

```shell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

## Instalando WSL CLI

1. Abra o PowerShell como administrador e execute o seguinte comando:

```shell
wsl --install
```

!!! tip "Caso não ocorra nada"
    Caso o `wsl` já esteja instalado, o comando apenas mostrará uma lista de opções. Neste caso, siga para o próximo passo.

## Instalando o Ubuntu

```shell
wsl --install -d Ubuntu
```

### Outra forma de instalar o Ubuntu

Caso queira, você pode instalar o Ubuntu através da Microsoft Store. Basta pesquisar por "Ubuntu" e instalar a versão mais recente.

## Configurando o usuário e senha no Ubuntu

Na barra de busca do Windows, pesquise por "Ubuntu" e abra o terminal. Será solicitado que você crie um usuário e senha.

Pronto! Agora volte para o handout e continue a instalação do Docker.

## Links úteis

- [https://docs.docker.com/desktop/wsl/](https://docs.docker.com/desktop/wsl/){:target="_blank"}
- [https://docs.microsoft.com/en-us/windows/wsl/install](https://docs.microsoft.com/en-us/windows/wsl/install){:target="_blank"}


<!-- 
Install using Command Prompt
Step 1: Start CMD with administrative privileges.
Step 2:Execute "wsl --install" command.
Step 3:Run "wsl -l -o" to list other Linux releases.
Step 4:You can install your favorite Linux distribution, use "wsl --install -d NameofLinuxDistro."
When the operation is finished, restart your PC.You can start the Linux distribution from your Start menu.
 
Install Using Windows Features
Step 1:Open the Start menu and type "Windows features" into the search bar and click on "Turn Windows Features On or Off".
Step 2:Tick the "Windows Subsystem for Linux" checkbox and press the “OK” button.
Step 3:When the operation is complete, you will be asked to restart your computer. -->


