import numpy as np

# Inicializando o resultado
r = 0

# Gerando 10 números aleatórios únicos entre 1 e 10
d0 = np.random.choice(range(1, 11), 10, replace=False)

# Separando os primeiros 5 números em ordem crescente
d1 = sorted(d0[:5])

# Separando os últimos 5 números em ordem decrescente
d2 = sorted(d0[5:], reverse=True)

# Inicializando a lista para armazenar as diferenças absolutas
d3 = [abs(d1[i] - d2[i]) for i in range(5)]

# Calculando o resultado
r = sum(d3)

# Imprimindo os resultados
print(d1)
print(d2)
print(d3)
print(r)