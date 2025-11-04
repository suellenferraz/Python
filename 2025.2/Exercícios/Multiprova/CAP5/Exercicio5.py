def total(lista):
    return sum(lista)

def maior_estudo(lista):
    dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    indice = lista.index(max(lista))
    return dias[indice]

def produtividade_por_dia(estudo, celular):
    porcentagens = []
    for e, c in zip(estudo, celular):
        if e + c == 0:
            porcentagens.append(0)
        else:
            porcentagens.append(round((e / (e + c)) * 100, 2))
    return porcentagens

estudo = list(map(int, input().split(',')))
celular = list(map(int, input().split(',')))

total_estudo = total(estudo)
total_celular = total(celular)
dia_maior = maior_estudo(estudo)
produtividade = produtividade_por_dia(estudo, celular)

print(f'Total de horas de estudo: {total_estudo}')
print(f'Total de horas no celular: {total_celular}')
print(f'Dia com maior estudo: {dia_maior}')
print('Produtividade por dia:')

dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
for dia, p in zip(dias, produtividade):
    print(f'- {dia}: {p:.2f}%')

if total_estudo > total_celular:
    print('Você estudou mais do que usou o celular esta semana. 📚')
elif total_estudo < total_celular:
    print('Você usou mais o celular do que estudou esta semana. 😬')
else:
    print('Você estudou e usou o celular por igual esta semana. ⚖️')
