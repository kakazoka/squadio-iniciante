capacidade_atual, aumento_percentual = map(int, input().split())

percentual = int(capacidade_atual * (aumento_percentual / 100))
nova_capacidade = int(capacidade_atual + percentual)

print(nova_capacidade)
