import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

credito = ctrl.Antecedent(np.arange(0, 11, 1), 'credito')
renda = ctrl.Antecedent(np.arange(0, 11, 1), 'renda')
divida = ctrl.Antecedent(np.arange(0, 11, 1), 'divida')

risco = ctrl.Consequent(np.arange(0, 11, 1), 'risco')

credito['Ruim'] = fuzz.trimf(credito.universe, [0, 2, 4])
credito['Regular'] = fuzz.trimf(credito.universe, [2, 4, 6])
credito['Bom'] = fuzz.trimf(credito.universe, [4, 6, 8])
credito['Excelente'] = fuzz.trimf(credito.universe, [6, 8, 10])

renda['Baixa'] = fuzz.trimf(renda.universe, [0, 0, 5])
renda['Média'] = fuzz.trimf(renda.universe, [0, 5, 10])
renda['Alta'] = fuzz.trimf(renda.universe, [5, 10, 10])

divida['Baixa'] = fuzz.trimf(divida.universe, [0, 0, 5])
divida['Moderada'] = fuzz.trimf(divida.universe, [0, 5, 10])
divida['Alta'] = fuzz.trimf(divida.universe, [5, 10, 10])

risco['Baixo'] = fuzz.trimf(risco.universe, [0, 0, 5])
risco['Médio'] = fuzz.trimf(risco.universe, [0, 5, 10])
risco['Alto'] = fuzz.trimf(risco.universe, [5, 10, 10])

# credito.view()
# plt.show()

# renda.view()
# plt.show()

# divida.view()
# plt.show()

# risco.view()
# plt.show()

rule1 = ctrl.Rule(credito['Excelente'] & divida['Baixa'], risco['Baixo']) # SE o histórico de crédito é "Excelente" E a dívida atual é "Baixa", ENTÃO o risco é "Baixo. Independente da renda"
rule2 = ctrl.Rule(credito['Ruim'] & divida['Alta'], risco['Alto']) # SE o histórico de crédito é "Ruim" E a dívida atual é "Alta", ENTÃO o risco é "Alto". Independente da renda
rule3 = ctrl.Rule(credito['Bom'] & renda['Média'] & divida['Moderada'], risco['Médio']) # SE o histórico de crédito é "Bom" E a renda mensal é "Média" E a dívida atual é "Moderada", ENTÃO o risco é "Médio"
rule4 = ctrl.Rule(credito['Regular'] & divida['Moderada'], risco['Médio']) # SE o histórico de crédito é "Regular" E a dívida atual é "Moderada", o risco é "Moderado". A menos que a renda seja baixa

rule5 = ctrl.Rule(credito['Excelente'] & divida['Moderada'], risco['Baixo'])
rule6 = ctrl.Rule(credito['Excelente'] & divida['Alta'], risco['Baixo'])
rule7 = ctrl.Rule(credito['Excelente'] & divida['Alta'] & renda['Baixa'], risco['Médio'])

rule8 = ctrl.Rule(credito['Bom'] & divida['Alta'], risco['Médio'])
rule9 = ctrl.Rule(credito['Bom'] & divida['Moderada'] & renda['Alta'], risco['Baixo'])
rule10 = ctrl.Rule(credito['Bom'] & divida['Moderada'] & renda['Baixa'], risco['Médio'])
rule11 = ctrl.Rule(credito['Bom'] & divida['Baixa'], risco['Baixo'])

rule12 = ctrl.Rule(credito['Regular'] & divida['Moderada'] & renda['Baixa'], risco['Alto'])
rule13 = ctrl.Rule(credito['Regular'] & divida['Alta'], risco['Alto'])
rule14 = ctrl.Rule(credito['Regular'] & divida['Baixa'], risco['Médio'])

rule15 = ctrl.Rule(credito['Ruim'] & divida['Moderada'], risco['Alto'])
rule16 = ctrl.Rule(credito['Ruim'] & divida['Baixa'], risco['Alto'])
rule17 = ctrl.Rule(credito['Ruim'] & divida['Baixa'] & renda['Alta'], risco['Médio'])

banco_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17])

banco = ctrl.ControlSystemSimulation(banco_ctrl)

banco.input['credito'] = 9.6
banco.input['renda'] = 2
banco.input['divida'] = 7.5

banco.compute()

resultado = banco.output['risco']

if resultado <= 3:
    rotulo = "Baixo"
elif resultado >= 7:
    rotulo = "Alto"
else:
    rotulo = "Médio"

print(f"Resultado numérico: {resultado}")
print(f"Rótulo do resultado: Risco {rotulo}")
risco.view(sim=banco)
plt.show()
