import os

lista_produtos = list()
itens = dict()


# ROTINA PARA LIMPAR A TELA
def limpa_tela():
	os.system('cls')


# ROTINA PARA EXIBIR O MENU PRINCIPAL
def menu_principal():
	limpa_tela()
	continua_001 = True
	while continua_001 == True:
		print(f"{'MENU PRINCIPAL':<45}")
		print()
		print(f"{'1 - ':<3}{'Cadastro de itens':<45}")
		print(f"{'2 - ':<3}{'Consulta geral':<45}")
		print(f"{'3 - ':<3}{'Remoção de itens':<45}")
		print(f"{'4 - ':<3}{'Reservado ao sistema':<45}")
		print(f"{'5 - ':<3}{'Reservado ao sistema':<45}")
		print(f"{'6 - ':<3}{'Reservado ao sistema':<45}")
		print(f"{'9 - ':<3}{'SAIR':<45}")
		esc_001 = str(input("\nDigite uma opção : "))

		if esc_001 == "1":
			cadastrar()

		elif esc_001 == "2":
			consultar()

		elif esc_001 == "3":
			remover()

		elif esc_001 == "4": # Menu criado apenas para fins de teste e recordação de dicionários dentro de listas
			print(lista_produtos)

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
	limpa_tela()
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
				itens['Codigo'] = input("\nDigite o código do produto : ")
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


# A partir daqui Mario, tenta ajustar esse trecho para baixo

		itens["Nome"] = str(input("Digite o nome do produto : ")).strip()

		itens["Descricao"] = str(input("Digite a descrição do produto : ")).strip()

		while True:
			quantidade_itens = input("Digite a quantidade a ser cadastrada : ")
			if quantidade_itens.isdigit():
				itens["Quantidade"] = quantidade_itens
				break
			print("Quantidade inválida !")

		while True:
			valor_item = input("Digite o valor unitário do produto : ").strip().replace(',', '.')
			try:
				valor_item = float(valor_item)
			except:
				pass
			if isinstance(valor_item, float):
				itens["Valor"] = valor_item
				break
			print('O valor informado é inválido !')

# Até aqui por enquanto.

	valor_item = float(valor_item)
	quantidade_itens = int(quantidade_itens)

	itens["valor total"] = ( quantidade_itens * valor_item )

	print()

	lista_produtos.append(itens.copy())
	salvar_produto(itens)
	itens.clear()


# ROTINA PARA EXIBIR O MENU CONSULTAR
def consultar():
	limpa_tela()
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
		limpa_tela()
		print("\nMENU REMOÇÃO DE PRODUTO CADASTRADO\n")
		consultar_simples()
		codigo_produto = input("Informe o código do produto a ser removido : ").strip()

		for item in lista_produtos:
			if item["Codigo"] == codigo_produto:
				produto = item
				lista_produtos.remove(item)
				print(f"O produto {item['Nome']} foi removido com sucesso !")
				break

		atualizar_base(lista_produtos)

		continua_001 = input("Deseja voltar ao menu principal [ S / N ] ? ").lower()
		if continua_001 == "s":
			break
		else :
			continua_001 = False


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
print(f"\n{'Programa : Cadastro 1.0':<60}")

ler_produtos()

menu_principal()
