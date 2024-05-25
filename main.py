from functions import *

arquivo = 'dadosLivros.json'
dadosDosLivros = carregarProdutos(arquivo)

while True:
    print(
        '\n1 - Registrar novos livros.',
        '\n2 - Listar livros.',
        '\n3 - Excluir livro.',
        '\n4 - Pesquisar livros.',
        '\n5 - Relatório de livros sem estoque.'
    )
    
    opcao = input('\nDigite a opção (0 para encerrar): ')

    if opcao == '0':
        break

    elif opcao == '1':
        continua, dadosDosLivros = registrarLivros(dadosDosLivros)
        if continua == True:
            salvarProdutos('dadosLivros.json', dadosDosLivros)

    elif opcao == '2':
        print(f'\n{"="*10} LIVROS CADASTRADOS {"="*10}')
        listarLivros(dadosDosLivros)

    elif opcao == '3':
        removeu, dadosDosLivros = excluirLivro(dadosDosLivros)
        if removeu == None:
            print('\nCódigo ISBN inexistente!!!')
        else:
            salvarProdutos('dadosLivros.json', dadosDosLivros)
    
    elif opcao == '4':
        pesquisarLivros(dadosDosLivros)
    
    elif opcao == '5':
        print(f'\n{"="*10} LIVROS SEM ESTOQUE {"="*10}')
        livrosSemEstoque(dadosDosLivros)