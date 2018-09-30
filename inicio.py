# Algoritmo de hash
# Desenvolvido por Anderson Oliveira
# Para disciplina de criptografia de dados

import os


def cls():
    os.system(['clear', 'cls'][os.name == 'nt'])


def existe(nome_do_arquivo):
    try:
        f = open(nome_do_arquivo, 'r')
        f.close()
        return 1
    except Exception as e:
        print(e)
        return 0


def ler_arquivo_entrada():
    conteudo_arquivo = ''
    while not conteudo_arquivo:
        caminho_arquivo = str(input('Informe o caminho do arquivo de entrada: '))
        caminho_arquivo = caminho_arquivo.replace('\u202a', '')  # nos testes esse caracter sempre aparecia :'(

        with open(caminho_arquivo, 'r+b') as arquivo:
            byte = arquivo.read(64)
            print(byte)


def gerar_hash():
    ler_arquivo_entrada()
    pass


def tela_inicial():
    """
    # Irá apresentar um menu de opções ao usuário e receber sua resposta
    # caso resposta seja válida retornará o valor informado
    :return:
    # valor numerico inteiro
    """
    resposta_usuario = -1
    while resposta_usuario < 0 or resposta_usuario > 3:
        print('Escolha')
        print('1 - Gerar hash')
        print('2 - Sair')

        resposta_usuario = int(input('Entre com a opção desejada: '))

        if resposta_usuario < 0 or resposta_usuario > 2:
            cls()
            print('resposta inválida')

    return resposta_usuario


def inicio():
    resposta = 0

    while resposta != 3:
        resposta = tela_inicial()

        if resposta == 1:
            gerar_hash()
        elif resposta == 2:
            cls()
            print('Nunca será um adeus!')
            print('Até mais...')
            exit()

        cls()


print('Bem vindo')
inicio()
