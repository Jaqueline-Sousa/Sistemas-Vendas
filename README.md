Projeto Final da UC 3: Desenvolver algoritmos 
Data de conclusão 19 de junho de 2026 às 23:59
Instruções
Projeto Prático: Sistema de Vendas em Terminal (E-Commerce)

Contexto do Desafio
Você foi contratado para desenvolver o protótipo funcional do sistema de vendas via terminal para uma plataforma de e-commerce. O objetivo é criar um script em Python que simule a experiência de um cliente: visualizar produtos, gerenciar um carrinho de compras, aplicar cupons de desconto e consolidar o estoque físico em tempo real.Requisitos Técnicos do Sistema

1. Estrutura de Dados (Banco de Dados Simulado)
Estoque: Deve ser implementado utilizando um dicionário, onde a chave é o ID numérico do produto e o valor é outro dicionário contendo as propriedades do produto: nome (string), preco (float) e quantidade (inteiro).
Carrinho de Compras: Deve ser uma lista dinâmica que armazenará temporariamente os itens selecionados pelo usuário (cada item no carrinho também será um dicionário contendo ID, nome, preço unitário e a quantidade escolhida).
2. Menu Interativo e Fluxo de Navegação
O sistema deve rodar em um loop contínuo (while), exibindo um menu textual com as seguintes opções:

[1] Visualizar Estoque
[2] Adicionar Item ao Carrinho
[3] Visualizar Carrinho
[4] Finalizar Compra
[0] Sair do Sistema
Atenção: Caso o usuário digite uma opção inválida, o sistema deve exibir uma mensagem de erro e reapresentar o menu.

Requisitos Funcionais (Regras de Negócio)
A. Visualização de Estoque
Exibir uma tabela formatada na tela mostrando todos os produtos cadastrados no sistema com suas respectivas colunas: ID, Nome, Preço (R$) e Quantidade em Estoque.
B. Adicionar Itens ao Carrinho
Ao selecionar esta opção, o sistema deve listar o estoque e solicitar o ID do produto e a quantidade desejada. O código precisa validar os seguintes cenários:

Produto Inexistente: Validar se o ID informado existe no estoque.
Quantidade Inválida: Impedir a inserção de valores menores ou iguais a zero.
Validação de Estoque: Impedir a venda se a quantidade solicitada for maior do que a disponível no estoque.
Reserva de Estoque: Se a validação passar, o item vai para o carrinho e a quantidade é subtraída temporariamente do estoque principal.
C. Visualizar Carrinho
Listar todos os itens adicionados até o momento informando a quantidade, o nome, o valor unitário e o total acumulado daquele item.
Exibir ao final o Subtotal atual da compra.
Se o carrinho estiver vazio, exibir uma mensagem informando o usuário.
D. Finalizar Compra
Se o carrinho possuir itens, o sistema iniciará o checkout seguindo as regras:

Sistema de Cupons de Desconto: Solicitar ao usuário um cupom). As regras são:
Cupom DEV10: Garante 10% de desconto sobre o subtotal.
Cupom DEV20: Garante 20% de desconto, mas apenas se o subtotal da compra for maior que R$ 500.00.
Outros cupons digitados devem ser tratados como inválidos (prosseguindo sem desconto).
Resumo do Pedido: Exibir um painel final com o valor do Subtotal, o Desconto aplicado e o Total a Pagar.
Confirmação de Pagamento: Perguntar se o usuário confirma o pagamento (S/N):
Se SIM (S): Exibir mensagem de sucesso e limpar (clear) o carrinho.
Se NÃO (N): Cancelar a operação e devolver obrigatoriamente todas as quantidades dos produtos do carrinho de volta para o estoque principal, limpando o carrinho em seguida.
Critérios de Avaliação
Organização do código em funções específicas (def).
Uso correto de estruturas de repetição (while, for) e condicionais (if, elif, else).
Manipulação correta de dicionários e listas.
Alinhamento e formatação visual das saídas de dados no terminal.
