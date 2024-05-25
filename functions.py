import json

def carregarProdutos(nomeArquivo):
    arquivo = open(nomeArquivo, 'r', encoding = 'utf8')
    conteudo = arquivo.read().strip()
    produtos = {}
    if conteudo:
        produtos = json.loads(conteudo)
        
    arquivo.close()

    return produtos

def salvarProdutos(nomeArquivo, produtos):
    arquivo = open(nomeArquivo, 'w', encoding = 'utf8')
    produtosJson = json.dumps(produtos, indent = 4, ensure_ascii = False)
    arquivo.write(produtosJson)
    arquivo.close()

def registrarLivros(dadosDosLivros):
    continua = True
    isbn = input('\nDigite o código ISBN (ex: 001): ')
    if isbn in dadosDosLivros:
        continua = False
        print('\nNúmero ISBN já CADASTRADO!!!')
        return continua, dadosDosLivros

    tituloL = input('Título do livro: ')
    autorL = input('Autor do livro: ')
    generoL = input('Gênero do livro: ')
    compraL = float(input('Preço de compra do livro: '))
    vendaL = float(input('Preço de venda do livro: '))
    qtL = int(input('Quantidade disponível do livro: '))

    dadosDosLivros[isbn] = {'titulo': tituloL, 'autor': autorL, 'genero': generoL, 'compra': float(compraL), 'venda': float(vendaL), 'quantidade': int(qtL)}

    return continua, dadosDosLivros

def listarLivros(dadosDosLivros):
    for key, dados in dadosDosLivros.items():
        print(f'{key} - {dados["titulo"]} - {dados["quantidade"]}')

def excluirLivro(dadosDosLivros):
    excluir = input('\nDigite o ISBN do livro para excluir: ')
    removeu = dadosDosLivros.pop(excluir, None)

    return removeu, dadosDosLivros

def pesquisarLivros(dadosDosLivros):
    titulo = input('\nNome do livro que deseja pesquisar: ')
    continua = True
    print(f'\n{"="*10} LIVROS ENCONTRADOS {"="*10}')

    for codigo, dados in dadosDosLivros.items():
        if dados['titulo'] == titulo:
            print(f'ISBN: {codigo}\nTitulo: {dados["titulo"]}\nAutor: {dados["autor"]}\nGênero: {dados["genero"]}\nPreço de Compra: {dados["compra"]}\nPreço de Venda: {dados["venda"]}\nQuantidade: {dados["quantidade"]}')
            continua = False
            break
        
        if titulo in dados['titulo']:
            print(f'Titulo: {dados["titulo"]}')
            continua = False

    if continua == True:
        print('Livro não existe nos dados!!!')
    
def livrosSemEstoque(dadosDosLivros):
    temLivros = False
    for key, dados in dadosDosLivros.items():
        if dados['quantidade'] == 0:
            temLivros = True
            print(f'{key} - {dados["titulo"]}')
    
    if temLivros == False:
        print('Nenhum Livro sem ESTOQUE!!!')