# vetor com os valores de faturamento diário
faturamento_diario = [1500, 1200, 1700, 1300, 1900, 1100, 1600, 1400, 1800, 2000, 1000, 1500, 1700, 1300, 1600, 1400, 1900, 1200, 1800, 1300, 1700, 1500, 1600, 1900, 2000, 1500, 1700, 1200, 1600, 1800]

# menor valor de faturamento
menor_valor = min(faturamento_diario)

# maior valor de faturamento
maior_valor = max(faturamento_diario)

# média mensal de faturamento
media_mensal = sum(faturamento_diario) / len(faturamento_diario)

# número de dias com faturamento acima da média mensal
dias_acima_media = len([valor for valor in faturamento_diario if valor > media_mensal])

# exibindo os resultados
print("Menor valor de faturamento: R$", menor_valor)
print("Maior valor de faturamento: R$", maior_valor)
print("Número de dias com faturamento acima da média: ", dias_acima_media)