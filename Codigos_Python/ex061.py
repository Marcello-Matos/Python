import itertools

# Número total de elementos e número de elementos a serem escolhidos
total_numeros = 25
quantidade_escolhida = 15

# Gerar todas as combinações
combinacoes = list(itertools.combinations(range(1, total_numeros + 1), quantidade_escolhida))

# Exibir as combinações
for i, combinacao in enumerate(combinacoes, start=1):
    print(f"Combinação {i}: {combinacao}")
