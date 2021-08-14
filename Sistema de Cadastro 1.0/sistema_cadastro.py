import os

lista_produtos = list()
itens = dict()


# ROTINA PARA LIMPAR A TELA
def limpa_tela() :
	os.system('cls')


# ROTINA PARA EXIBIR O MENU PRINCIPAL
def menu_principal() :

	continua_001 = True
	while continua_001 == True :
		print(f"{'MENU PRINCIPAL':<45}")
		print()
		print(f"{'1 - ':<3}{'Cadastro':<45}")
		print(f"{'2 - ':<3}{'Consulta':<45}")
		print(f"{'3 - ':<3}{'Remoção':<45}")
		print(f"{'4 - ':<3}{'Reservado ao sistema':<45}")
		print(f"{'5 - ':<3}{'Reservado ao sistema':<45}")
		print(f"{'6 - ':<3}{'Reservado ao sistema':<45}")
		print(f"{'9 - ':<3}{'SAIR':<45}")
		esc_001 = str(input("\nDigite uma opção : "))

		if esc_001 == "1" :
			cadastrar()

		elif esc_001 == "2" :
			consultar()

		elif esc_001 == "3" :
			remover()

		elif esc_001 == "9" :
			continua_002 = True
			while continua_002 == True :
				esc_002 = str(input("Deseja sair do programa [ S / N ] ? ")).strip().lower()[0]
				if esc_002 == "s" :
					continua_001 = False
					continua_002 = False

				elif esc_002 == "n" :
					continua_001 = True
					continua_002 = False

				else :
					print("Opção inválida !")
					continua_001 = True
					continua_002 = True

		elif esc_001 in ("4","5","6") :
			print("Opção reservada ao sistema. Tente outra opção.")
			continua_001 = True

		else :
			print("Opção inválida !")

	print()
	print("PROGRAMA FINALIZADO")


# ROTINA PARA EXIBIR O MENU CADASTRAR
def cadastrar() :
	limpa_tela()

	continua_001 = True
	while continua_001 == True :
		qtd_itens = str(input("Digite a quantidade de produtos a serem cadastrados : ")).strip()
		if qtd_itens.isnumeric() == False :
			print("Digite apenas números.")
			continua_001 = True
		else:
			continua_001 = False

	qtd_itens = int(qtd_itens)
	for contador in range ( 0, qtd_itens ) :

		itens["Nome"] = str(input("Digite o nome do produto : ")).strip()
		itens["Descricao"] = str(input("Digite a descrição do produto : ")).strip()
		itens["Quantidade"] = int(input("Digite a quantidade a ser cadastrada : "))
		itens["Valor"] = float(input("Digite o valor unitário do produto : "))
		print()
		lista_produtos.append(itens.copy())
		itens.clear()


# ROTINA PARA EXIBIR O MENU CONSULTAR
def consultar() :
	limpa_tela()
	print("Consulta de Produto cadastrado")
	print(f"Quantidade de produtos cadastrados: {len(lista_produtos)}\n")
	print(f"{'NOME':<25}{'DESCRIÇÃO':<25}{'QUANTIDADE':<12}{'VALOR UNITÁRIO':<12}")
	for contador in range ( 0, len(lista_produtos)) :
		print(f"{lista_produtos[contador]['Nome']:<25}{lista_produtos[contador]['Descricao']:<25}{lista_produtos[contador]['Quantidade']:<12}{lista_produtos[contador]['Valor']:<12}")
	print()


# ROTINA PARA EXIBIR O MENU REMOVER
def remover() :
	limpa_tela()
	print("Remoção de Produto cadastrado")


# PROGRAMA PRINCIPAL
print(f"{'Programa : Cadastro 1.0':<60}")
print()

menu_principal()
