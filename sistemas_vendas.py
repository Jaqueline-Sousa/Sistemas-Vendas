import os

estoque = {
    1: {"nome": "Elden Ring (Mídia Física)", "preco": 250.00, "quantidade": 8, "tipo": "Física"},
    2: {"nome": "Elden Ring (Mídia Digital)", "preco": 220.00, "quantidade": 999, "tipo": "Digital"},
    3: {"nome": "GTA VI (Mídia Física)", "preco": 349.90, "quantidade": 5, "tipo": "Física"},
    4: {"nome": "GTA VI (Mídia Digital)", "preco": 299.90, "quantidade": 999, "tipo": "Digital"},
    5: {"nome": "The Witcher 3 (Mídia Digital)", "preco": 40.00, "quantidade": 999, "tipo": "Digital"},
    6: {"nome": "Nintendo Switch Sports (Física)", "preco": 280.00, "quantidade": 4, "tipo": "Física"}
}

carrinho = []


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def exibir_cabecalho(titulo):
    print("\n" + "=" * 65)
    print(f"{titulo.upper().center(65)}")
    print("=" * 65)


def visualizar_estoque():
    exibir_cabecalho("Catálogo de Jogos Disponíveis")
    print(f"{'ID':<4} | {'Nome do Jogo':<30} | {'Tipo':<8} | {'Preço':<9} | {'Estoque':<7}")
    print("-" * 69)
    for id_prod, info in estoque.items():
        # Se for digital, exibe "Ilimitado" ou a quantidade de Keys
        qtd_exibida = "Ilimitado" if info['tipo'] == "Digital" else info['quantidade']
        print(f"{id_prod:<4} | {info['nome']:<30} | {info['tipo']:<8} | R$ {info['preco']:>6.2f} | {qtd_exibida:^7}")
    print("-" * 69)



def adicionar_item_carrinho():
    visualizar_estoque()

    try:
        id_escolhido = int(input("\nDigite o ID do jogo que deseja comprar: "))
    except ValueError:
        print("\n Erro: O ID deve ser um número inteiro.")
        return

    if id_escolhido not in estoque:
        print("\n Erro: Jogo não encontrado no catálogo.")
        return

    jogo = estoque[id_escolhido]

    try:
        qtd_desejada = int(input(f"Digite a quantidade de '{jogo['nome']}' desejada: "))
    except ValueError:
        print("\n Erro: A quantidade deve ser um número inteiro.")
        return


    if qtd_desejada <= 0:
        print("\n Erro: A quantidade deve ser maior do que zero.")
        return

    if jogo["tipo"] == "Física" and qtd_desejada > jogo["quantidade"]:
        print(f"\n Erro: Estoque insuficiente. Temos apenas {jogo['quantidade']} unidades físicas.")
        return
    elif jogo["tipo"] == "Digital" and qtd_desejada > jogo["quantidade"]:
        print(f"\n Erro: Não há chaves (keys) digitais suficientes no momento.")
        return


    estoque[id_escolhido]["quantidade"] -= qtd_desejada

    item_ja_no_carrinho = False
    for item in carrinho:
        if item["id"] == id_escolhido:
            item["quantidade"] += qtd_desejada
            item_ja_no_carrinho = True
            break

    if not item_ja_no_carrinho:
        carrinho.append({
            "id": id_escolhido,
            "nome": jogo["nome"],
            "tipo": jogo["tipo"],
            "preco_unitario": jogo["preco"],
            "quantidade": qtd_desejada
        })

    print(f"\n Sucesso: {qtd_desejada}x '{jogo['nome']}' adicionado ao carrinho!")


def calcular_subtotal():
    subtotal = 0.0
    for item in carrinho:
        subtotal += item["preco_unitario"] * item["quantidade"]
    return subtotal


def visualizar_carrinho():
    exibir_cabecalho("Seu Carrinho de Compras")

    if not carrinho:
        print("Seu carrinho está vazio no momento.".center(65))
        print("=" * 65)
        return False

    print(f"{'Qtd':<4} | {'Nome do Jogo':<30} | {'Tipo':<8} | {'Unitário':<9} | {'Total':<9}")
    print("-" * 69)

    for item in carrinho:
        total_item = item["preco_unitario"] * item["quantidade"]
        print(
            f"{item['quantidade']:^4} | {item['nome']:<30} | {item['tipo']:<8} | R$ {item['preco_unitario']:>6.2f} | R$ {total_item:>6.2f}")

    print("-" * 69)
    subtotal = calcular_subtotal()
    print(f"{'SUBTOTAL:':>53} R$ {subtotal:>7.2f}")
    print("=" * 65)
    return True


def finalizar_compra():
    if not visualizar_carrinho():
        print("\n⚠️ Não é possível finalizar a compra com o carrinho vazio.")
        return

    subtotal = calcular_subtotal()
    desconto = 0.0

    cupom = input("\nPossui cupom de desconto de Gamer? (Deixe em branco se não tiver): ").strip().upper()

    if cupom == "DEV10":
        desconto = subtotal * 0.10
        print("🎉 Cupom DEV10 aplicado! 10% de desconto garantido.")
    elif cupom == "DEV20":
        if subtotal > 500.00:
            desconto = subtotal * 0.20
            print(" Cupom DEV20 aplicado! 20% de desconto garantido.")
        else:
            print("⚠️ Cupom DEV20 só é válido para compras acima de R$ 500.00. (Prosseguindo sem desconto).")
    elif cupom != "":
        print("⚠️ Cupom inválido ou expirado. (Prosseguindo sem desconto).")

    total_a_pagar = subtotal - desconto


    exibir_cabecalho("Resumo do Pedido")
    print(f"{'Subtotal:':<45} R$ {subtotal:>10.2f}")
    print(f"{'Desconto aplicado:':<45} R$ {desconto:>10.2f}")
    print("-" * 65)
    print(f"{'TOTAL A PAGAR:':<45} R$ {total_a_pagar:>10.2f}")
    print("=" * 65)


    while True:
        confirmacao = input("\nConfirmar pagamento? (S/N): ").strip().upper()

        if confirmacao == 'S':
            print("\n Pagamento Confirmado! ✨")


            tem_digital = any(item["tipo"] == "Digital" for item in carrinho)
            if tem_digital:
                print(" As chaves (keys) de ativação dos jogos digitais foram enviadas para o seu e-mail!")

            carrinho.clear()
            break
        elif confirmacao == 'N':
            print("\n Compra cancelada. Devolvendo jogos ao estoque principal...")

            for item in carrinho:
                estoque[item["id"]]["quantidade"] += item["quantidade"]
            carrinho.clear()
            print("Operação desfeita com sucesso.")
            break
        else:
            print("Opção inválida! Digite 'S' para Sim ou 'N' para Não.")


def menu_principal():
    while True:
        print("\n" + "#" * 65)
        print(" GAME STORE TERMINAL SYSTEM ".center(65, "#"))
        print("#" * 65)
        print("[1] Visualizar Catálogo de Jogos")
        print("[2] Adicionar Jogo ao Carrinho")
        print("[3] Visualizar Meu Carrinho")
        print("[4] Finalizar Compra / Checkout")
        print("[0] Sair do Sistema")
        print("#" * 65)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            limpar_tela()
            visualizar_estoque()
        elif opcao == "2":
            limpar_tela()
            adicionar_item_carrinho()
        elif opcao == "3":
            limpar_tela()
            visualizar_carrinho()
        elif opcao == "4":
            limpar_tela()
            finalizar_compra()
        elif opcao == "0":
            print("\nObrigado por usar a Game Store. Boa jogatina!")
            break
        else:
            limpar_tela()
            print("\n Erro: Opção inválida! Selecione uma opção válida do menu.")

if __name__ == "__main__":
    limpar_tela()
    menu_principal()