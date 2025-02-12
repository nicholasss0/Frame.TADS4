# Dependencias
    Flask ou SQLalchemy
    numpy
    pypi


# Atividade da Aula 2

0. 
    1. crie uma rota para uma pag web, com uma tag canvas, que permite ao usuário deslocar uma fotografia para a direita e para a esquerda; feito

    2. crie uma rota que permita ao usuário capturar uma fotografia da webcam; feito

    3. crie uma rota com uma página web sem table que exiba uma tabela com 997 linhas e 5 colunas, com ID,  nome, sobrenome, e-mail e ações; feito

    4. criar uma rota com tres links, uma para cada atividade acima, de forma bem estilizadas; feito



# Atividade Aula 3

0. 

    1. considerando um usuário e uma senha mocados faça uma página de autenticaçao que retorne a mesangem olá "nome" se tudo funcionar, ou "usuário ou senha não confere"; feito

    2. Limite as tentativas de autenticação do usuário da questão 1 em duas vezes; feito

    3. Estilizar de forma bonita as paginas criadas; feito

    4. Escreva um script python que gere automaticamente um template html contendo um formulário de input de dados com campos que serão recebidos atravez de um payload de JSON; feito

    5. Incremente o script python da questão 4 para que após gerar o template, ele construa automaticamente uma rota que permita visualizar o template. feito

    6. Crie uma classe python que encapsula dados de usuário, de uma pessoa, e desenvolva uma função de autenticação que faça as devidas validações; feito

# Aula 4

0. Regrinhas básicas
    1. não confiar nos dados que chegam de uma requisição (validar todos os dados que chegam)
    2. garantir integridade e consistência dos dados de uma forma que possa ser recuperado e seja persistente 
    3. Que seja uma resposta assíncrona ou um sistema que retorne em tempo hábil
    4. Tratar as exceções
    5. SQLite

## Atividade aula 4

0. 

    1. fazer, no código, todas as validações necessárias para que as senha e usuario sejam devidamente preenchiddos feito

    2. tratar excessões para evitar que seja exibida a mensagem "method not allowed" feito

    3. Garantir que usuário seja redirecionado e tentar autenticar novamente caso a senha e o user estejam incorretos feito

    4. limitar em duas tentativas feito
 
    5. Alterar todos os retornos possíveis, usando dados formatados em JSON


# Atividades aula 8:

## Mini-blog Pessoal:

Objetivo da atividade: 
Criar uma aplicação simples para postar pequenos textos com data e hora.

Funcionalidades:
- Formulário para adicionar novos posts.
- Lista de posts na página inicial, ordenados por data.
- Utilização de templates para formatar a página.

Dicas:
- Utilizar uma lista em Python para armazenar os posts.
- Usar o módulo datetime para registrar a data e hora de cada post.
- Criar um template básico com HTML e CSS para estilizar a página.

Tempo: 30 minutos. Tempo não é longo, portanto, o foco deve ser em funcionalidades básicas.

Aprendizado: O objetivo principal é praticar os conceitos aprendidos e explorar novas possibilidades com o Flask.

Ferramentas: Recomenda-se utilizar um editor de código com suporte a Python e Flask, como o Visual Studio Code.

Proibido usar Internet.

    
## Página de autenticação básica:

Objetivo da atividade: 
Criar uma aplicação simples para comparar se o usuário e a senha digitados estão corretos.

Funcionalidades:
- Formulário para informar usuário e senha.
- Dicionário para armazenar o usuário e senha cadastrados.
- Utilização de templates para formatar a página.
- Retornar mensagens de sucesso ou falha na autenticação.

Dicas: 
- Utilizar lista para armazenar as tentativas de autenticação.
- Usar o módulo datetime para registrar a data e hora de login.
- Criar um template básico com HTML e CSS para estilizar a página.

Tempo: 30 minutos. Tempo não é longo, portanto, o foco deve ser em funcionalidades básicas.

Aprendizado: O objetivo principal é praticar os conceitos aprendidos e explorar novas possibilidades com o Flask.

Ferramentas: Recomenda-se utilizar um editor de código com suporte a Python e Flask, como o Visual Studio Code.

Proibido usar Internet.


## Página de upload de fotos:

Objetivo da atividade: 
- Criar uma aplicação simples para fazer upload de imagens.

Funcionalidades:
- Formulário para escolher o arquivo a partir do computador do usuário.
- Armazenar os arquivos enviados pelos usuários em uma pasta.
- Utilização de templates para formatar a página.
- Retornar mensagens de sucesso ou falha na autenticação. Em caso de sucesso, deve-se retornar também o path de onde o arquivo foi armazenado no servidor.

Dicas:
- Utilizar lista para armazenar os arquivos enviados.
- Usar o módulo datetime para registrar a data e hora do upload do arquivo.
- Criar um template básico com HTML e CSS para estilizar a página.

Tempo: 30 minutos. Tempo não é longo, portanto, o foco deve ser em funcionalidades básicas.

Aprendizado: O objetivo principal é praticar os conceitos aprendidos e explorar novas possibilidades com o Flask.

Ferramentas: Recomenda-se utilizar um editor de código com suporte a Python e Flask, como o Visual Studio Code.

Proibido usar Internet.