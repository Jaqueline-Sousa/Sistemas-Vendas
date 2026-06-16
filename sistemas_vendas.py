estoque = {
    1: {"nome": "Elden Ring (Mídia Física)", "preco": 250.00, "quantidade": 8, "tipo": "Física"},
    2: {"nome": "Elden Ring (Mídia Digital)", "preco": 220.00, "quantidade": 999, "tipo": "Digital"},
    3: {"nome": "GTA VI (Mídia Física)", "preco": 349.90, "quantidade": 5, "tipo": "Física"},
    4: {"nome": "GTA VI (Mídia Digital)", "preco": 299.90, "quantidade": 999, "tipo": "Digital"},
    5: {"nome": "The Witcher 3 (Mídia Digital)", "preco": 40.00, "quantidade": 999, "tipo": "Digital"},
    6: {"nome": "Nintendo Switch Sports (Física)", "preco": 280.00, "quantidade": 3, "tipo": "Física"}
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