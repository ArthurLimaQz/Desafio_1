# VARIÁVEIS DE ENTRADA
mes_1 = float(input('Qual o consumo do 3º último mês? '))
mes_2 = float(input('Qual o consumo do 2º último mês? '))
mes_3 = float(input('Qual o consumo do último mês? '))

# Faixas de consumo (em kWh)
BAIXO_CONSUMO = 10_000
ALTO_CONSUMO = 20_000

# Tarifas únicas (por kWh)
TARIFA_RESIDENCIAL = 0.60
TARIFA_COMERCIAL = 0.70
TARIFA_INDUSTRIAL = 0.50

# Descontos por faixa de consumo
# Residencial
DESCONTO_RESID_BAIXO = 18 / 100
DESCONTO_RESID_MEDIO = 15 / 100
DESCONTO_RESID_ALTO = 10 / 100

# Comercial
DESCONTO_COM_BAIXO = 16 / 100
DESCONTO_COM_MEDIO = 12 / 100
DESCONTO_COM_ALTO = 8 / 100

# Industrial
DESCONTO_IND_BAIXO = 12 / 100
DESCONTO_IND_MEDIO = 8 / 100
DESCONTO_IND_ALTO = 5 / 100

# Cobertura por faixa de consumo
COBERTURA_BAIXO = 0.90  # 90%
COBERTURA_MEDIO = 0.95  # 95%
COBERTURA_ALTO = 0.99   # 99%

# Cálculo da média de consumo
consumo_medio = (mes_1 + mes_2 + mes_3) / 3

# Determinação dos descontos e cobertura com base no consumo médio
if consumo_medio < BAIXO_CONSUMO:
    desconto_residencial = DESCONTO_RESID_BAIXO
    desconto_comercial = DESCONTO_COM_BAIXO
    desconto_industrial = DESCONTO_IND_BAIXO
    cobertura = COBERTURA_BAIXO
elif BAIXO_CONSUMO <= consumo_medio <= ALTO_CONSUMO:
    desconto_residencial = DESCONTO_RESID_MEDIO
    desconto_comercial = DESCONTO_COM_MEDIO
    desconto_industrial = DESCONTO_IND_MEDIO
    cobertura = COBERTURA_MEDIO
else:
    desconto_residencial = DESCONTO_RESID_ALTO
    desconto_comercial = DESCONTO_COM_ALTO
    desconto_industrial = DESCONTO_IND_ALTO
    cobertura = COBERTURA_ALTO

# Função para calcular valores com desconto e aplicar a cobertura
def calcular_valores(consumo, tarifa, desconto, cobertura):
    valor_sem_desconto = consumo * tarifa
    valor_com_desconto = valor_sem_desconto * (1 - desconto)
    valor_com_cobertura = valor_com_desconto * cobertura
    economia = valor_sem_desconto - valor_com_cobertura
    return valor_com_cobertura, economia

# Cálculos para cada categoria
residencial_final, economia_residencial = calcular_valores(
    consumo_medio, TARIFA_RESIDENCIAL, desconto_residencial, cobertura
)
comercial_final, economia_comercial = calcular_valores(
    consumo_medio, TARIFA_COMERCIAL, desconto_comercial, cobertura
)
industrial_final, economia_industrial = calcular_valores(
    consumo_medio, TARIFA_INDUSTRIAL, desconto_industrial, cobertura
)

# Exibir resultados
print("\nResultados para o consumo médio de {:.2f} kWh:".format(consumo_medio))
print(f"Residencial: Valor final (após cobertura): R$ {residencial_final:.2f}, Economia: R$ {economia_residencial:.2f}")
print(f"Comercial: Valor final (após cobertura): R$ {comercial_final:.2f}, Economia: R$ {economia_comercial:.2f}")
print(f"Industrial: Valor final (após cobertura): R$ {industrial_final:.2f}, Economia: R$ {economia_industrial:.2f}")

# Economia anual para cada categoria
economia_anual_residencial = economia_residencial * 12
economia_anual_comercial = economia_comercial * 12
economia_anual_industrial = economia_industrial * 12

print("\nEconomia anual estimada:")
print(f"Residencial: R$ {economia_anual_residencial:.2f}")
print(f"Comercial: R$ {economia_anual_comercial:.2f}")
print(f"Industrial: R$ {economia_anual_industrial:.2f}")
