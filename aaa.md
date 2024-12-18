# Dependencias
    Flask ou SQLalchemy
    numpy
    pypi


# Atividade da Aula 2

0. 
    1. crie uma rota para uma pag web, com uma tag canvas, que permite ao usuário deslocar uma fotografia para a diretia e para a esquerda

    2. crie uma rota que permita ao usuário capturar uma fotografia da webcam

    3. crie uma rota com uma página web sem table que exiba uma tabela com 997 linhas e 5 colunas, com ID,  nome, sobrenome, e-mail, ações

    4. criar uma rota com tres links, uma para cada atividade acima, de forma bem estilizadas

    5. crie 6 rotas onde cada um envie o currículo de um integrante do grupo


# Atividade Aula 3

0. 

    1. considerando um usuário e uma senha mocados faça uma página de autenticaçao que retorne a mesangem olá "nome" se tudo funcionar, ou "usuário ou senha não confere"

    2. Limite as tentativas de autenticação do usuário da questão 1 em duas vezes

    3. Estilizar de forma bonita as paginas criadas

    4. Escreva um script python que gere automaticamente um template html contendo um formulário de input de dados com campos que serão recebidos atravez de um payload de JSON

    5. Incremente o script python da questão 4 para que após gerar o template, ele construa automaticamente uma rota que permita visualizar o template. 

    6. Crie uma classe python que encapsula dados de usuário, de uma pessoa, e desenvolva uma função de autenticação que faça as devidas validações

# Aula 4

0. Regrinhas básicas
    1. não confiar nos dados que chegam de uma requisição (validar todos os dados que chegam)
    2. garantir integridade e consistência dos dados de uma forma que possa ser recuperado e seja persistente 
    3. Que seja uma resposta assíncrona ou um sistema que retorne em tempo hábil
    4. Tratar as exceções
    5. SQLite

# ATividade aula 4

0. 

    1. fazer, no código, todas as validações necessárias para que as senha e ususario sejam devidamente preenchiddos
    2. tratar excessões para evitar que seja exibida a mensagem "method not allowed"
    3. Garantir que usuário seja redirecionado e tentar autenticar novamente caso a senha e o user estejam incorretos
    4. limitar em duas tentativas
    5. Alterar todos os retornos possíveis, usadando dados formatados em JSON
