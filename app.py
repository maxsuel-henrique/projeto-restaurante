import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                    {'nome':'Pizza Superma', 'categoria':'Pizza', 'ativo':True},
                    {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def exibir_nome_do_programa(): 
    print ('''𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤
       ''')

def exibir_opcoes():
    print ('1. Cadastrar restaurantes')
    print ('2. Listar restaurantes')
    print ('3. Alternar estado do restaurante')
    print ('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando app....')

def voltar_ao_menu_principal():
    input ('digite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    print ('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(texto)
    print()


def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}:')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listar os restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(22)} | {'Status'} ')
    for restaurante in restaurantes:
        nome_restaurantes = restaurante ['nome']
        categoria_restaurantes = restaurante ['categoria']
        ativo = 'Ativado' if restaurante ['ativo'] else 'Desativado'      
        print (f' - {nome_restaurantes.ljust(20)} | {categoria_restaurantes.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado restaurante')
    nome_restaurante = input ('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False 

    for restaurante in restaurantes:
        if nome_restaurante == restaurante ['nome']:
            restaurante_encontrado = True 
            restaurante ['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativdado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso! '
            print(mensagem)
    if not restaurante_encontrado:
        print ('O restaurante não foi encontrado')


    voltar_ao_menu_principal()

def escolher_opcoes():

    try:
        opcao_escolhida = int(input ('Escolha uma opcao: '))
        print (f'Você escolheu a opcao:{opcao_escolhida}' )

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()    
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
    
if __name__ == '__main__':
    main() 