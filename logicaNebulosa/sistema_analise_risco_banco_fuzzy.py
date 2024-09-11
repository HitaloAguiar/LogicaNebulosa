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

credito.view()
plt.show()

renda.view()
plt.show()

divida.view()
plt.show()

risco.view()
plt.show()

# rule1 = ctrl.Rule(quality['poor'] | service['poor'], tip['low'])
# rule2 = ctrl.Rule(service['average'], tip['medium'])
# rule3 = ctrl.Rule(service['good'] | quality['good'], tip['high'])

# rule1.view()
# plt.show()

# tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

# tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

# tipping.input['quality'] = 6.5
# tipping.input['service'] = 9.8

# tipping.compute()

# print(tipping.output['tip'])
# tip.view(sim=tipping)
# plt.show()
