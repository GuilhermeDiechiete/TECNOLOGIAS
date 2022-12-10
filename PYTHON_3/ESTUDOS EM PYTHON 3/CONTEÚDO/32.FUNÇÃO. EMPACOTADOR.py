def estoque(* nome):
    nome = produto
    print(produto)



while True:
    produto = str(input('Digite o Produto:'))
    continuar = str(input('Deseja Cadastrar mais [S|N]:')).strip().upper()
    if continuar == 'S':
        continue
    else:
        break

estoque()


