import os

lista_produtos = list()
itens = dict()


# ROTINA PARA LIMPAR A TELA
def limpa_tela():
	os.system('cls')


# ROTINA PARA EXIBIR O MENU PRINCIPAL
def menu_principal():
	#limpa_tela()
	continua_001 = True
	while continua_001 == True:
		print("\033[0;30;46m{:>50}\033[m".format("Programação Python "))
		print("\033[0;40m{:>50}\033[m".format("Equipe CFM "))
		print("\033[37m{:>50}\033[m".format("Programa 001 : Controle de Estoque Ver 1.0 + git"))
		print(f"\n\n\033[1;30;44m{' MENU PRINCIPAL':<50}\033[m")
		print()
		print(f"{' 1 - ':<3}\033[0;30;44m{' Cadastro de itens':<45}\033[m")
		print(f"{' 2 - ':<3}\033[0;30;44m{' Consulta de itens cadastrados':<45}\033[m")
		print(f"{' 3 - ':<3}\033[0;30;44m{' Remoção de itens':<45}\033[m")
		print(f"{' 4 - ':<3}\033[0;30;44m{' Reservado ao sistema':<45}\033[m")
		print(f"{' 5 - ':<3}\033[0;30;44m{' Reservado ao sistema':<45}\033[m")
		print(f"{' 6 - ':<3}\033[0;30;44m{' Reservado ao sistema':<45}\033[m")
		print(f"{' 9 - ':<3}\033[1;30;41m{' SAIR DO PROGRAMA':<45}\033[m")
		esc_001 = str(input(f"\n\033[1;30;42m{' Digite uma opção :':<20}\033[m"))


		if esc_001 == "1":
			cadastrar()

		elif esc_001 == "2":
			consultar()

		elif esc_001 == "3":
			remover()

		elif esc_001 == "4":
			print("Menu criado apenas para fins de teste e recordação de dicionários dentro de listas")
			for contador in range(0, len(lista_produtos)):
				for k, v in lista_produtos[0].items():
					print(f"a chave é {k} e o valor é {v}")

		elif esc_001 == "9":
			continua_002 = True
			while continua_002 == True:
				esc_002 = str(input("Deseja sair do programa [ S / N ] ? ")).strip().lower()[0]
				if esc_002 == "s":
					continua_001 = False
					continua_002 = False

				elif esc_002 == "n":
					continua_001 = True
					continua_002 = False

				else:
					print("Opção inválida !")
					continua_001 = True
					continua_002 = True

		elif esc_001 in ("5", "6"):
			print("Opção reservada ao sistema. Tente outra opção.")
			continua_001 = True

		else:
			print("Opção inválida !")

	print()
	print("PROGRAMA FINALIZADO")


# ROTINA PARA EXIBIR O MENU CADASTRAR
def cadastrar():
	#limpa_tela()
	print("\nMENU CADASTRO DE PRODUTO")

	continua_001 = True
	while continua_001 == True:
		qtd_itens = str(input("Digite a quantidade de produtos a serem cadastrados : "))
		if qtd_itens.isnumeric() == False:
			print("Digite apenas números...")
			continua_001 = True
		else:
			continua_001 = False

	qtd_itens = int(qtd_itens)

	for contador_001 in range(0, qtd_itens):

		continua_002 = True
		while continua_002 == True:

			continua_003 = True
			while continua_003 == True:
				itens['Codigo'] = input("Digite o código do produto : ")
				if itens['Codigo'].isdigit() == False:
					print("\nCódigo do produto inválido ! Tente novamente ...")
					continua_003 = True
				else :
					continua_003 = False

			for contador_002 in range(0, len(lista_produtos)):
				if itens['Codigo'] == lista_produtos[contador_002]['Codigo']:
					print("O código informado já pertence a um item cadastrado ! Tente novamente ...")
					continua_002 = True
					break
				else :
					continua_002 = False

		itens["Nome"] = input("Digite o nome do produto : ").strip()

		itens["Descricao"] = input("Digite a descrição do produto : ").strip()

		continua_004 = True
		while continua_004 == True:
			quantidade_itens = input("Digite a quantidade a ser cadastrada : ")
			if quantidade_itens.isdigit() == True:
				itens["Quantidade"] = quantidade_itens
				continua_004 = False
			else:
				print("Quantidade do produto inválido ! Tente novamente ...")
				continua_004 = True

		continua_005 = True
		while continua_005 == True:
			valor_item = input("Digite o valor unitário do produto : ").strip().replace(',', '.')
			if valor_item.replace('.', '').isdigit():
				itens["Valor"] = float(valor_item)
				continua_005 = False
			else:
				print('O valor informado é inválido !')
				continua_005 = True

		valor_item = float(valor_item)
		quantidade_itens = int(quantidade_itens)

		itens["valor total"] = ( quantidade_itens * valor_item )

		print()

		lista_produtos.append(itens.copy())
		salvar_produto(itens)
		itens.clear()


# ROTINA PARA EXIBIR O MENU CONSULTAR
def consultar():
	#limpa_tela()
	print("\nMENU CONSULTA DE PRODUTO CADASTRADO")
	print(f"Quantidade de produtos cadastrados : {len(lista_produtos)}\n")
	print(f"{'CÓDIGO':<9}{'NOME':<32}{'DESCRIÇÃO':<68}{'QUANTIDADE':<10}{'VALOR UNITÁRIO':>17}{'VALORES TOTAIS':>19}")
	for contador in range(0, len(lista_produtos)):
		print(f"{lista_produtos[contador]['Codigo']:<9}{lista_produtos[contador]['Nome']:<32}{lista_produtos[contador]['Descricao']:<68}{lista_produtos[contador]['Quantidade']:>10}{'R$':>5}{lista_produtos[contador]['Valor']:>12.2f}{'R$':>7}{lista_produtos[contador]['valor total']:>12.2f}")
	print()


# ROTINA PARA EXIBIR O MENU CONSULTAR DE FORMA SIMPLIFICADA
def consultar_simples():
	print(f"{'CÓDIGO':<9}{'NOME':<32}{'DESCRIÇÃO':<68}{'QUANTIDADE':<10}{'VALOR UNITÁRIO':>17}{'VALORES TOTAIS':>19}")
	for contador in range(0, len(lista_produtos)):
		print(f"{lista_produtos[contador]['Codigo']:<9}{lista_produtos[contador]['Nome']:<32}{lista_produtos[contador]['Descricao']:<68}{lista_produtos[contador]['Quantidade']:>10}{'R$':>5}{lista_produtos[contador]['Valor']:>12.2f}{'R$':>7}{lista_produtos[contador]['valor total']:>12.2f}")
	print()


# ROTINA PARA EXIBIR O MENU REMOVER
def remover():
	continua_001 = True
	while continua_001 == True:
		print("\nMENU REMOÇÃO DE PRODUTO CADASTRADO\n")
		consultar_simples()
		codigo_produto = input("Informe o código do produto a ser removido : ").strip()

		continua_002 = True
		while continua_002 == True:

			for produto in lista_produtos:
				trigger = True # Variável responável por guardar informação sobre item pesquisado.

				if produto["Codigo"] == codigo_produto:
					trigger = False
					esc_001 = str(input(f"\033[1;31mDeseja remover o produto :\033[m {produto['Nome']} \033[1;31m?\033[m [ S / N ]")).strip().lower()[0]

					if esc_001 == "s":
						lista_produtos.remove(produto)
						atualizar_base(lista_produtos)
						print(f"O produto {produto['Nome']} com {produto['Quantidade']} unidade(s) foi removido com sucesso !")
						continua_001 = True
						continua_002 = False
						break

					elif esc_001 == "n":
						print("\033[1;33mO produto não foi removido.\033[m")
						continua_001 = True
						continua_002 = False
						break

					else:
						print("Opção inválida !")
						continua_001 = True
						continua_002 = True
						break

				elif produto["Codigo"] != codigo_produto:
					continua_002 = False
					#break Não pode ter break pois se o item não for achado de primeira, quebra a pesquisa.

			if trigger == True:
				print("\033[1;31mCódigo do produto não encontrado ou inválido ! Tente novamente ...\033[m")

		continua_003 = True
		while continua_003 == True:
			esc_001 = input("\nDeseja voltar ao menu principal [ S / N ] ? ").lower()[0]
			if esc_001 == "s":
				continua_001 = False
				continua_003 = False

			elif esc_001 == 'n':
				continua_001 = True
				continua_003 = False

			else:
				print("Opção inválida !")
				continua_001 = True
				continua_003 = True


# SALVA OS DADOS DO PRODUTO NO ARQUIVO
def salvar_produto(dados_produto):
	with open('produtos.txt', 'a') as produtos:
		produtos.write(f'{str(dados_produto)}\n')


# CARREGA OS DADOS DO PRODUTO QUE ESTÃO SALVOS NO ARQUIVO
def ler_produtos():
	with open('produtos.txt', 'r') as produtos:
		lista = produtos.readlines()

	for linha in lista:
		lista_produtos.append(eval(linha.strip()))

	return lista_produtos


def atualizar_base(l_pro):
	with open('produtos.txt', 'w') as base:
		base.write('')
	for produto in l_pro:
		salvar_produto(produto)


# PROGRAMA PRINCIPAL
ler_produtos()
menu_principal()



# Comandos para melhor entendimento da lista de produtos onde cada item da lista é um dicionário
''' 
for contador in range ( 0, len(lista_produtos)) :
for k, v in lista_produtos[0].items() :
	print(f"a chave é {k} e o valor é {v}")	
'''
