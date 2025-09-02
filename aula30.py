"""
CONSTANTE = "Variáveis" que não vão mudar 
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 61  # Velocidade atual do carro
local_carro = 100  # Localização atual do carro

RADAR_1 = 60  # Limite de velocidade do radar 1
LOCAL_1 = 100  # Localização do radar 1
RADAR_RANGE = 1  # Alcance do radar


velocidade_carro_passou_radar1 = velocidade > RADAR_1
carro_passou_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar1 = velocidade_carro_passou_radar1 and carro_passou_radar1

if carro_passou_radar1:
    print('Carro passou no radar 1')

if carro_multado_radar1:
    print('Multado no radar 1')

