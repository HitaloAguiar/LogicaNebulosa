---

# Algoritmo Fuzzy para Análise de Risco de Crédito

Este é um algoritmo fuzzy para avaliar o risco de crédito com base em três variáveis de entrada: histórico de crédito, renda e dívida. O sistema fuzzy classifica o risco como Baixo, Médio ou Alto, fornecendo um resultado numérico e um rótulo correspondente.

## Instalação

### Requisitos
- Python 3.x
- Bibliotecas Python:
  - `numpy`
  - `scikit-fuzzy`
  - `matplotlib`

### Instruções de instalação

1. Clone este repositório ou baixe o código.

2. Instale as dependências executando o comando:

   ```bash
   pip install numpy scikit-fuzzy matplotlib
   ```

## Variáveis de Entrada (Inputs)

O sistema fuzzy utiliza três variáveis de entrada, cada uma representada por um conjunto fuzzy com valores de 0 a 10:

1. **Crédito (`credito`)**: 
   - Intervalo: 0 a 10
   - Conjuntos fuzzy: `Ruim`, `Regular`, `Bom`, `Excelente`

2. **Renda (`renda`)**: 
   - Intervalo: 0 a 10
   - Conjuntos fuzzy: `Baixa`, `Média`, `Alta`

3. **Dívida (`divida`)**: 
   - Intervalo: 0 a 10
   - Conjuntos fuzzy: `Baixa`, `Moderada`, `Alta`

## Variável de Saída (Output)

- **Risco (`risco`)**: 
  - Intervalo: 0 a 10
  - Conjuntos fuzzy: `Baixo`, `Médio`, `Alto`

O resultado do sistema fuzzy é um valor numérico entre 0 e 10, que é categorizado nos seguintes rótulos:
- **Baixo**: 0 a 3
- **Médio**: 4 a 6
- **Alto**: 7 a 10

## Regras Fuzzy

O sistema fuzzy é controlado por 17 regras. Alguns exemplos são:

- **Regra 1**: Se o crédito é "Excelente" e a dívida é "Baixa", então o risco é "Baixo".
- **Regra 2**: Se o crédito é "Ruim" e a dívida é "Alta", então o risco é "Alto".
- **Regra 3**: Se o crédito é "Bom", a renda é "Média" e a dívida é "Moderada", então o risco é "Médio".
- **Regra 4**: Se o crédito é "Regular" e a dívida é "Moderada", então o risco é "Médio". A menos que a renda seja "Baixa"
- **Regra 12**: Se o crédito é "Regular", a renda é "Baixa" e a dívida é "Moderada", então o risco é "Alto".
- **Regra 17**: Se o crédito é "Ruim", a renda é "Alta" e a dívida é "Baixa", então o risco é "Médio".

## Funcionamento e construção do Sistema

O algoritmo usa lógica fuzzy para combinar entradas (crédito, renda e dívida) e calcular o nível de risco. Baseado nas regras definidas, ele determina o risco com base nos graus de pertinência de cada entrada. Foi entendido do contexto apresentado que a variável 'crédito' possui um grau de influência maior no cálculo de risco e, portanto, as regras foram feitas pensando primeiramente nos valores de crédito. Também tendo em vista o contexto, a variável renda teve uma influência reduzida, tendo importância apenas em casos mais específicos, em geral os casos onde as outras variáveis ('crédito' e 'dívida') estavam em níveis intermediários ou muito discrepantes uma da outra (Exemplo, 'crédito' = "Ruim" e 'dívida' = "Baixa").

### Exemplo de Uso

No código atual, as seguintes entradas são utilizadas:

```python
banco.input['credito'] = 9.6
banco.input['renda'] = 2
banco.input['divida'] = 7.5
```

O sistema calcula o risco com base nessas entradas e fornece o seguinte resultado:

- Resultado numérico: `4.7...`
- Rótulo do risco: `Médio`

Além disso, um gráfico da variável `risco` será exibido para visualização.

## Exemplo de Saída

```bash
Resultado numérico: 4.7
Rótulo do resultado: Risco Médio
```

## Gráficos

O sistema gera gráficos para as variáveis de entrada e saída que podem ser visualizados ao rodar o código.

---