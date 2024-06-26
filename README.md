
 Luan Silveira Macea- RM 98290
 Luigi Ferrara- RM 98047
 Pedro Henrique Bicas Couto- RM 99534
 
 # Detecção de Lixo no Mar com Sensores Tridimensionais

Este é um programa Python que simula a detecção de lixo no mar utilizando sensores tridimensionais. Ele gera um gráfico tridimensional mostrando a distribuição dos sensores, o lixo presente e quantidades de lixo detectado por cada sensor.

## Como Executar o Código

1. **Instalar Dependências:**
   Certifique-se de ter o Matplotlib e o NumPy instalados. Se não tiver, você pode instalá-los via pip:
   ```
   pip install matplotlib numpy
   ```

2. **Executar o Código:**
   - Baixe o código fornecido e salve-o como um arquivo Python (por exemplo, `detecao_lixo_mar.py`).
   - Abra um terminal ou prompt de comando na pasta onde o arquivo Python está localizado.
   - Execute o código Python digitando:
     ```
     python detecao_lixo_mar.py
     ```
   - Siga as instruções no terminal para fornecer valores personalizados (opcional) ou use os valores padrão.

## Inputs do Usuário (Valores Personalizados)

- **Alcance Máximo da Área do Gráfico em km:** Define o tamanho máximo da área do gráfico em quilômetros.
- **Quantidade de Sensores:** Especifica o número de sensores a serem utilizados na detecção.
- **Alcance do Raio de Cada Sensor em km:** Define o alcance do raio de cada sensor em quilômetros.
- **Quantidade Total de Lixos Presentes:** Determina o número total de "lixos" presentes na área.


# Função para criar sensores

Esta função, `criar_sensores`, é projetada para gerar coordenadas de sensores de forma aleatória, garantindo que não haja colisões entre eles. Isso é útil em cenários onde é necessário simular a distribuição de sensores em uma área delimitada.

## Lógica do código

1. **Inicialização das coordenadas**: A função inicializa um array `coord_sensores` de forma `(num_sensores, 3)`, onde `num_sensores` é o número de sensores desejados e `3` representa as coordenadas `(x, y, z)` de cada sensor.

2. **Geração de coordenadas**: Para cada sensor a ser criado (`for i in range(num_sensores)`), a função executa o seguinte procedimento:

   - **Posição Potencial**: Gera uma posição potencial para o sensor dentro de um limite definido.
   
   - **Verificação de colisão**: Verifica se a nova posição colide com qualquer sensor já existente. Se este não for o primeiro sensor (ou seja, `i > 0`), calcula as distâncias entre a nova posição e as posições dos sensores já existentes. Se alguma dessas distâncias for menor que `2*raio` (onde `raio` é o raio de cada sensor), isso significa que há uma colisão.
   
   - **Adição à lista**: Se não houver colisão, a nova posição é adicionada à lista de coordenadas de sensores.

3. **Retorno**: Retorna a matriz de coordenadas de sensores resultante, onde cada linha representa as coordenadas `(x, y, z)` de um sensor.

## Parâmetros

- `raio`: O raio de cada sensor.
- `num_sensores`: O número total de sensores a serem criados.
- `limite`: Os limites da área onde os sensores serão distribuídos.

## Exemplo de Uso

```python
import numpy as np

# Definindo parâmetros
raio = 1
num_sensores = 10
limite = 100

# Chamando a função para criar os sensores
coordenadas_sensores = criar_sensores(raio, num_sensores, limite)

print(coordenadas_sensores)
```

# Função para Verificar Lixo Encontrado por Sensores

Esta função, `verificar_lixo_encontrado`, é utilizada para contabilizar a quantidade de "lixo" encontrada por cada sensor em uma determinada área. A detecção de lixo é baseada na proximidade entre os sensores e as posições dos lixos.

## Lógica do Código

1. **Inicialização do Array de Contagem**: A função inicializa um array `lixo_encontrado` de tamanho `num_sensores`, onde cada elemento representa a quantidade de lixo encontrada pelo respectivo sensor.

2. **Verificação de Proximidade**: Para cada sensor (`for i in range(num_sensores)`) e cada posição de lixo (`for j in range(num_lixos)`), a função calcula a distância entre o sensor e o lixo.

3. **Contagem de Lixo**: Se a distância entre o sensor e o lixo for menor ou igual ao raio de detecção (`raio`), o sensor é considerado capaz de detectar o lixo e a contagem correspondente é incrementada.

4. **Retorno**: Retorna o array `lixo_encontrado`, onde cada elemento representa a quantidade de lixo encontrada pelo respectivo sensor.

## Parâmetros

- `num_sensores`: O número total de sensores.
- `num_lixos`: O número total de posições de lixo a serem verificadas.
- `coord_sensores`: As coordenadas dos sensores.
- `coord_lixos`: As coordenadas dos lixos.
- `raio`: O raio de detecção de cada sensor.

## Exemplo de Uso

```python
import numpy as np

# Definindo parâmetros
num_sensores = 5
num_lixos = 10
raio = 2

# Gerando coordenadas aleatórias para os sensores e os lixos (para exemplo)
coord_sensores = np.random.rand(num_sensores, 3) * 100
coord_lixos = np.random.rand(num_lixos, 3) * 100

# Chamando a função para verificar o lixo encontrado por cada sensor
lixo_encontrado = verificar_lixo_encontrado(num_sensores, num_lixos, coord_sensores, coord_lixos, raio)

print(lixo_encontrado)
```

# referencias 
documentação oficial matplotlib 
https://matplotlib.org/stable/gallery/mplot3d/index.html
obs: este é apenas um link especifico para a criação de graficos 3d, porem eu li muitas outras paginas da documentação oficial

documentação oficial numpy 
https://numpy.org/doc/
obs: este é apenas um link especifico para a pagina oficial dentro da documentação da numpy, porem eu acessei diversas paginas da documentação oficial tambem

video do neuralnine 
https://www.youtube.com/watch?v=fAztJg9oi7s&t=3s
um video que me ensinou a usar melhor o matplotlib

site ichi.pro
https://ichi.pro/pt/visualizacao-3d-python-com-matplotlib-143507198304171
me ensinou a usar melhor o matplotlib
