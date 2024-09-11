import os

def processar_resposta(resposta,nome):
    if resposta == '1':
        print(f'{os.linesep}{nome} a marcação de consulta pode ser feita atraves do nosso contato 81 xxxx-xxxx.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome} os orçamentos podem ser solicitados atravez do nosso email juliana@gmail.com, lembrando que os exames tem que estar em anexo!{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome} para duvidas ligue para o 81 xxxx-xxxx!{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome} funcionamos de Seg a Sex das 09h às 17h e ao sábados de 09h as 13h!{os.linesep}')
    else:
        print('Digite apenas 1, 2, 3 ou 4')

def start():
    #Apresentar o chatbot
    print('Olá! Bem-vindo(A) a Dra. Juliana')
    # pedir o nome
    nome = input('Digite seu nome: ')
    # pedir e-mail
    email = input('Digite seu email: ')
    while True:
    # Oferecer o menu de opções
        resposta = input(
            f'Como podemos te ajudar hoje {nome}?{os.linesep}[1] - Marcação de consulta?{os.linesep}[2] - Orcamentos?{os.linesep}[3] - Duvidas?{os.linesep}[4] - Horário de funcionamento?{os.linesep}')
    # Processar a resposta enviada
        processar_resposta(resposta,nome)


if __name__ == '__main__':
    start()