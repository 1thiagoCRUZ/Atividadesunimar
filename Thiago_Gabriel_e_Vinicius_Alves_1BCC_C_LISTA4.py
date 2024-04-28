#TRABALHO REALIZADO POR:
#-----! THIAGO GABRIEL SILVA BRAGA DA CRUZ -----!#
#-----! VINÍCIUS ALVES DE SANTANA -----!#


def exercicio6():
    lista_n = [2,5,8,11,14]
    for idx, nmr_impar in enumerate(lista_n):
        if nmr_impar % 2 != 0:
            print(f"Indíce: {idx} | Número ímpar: {nmr_impar}")

def exercicio7():
    lista_divisiveis_tres = []
    cont = 0

    while cont <= 100:
        cont += 1
        if cont % 3 == 0:
            lista_divisiveis_tres.append(cont)
            continue
    print(lista_divisiveis_tres)

def exercicio8():
    while True:
        qntdUsers = int(input("Quantos usuários deseja cadastrar (min. 10): "))
        if qntdUsers >= 10:
                break
        else:
            print("Informe um número válido para a o cadastro.")
    cont = 0
    lista_users = []

    for users in range(qntdUsers):

            cont += 1
            nomes = input(f"Digite o nome da {cont}ª pessoa: ")
            lista_users.append(nomes)
    print("\nLista de nomes:")
    for idx, user in enumerate(lista_users):
        print(f"{idx}. {user}.")

def exercicio9():
    while True:
        qntdCompra = int(input("Quantos produtos deseja colocar em sua lista de compras (min. 10): "))
        if qntdCompra >= 10:
            break
        else:
            print("Informe um número válido!")
    lista_compra = []
    cont = 0


    for produtos in range(qntdCompra):
        cont += 1
        lista_compra.append(input(f"Digite o nome do {cont}º produto que deseja adicionar em sua lista: "))
    
    print("\nLista de compras:")
    for idx, prod in enumerate(lista_compra):
        print(f"{idx}. {prod}")
    
   
    while lista_compra:
         compra = input("Informe qual produto está comprando (pelo nome do produto): ")
         if compra in lista_compra:
             lista_compra.remove(compra)
             print(f"Produtos restantes: {lista_compra}")

             if len(lista_compra) == 0:
                 print("Acabaram os itens da lista 😊")
         else:
             print("O produto informado não existe na lista. Tente informar um produto válido!")
                        
def exercicio10():
    lista_jogo = []
    lista_preco = []
    lista_avaliacao = []
    cont = 0

    qntd = int(input("Informe quantos jogos deseja cadastrar: "))

    for cont in range(qntd):
        cont +=1
        jogo = input(f"Informe o nome do {cont}º jogo: ")
        preco = float(input(f"Informe o preço do {jogo}: "))
        
        while True:
            avaliacao = float(input(f"Informe a nota de avaliação do {jogo} (nota de 1 a 10): "))
            if avaliacao >= 1 and avaliacao <=10:
                break
            else:
                print("Informe um número válido para a avaliação.")
        print("")
        lista_jogo.append(jogo)
        lista_preco.append(preco)
        lista_avaliacao.append(avaliacao)
    
    #max e min são utilizados para pegar o maior valor encontrado na lista e o menor valor encontrado na lista
    melhor_avaliado = max(lista_avaliacao)
    pior_avaliado = min(lista_avaliacao)
    mais_caro = max(lista_preco)
    mais_barato = min(lista_preco)

    for idx, jogo in enumerate(lista_jogo):
        if lista_avaliacao[idx] == melhor_avaliado:
            print("Jogo com a MELHOR avaliação:")
            print(f"Nome: {jogo}, Preço: {lista_preco[idx]}, Nota: {melhor_avaliado}\n")

        if lista_avaliacao[idx] == pior_avaliado:
            print("Jogo com a PIOR avaliação:")
            print(f"Nome: {jogo}, Preço: {lista_preco[idx]}, Nota: {pior_avaliado}\n")
        
        if lista_preco[idx] == mais_caro:
            print("Jogo mais CARO:")
            print(f"Nome: {jogo}, Preço: {mais_caro}, Nota: {lista_avaliacao[idx]}\n")

        if lista_preco[idx] == mais_barato:
         print("Jogo mais BARATO:")
         print(f"Nome: {jogo}, Preço: {mais_barato}, Nota: {lista_avaliacao[idx]}\n")

    print("Lista de todos os jogos e suas informações:")
    print("------------------------------------------")
    for idx, jogo in enumerate(lista_jogo):
        preco = lista_preco[idx]
        print(f"Nome: {jogo}, Preço: {preco}, Nota: {lista_avaliacao[idx]}")
    
    print("------------------------------------------")

#Todos os exercícios abaixo
todos_exercicios = {
    6: exercicio6,
    7: exercicio7,
    8: exercicio8,
    9: exercicio9,
    10: exercicio10
}
opcao = ''

while opcao.lower() != 'sair':
    exercicio_escolhido = int(input("Temos 10 exercícios! Informe o número do exercício que deseja executar (Ex: 1): "))
    if exercicio_escolhido in todos_exercicios:
        exercicio = todos_exercicios[exercicio_escolhido]()
    
    else:
        print("Exercício informado não existe")
    
    opcao = input("Deseja continuar? Para parar digite sair: ")
