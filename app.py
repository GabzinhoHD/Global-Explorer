import os
viagens = [{"nome": "Pedro Pedro", "Destino": "Rio de Janeiro", "ativo": True},
           {"nome": "Isabel Roberta", "Destino": "São Paulo", "ativo": False},
           {"nome": "Vinicius Rosa", "Destino": "New York", "ativo": True},
           {"nome": "Gustavo Erique", "Destino": "Malé", "ativo": True}]
    
def exibir_titulo():
    print("""🅖🅛🅞🅑🅐🅛 🅔🅧🅟🅛🅞🅡🅔🅡\n""")


def exibir_opcao():
    print('1. Cadastrar Viajante')
    print('2. Listar Viagem')
    print('3. Ativar Cadrastro')
    print('4. Sair\n')

def escolher_opcao():

    def exibir_subtitulo(texto):
        os.system('cls')
        print(texto)
        print(" ")

    def retorna_menu():
        input("Aperte para retornar")
        main()


    def cadrastro_viagem():
        exibir_subtitulo("Cadastro de viagens")
        destino_viagem = input("Digite o destino da sua viagem: ")
        viagens.append(destino_viagem)
        print(f" A viagem {destino_viagem} foi cadrastada com exito")
        retorna_menu()

    def lista_viagens():
        exibir_subtitulo("Lista de Viagens")
        for viagem in viagens:
            nome_pessoa = viagem["nome"]
            destino_pessoa = viagem["Destino"]
            ativo = viagem["ativo"]
            print(f" - {nome_pessoa} | {destino_pessoa} | {ativo} ")
        retorna_menu()

    def ativar_cadrastro():
        exibir_subtitulo("Ativar cadastro de viagem")
        retorna_menu()
        

    def finalizar_app():
        os.system('cls')
        print("Finalizando programa")

    def opcao_invalida():
        print("Opçao Invalida")
        input("Aperte um botão para retornar")
        main()

    opcao_escolhida = int(input('Escolha uma opção:'))
    try:
        if opcao_escolhida == 1:
            cadrastro_viagem()
        elif opcao_escolhida == 2:
            lista_viagens()
        elif opcao_escolhida == 3:
            ativar_cadrastro()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_titulo()
    exibir_opcao()
    escolher_opcao()

if __name__ == "__main__":
    main()
