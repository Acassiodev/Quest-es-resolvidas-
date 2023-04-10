 # Define um dicionário com os valores de faturamento por estado
faturamento_mensal = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcula o valor total mensal de faturamento
total_mensal = sum(faturamento_mensal.values())

# Calcula o percentual de representação de cada estado
representacao_por_estado = {}
for estado, faturamento in faturamento_mensal.items():
    representacao_por_estado[estado] = faturamento / total_mensal * 100

# Imprime os resultados
for estado, representacao in representacao_por_estado.items():
    print(f"{estado}: {representacao:.2f}%")